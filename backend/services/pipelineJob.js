import fs from 'fs';
import path from 'path';
import { extractText } from '../utils/pdfExtractor.js';
import { checkRelevance, generateScenes, generateManimCode, isNarrationGeneric, regenerateNarration } from './gemini.js';
import { runManimCodeWithRetry } from './manimRunner.js';
import { mergeVideos } from '../utils/videoMerger.js';
import { generateFallbackVideo } from '../utils/fallbackVideoGenerator.js';
import { syncAudioWithVideo } from './audioService.js';
import { generateQuestionsFromText } from './questionService.js';
import Question from '../models/Question.js';


// Global Job Store
export const jobsStore = {};

// Concurrency limit
const MAX_CONCURRENT_JOBS = 2;
let activeJobs = 0;
const jobQueue = [];

function updateJob(jobId, patch) {
    jobsStore[jobId] = { ...jobsStore[jobId], ...patch };
}

export async function startPipelineJob(jobId, buffer, numMcqs = 0, numShorts = 0, audioLanguage = 'english', focusTopic = "") {


    if (activeJobs >= MAX_CONCURRENT_JOBS) {
        updateJob(jobId, { status: 'queued', statusMessage: 'Waiting in queue...' });
        jobQueue.push({ jobId, buffer, numMcqs, numShorts, audioLanguage, focusTopic });
        return;
    }

    try {
        activeJobs++;
        updateJob(jobId, { status: 'processing', statusMessage: 'Starting pipeline...' });
        await runPipeline(jobId, buffer, numMcqs, numShorts, audioLanguage, focusTopic);


    } catch (error) {
        console.error(`[Job ${jobId}] Pipeline failed:`, error);
        updateJob(jobId, {
            status: 'error',
            error: error.message,
            statusMessage: 'Pipeline failed.',
            timestamp: new Date().toISOString()
        });
    } finally {
        activeJobs--;
        processNextInQueue();
    }
}

function processNextInQueue() {
    if (jobQueue.length > 0 && activeJobs < MAX_CONCURRENT_JOBS) {
        const nextJob = jobQueue.shift();
        startPipelineJob(nextJob.jobId, nextJob.buffer, nextJob.numMcqs, nextJob.numShorts, nextJob.audioLanguage, nextJob.focusTopic);
    }
}

