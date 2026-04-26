import { spawn } from 'child_process';
import path from 'path';
import fs from 'fs';

// ─── CAMB.AI TTS ──────────────────────────────────────────────────────────────

const CAMB_TTS_URL = 'https://client.camb.ai/apis/tts-stream';
const CAMB_VOICE_ID = 147320;           // Default English natural voice
const CAMB_MODEL    = 'mars-8.1-flash-beta'; // Expressive, teacher-style delivery
const CAMB_LANGUAGE = 'en-us';

/**
 * Generate human-like speech using CAMB.AI TTS API.
 * Saves the audio as an MP3 file at `outputPath`.
 *
 * @param {string} text       – Narration text to convert to speech
 * @param {string} outputPath – Destination file path (*.mp3)
 * @returns {Promise<string>}   The outputPath on success
 */
export async function generateAudio(text, outputPath) {
    const apiKey = process.env.CAMB_API_KEY || process.env.CAMB_AI;
    if (!apiKey) {
        throw new Error('CAMB_API_KEY not set');
    }

    const response = await fetch(CAMB_TTS_URL, {
        method: 'POST',
        headers: {
            'x-api-key': apiKey,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            text,
            voice_id: CAMB_VOICE_ID,
            language: CAMB_LANGUAGE,
            speech_model: CAMB_MODEL,
            output_configuration: { format: 'mp3' },
        }),
    });

    if (!response.ok) {
        const errBody = await response.text();
        throw new Error(`CAMB.AI ${response.status}: ${errBody}`);
    }

    const buffer = Buffer.from(await response.arrayBuffer());
    if (buffer.length < 100) {
        throw new Error('CAMB.AI returned empty or invalid audio data');
    }

    fs.writeFileSync(outputPath, buffer);
    return outputPath;
}

// ─── Audio + Video sync ───────────────────────────────────────────────────────

/**
 * Syncs audio (generated from narration) with a video file.
 * Tries CAMB.AI TTS first; falls back to Python gTTS on failure.
 */
export async function syncAudioWithVideo(videoPath, narration, outputPath, audioLanguage = 'english') {
    let audioArg = narration;

    if (narration && narration.trim().length > 0) {
        try {
            const ttsAudioPath = outputPath.replace('.mp4', '_camb_tts.mp3');
            await generateAudio(narration, ttsAudioPath);
            audioArg = ttsAudioPath; // pass .mp3 path to Python handler
            console.log(`[AudioService] CAMB.AI TTS audio saved → ${ttsAudioPath}`);
        } catch (err) {
            console.warn(`[AudioService] CAMB.AI TTS failed (${err.message}), falling back to gTTS`);
            // audioArg stays as the raw narration string → Python handler will use gTTS
        }
    }

    return new Promise((resolve) => {
        const handlerPath = path.resolve('../python-service/audio_handler.py');
        const processArgs = [handlerPath, videoPath, audioArg, outputPath, audioLanguage];

        const child = spawn('python', processArgs, {
            cwd: path.resolve('../python-service')
        });

        let stdoutData = '';
        let stderrData = '';

        child.stdout.on('data', (data) => { stdoutData += data.toString(); });
        child.stderr.on('data', (data) => { stderrData += data.toString(); });

        // 120s timeout for audio processing
        const timeout = setTimeout(() => {
            child.kill();
            resolve({ success: false, error: 'Audio processing timeout exceeded (120s).' });
        }, 120000);

        child.on('close', (code) => {
            clearTimeout(timeout);

            // Clean up temp CAMB.AI TTS mp3 after Python has consumed it
            if (audioArg.endsWith('.mp3') && fs.existsSync(audioArg)) {
                try { fs.unlinkSync(audioArg); } catch (_) { /* ignore */ }
            }

            try {
                const lines = stdoutData.trim().split('\n');
                const lastLine = lines[lines.length - 1];
                if (!lastLine) {
                    console.error(`[AudioService] No output from audio handler. Stderr: ${stderrData}`);
                    return resolve({ success: false, error: `No output from audio handler. Stderr: ${stderrData}` });
                }
                const result = JSON.parse(lastLine);
                if (!result.success) {
                    console.error(`[AudioService] Python error: ${result.error}`);
                }
                resolve(result);
            } catch (e) {
                console.error(`[AudioService] Parse error: ${e.message}. Stdout: ${stdoutData}`);
                resolve({
                    success: false,
                    error: `Audio JSON Parse error: ${e.message}. Stdout snippet: ${stdoutData.slice(-200)}`
                });
            }
        });
    });
}

