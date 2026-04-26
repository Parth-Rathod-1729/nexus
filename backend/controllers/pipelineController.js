import { v4 as uuidv4 } from 'uuid';
import { startPipelineJob, jobsStore } from '../services/pipelineJob.js';

/**
 * Handles the PDF upload and kicks off the background job.
 */
export async function generatePipeline(req, res) {
    if (!req.file) {
        return res.status(400).json({ error: 'No file uploaded. Please upload a PDF/PPT file.' });
    }

    const buffer = req.file.buffer;
    const jobId = uuidv4();
    const numMcqs = parseInt(req.body.num_mcqs) || 0;
    const numShorts = parseInt(req.body.num_shorts) || 0;
    const audioLanguage = req.body.audio_language || "english";
    const focusTopic = req.body.focus_topic || "";

    // Initialize job in the store
    jobsStore[jobId] = {
        status: "processing",
        numMcqs,
        numShorts,
        audioLanguage,
        focusTopic
    };

    // Kick off pipeline asynchronously (do NOT await)
    startPipelineJob(jobId, buffer, numMcqs, numShorts, audioLanguage, focusTopic).catch((err) => {
        console.error(`Unhandled error inside pipeline for ${jobId}: `, err);
    });



    // Return the jobId immediately 
    return res.status(202).json({
        jobId: jobId,
        status: "processing"
    });
}

/**
 * Returns the status of a given job.
 */
export function getPipelineStatus(req, res) {
    const { jobId } = req.params;
    
    const jobData = jobsStore[jobId];
    if (!jobData) {
        return res.status(404).json({ error: 'Job not found' });
    }

    return res.status(200).json(jobData);
}