async function runPipeline(jobId, buffer, numMcqs = 0, numShorts = 0, audioLanguage = 'english', focusTopic = "") {


    const jobDir = path.resolve(`./temp/videos/${jobId}`);
    if (!fs.existsSync(jobDir)) {
        fs.mkdirSync(jobDir, { recursive: true });
    }

    // ── Step 1: Extract text ──────────────────────────────────────────────────
    updateJob(jobId, { statusMessage: 'Extracting document text...' });
    console.log(`[Job ${jobId}] Extracting text...`);
    const text = await extractText(buffer, 8000);

    // ── Step 2: Relevance check ───────────────────────────────────────────────
    updateJob(jobId, { statusMessage: 'Checking content relevance...' });
    console.log(`[Job ${jobId}] Checking relevance...`);
    const isValid = await checkRelevance(text);
    if (!isValid) {
        throw new Error('INVALID: Uploaded file does not appear to contain educational content.');
    }

    // ── Step 3: Generate scene plan ───────────────────────────────────────────
    updateJob(jobId, { statusMessage: 'Generating scene plan with AI...' });
    console.log(`[Job ${jobId}] Generating scenes JSON...`);
    let scenes = [];
    try {
        scenes = await generateScenes(text, audioLanguage, focusTopic);
    } catch (e) {
        throw new Error(`Scene generation failed: ${e.message}`);
    }

    if (!Array.isArray(scenes) || scenes.length === 0) {
        throw new Error('AI returned empty or invalid scene list.');
    }
    scenes = scenes.slice(0, 3);

    // ── Validation: Fix generic narration (Requirement 7) ─────────────────────
    updateJob(jobId, { statusMessage: 'Validating narration quality...' });
    for (let i = 0; i < scenes.length; i++) {
        if (isNarrationGeneric(scenes[i])) {
            console.log(`[Job ${jobId}] Scene${scenes[i].scene_id} narration is generic. Regenerating...`);
            try {
                const fixed = await regenerateNarration(scenes[i], audioLanguage);
                if (fixed && fixed.length > 5) {
                    scenes[i].narration = fixed;
                    console.log(`[Job ${jobId}] Scene${scenes[i].scene_id} narration improved: "${fixed}"`);
                }
            } catch (err) {
                console.warn(`[Job ${jobId}] Failed to regenerate narration for Scene${scenes[i].scene_id}:`, err.message);
            }
        }
    }

    // Initialize progress tracking
    const sceneStatuses = scenes.map(s => ({ scene_id: s.scene_id, status: 'pending' }));
    updateJob(jobId, { sceneStatuses });

    const updateSceneStatus = (sceneId, status) => {
        const scene = sceneStatuses.find(s => s.scene_id === sceneId);
        if (scene) {
            scene.status = status;
            updateJob(jobId, { sceneStatuses });
        }
    };

    // ── Step 4: Render each scene in parallel (skip failures — don't abort) ──────────────
    updateJob(jobId, { statusMessage: 'Processing scenes in parallel...' });

    const sceneResults = await Promise.all(scenes.map(async (scene, idx) => {
        console.log(`[Job ${jobId}] Generating Manim code for Scene${scene.scene_id}...`);

        let code;
        try {
            code = await generateManimCode(scene);
            updateSceneStatus(scene.scene_id, 'code_generated');
        } catch (e) {
            console.error(`[Job ${jobId}] Code generation failed for scene ${scene.scene_id}:`, e.message);
            updateSceneStatus(scene.scene_id, 'failed');
            return { failed: true, scene_id: scene.scene_id };
        }

        updateSceneStatus(scene.scene_id, 'rendering');
        const result = await runManimCodeWithRetry(code, scene, jobId);

        if (result.success) {
            const rawVideoFile = path.join(jobDir, `scene${scene.scene_id}.mp4`);
            if (fs.existsSync(rawVideoFile)) {
                // ── Sync Audio (Narration) ──
                updateSceneStatus(scene.scene_id, 'audio_generating');
                const syncedVideoFile = path.join(jobDir, `scene${scene.scene_id}_synced.mp4`);
                console.log(`[Job ${jobId}] Syncing audio for Scene${scene.scene_id}...`);

                try {
                    const audioResult = await syncAudioWithVideo(rawVideoFile, scene.narration || "", syncedVideoFile, audioLanguage);
                    if (audioResult.success && fs.existsSync(syncedVideoFile)) {
                        updateSceneStatus(scene.scene_id, 'completed');
                        return { success: true, path: syncedVideoFile, scene_id: scene.scene_id };
                    } else {
                        console.warn(`[Job ${jobId}] Audio sync failed for Scene${scene.scene_id}, trying to generate silent video with audio stream.`);
                        const silentResult = await syncAudioWithVideo(rawVideoFile, "", syncedVideoFile, audioLanguage);
                        if (silentResult.success && fs.existsSync(syncedVideoFile)) {
                            updateSceneStatus(scene.scene_id, 'completed');
                            return { success: true, path: syncedVideoFile, scene_id: scene.scene_id };
                        } else {
                            console.error(`[Job ${jobId}] Failed to generate even a silent synced video. Merge may fail.`);
                            updateSceneStatus(scene.scene_id, 'completed');
                            return { success: true, path: rawVideoFile, scene_id: scene.scene_id };
                        }
                    }
                } catch (audioErr) {
                    console.error(`[Job ${jobId}] Audio sync error:`, audioErr.message);
                    updateSceneStatus(scene.scene_id, 'completed');
                    return { success: true, path: rawVideoFile, scene_id: scene.scene_id };
                }
            } else {
                console.warn(`[Job ${jobId}] Scene${scene.scene_id} reported success but no mp4 found.`);
                updateSceneStatus(scene.scene_id, 'failed');
                return { failed: true, scene_id: scene.scene_id };
            }
        } else {
            updateSceneStatus(scene.scene_id, 'failed');
            return { failed: true, scene_id: scene.scene_id };
        }
    }));

    // Promise.all preserves the order of the `scenes` array
    const generatedVideoPaths = sceneResults.filter(r => r.success).map(r => r.path);
    const failedScenes = sceneResults.filter(r => r.failed).map(r => r.scene_id);

    const finalOutputPath = path.join(jobDir, 'final.mp4');

    // ── Step 5: Merge or fallback ─────────────────────────────────────────────
    if (generatedVideoPaths.length > 0) {
        updateJob(jobId, {
            statusMessage: `Merging ${generatedVideoPaths.length} scene(s)...`
        });
        console.log(`[Job ${jobId}] Merging ${generatedVideoPaths.length} video(s)...`);

        if (generatedVideoPaths.length === 1) {
            // Only 1 scene — just copy, no need to concat
            fs.copyFileSync(generatedVideoPaths[0], finalOutputPath);
        } else {
            await mergeVideos(generatedVideoPaths, finalOutputPath);
        }
    } else {
        // Zero scenes rendered — use fallback generator
        console.warn(`[Job ${jobId}] All Manim scenes failed. Generating fallback video...`);
        updateJob(jobId, { statusMessage: 'All scenes failed — generating fallback video...' });
        await generateFallbackVideo(scenes, finalOutputPath);
    }

    if (!fs.existsSync(finalOutputPath)) {
        throw new Error('Final video was not created. Pipeline failed completely.');
    }

    // ── Step 7: Generate Questions (if requested) ───────────────────────────
    let questionsGenerated = false;
    if (numMcqs > 0 || numShorts > 0) {
        try {
            updateJob(jobId, { statusMessage: `Generating questions (${numMcqs} MCQ, ${numShorts} Short)...` });
            console.log(`[Job ${jobId}] Generating questions (${numMcqs} MCQ, ${numShorts} Short)...`);
            const questions = await generateQuestionsFromText(text, numMcqs, numShorts);

            await Question.create({
                jobId,
                questions
            });

            console.log(`[Job ${jobId}] Questions generated successfully. Count: ${questions?.length || 0}`);
            questionsGenerated = true;
        } catch (qErr) {
            console.error(`[Job ${jobId}] Question generation CRITICAL FAILURE:`, qErr);
        }
    }

    // ── Step 8: Final Completion ─────────────────────────────────────────────
    const partial = failedScenes.length > 0 && generatedVideoPaths.length > 0;
    updateJob(jobId, {
        status: 'done',
        videoUrl: `/videos/${jobId}/final.mp4`,
        completedAt: new Date().toISOString(),
        statusMessage: partial
            ? `Done (${generatedVideoPaths.length}/${scenes.length} scenes rendered)`
            : generatedVideoPaths.length === 0
                ? 'Done (fallback video generated)'
                : 'Done — all scenes rendered!',
        scenesRendered: generatedVideoPaths.length,
        scenesTotal: scenes.length,
        questionsGenerated
    });




    console.log(`[Job ${jobId}] Complete → /videos/${jobId}/final.mp4`);
}
