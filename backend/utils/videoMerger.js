import ffmpeg from 'fluent-ffmpeg';
import ffmpegInstaller from '@ffmpeg-installer/ffmpeg';
import fs from 'fs';
import path from 'path';

// Configure fluent-ffmpeg to use the static binary
ffmpeg.setFfmpegPath(ffmpegInstaller.path);

/**
 * Merges a list of video files sequentially with re-encoding.
 * @param {string[]} videoFiles - Array of paths to video files to merge
 * @param {string} outputPath - Path pointing to the final final.mp4
 * @returns {Promise<void>}
 */
export async function mergeVideos(videoFiles, outputPath) {
    return new Promise((resolve, reject) => {
        if (!videoFiles || videoFiles.length === 0) {
            return reject(new Error('No videos to merge.'));
        }

        // Sort files numerically
        const sortedFiles = [...videoFiles].sort((a, b) => {
            const numA = parseInt(path.basename(a).replace(/[^0-9]/g, '')) || 0;
            const numB = parseInt(path.basename(b).replace(/[^0-9]/g, '')) || 0;
            return numA - numB;
        });

        console.log(`[Merger] Merging ${sortedFiles.length} files with re-encoding...`);

        const command = ffmpeg();

        // Add inputs
        sortedFiles.forEach(file => {
            command.input(file);
        });

        // Use concat filter for re-encoding. 
        // This requires ALL inputs to have BOTH a video and audio stream.
        // pipelineJob.js ensures this by falling back to silent audio if needed.
        let filterStr = "";
        sortedFiles.forEach((_, i) => {
            filterStr += `[${i}:v][${i}:a]`;
        });
        filterStr += `concat=n=${sortedFiles.length}:v=1:a=1[vmerged][amerged]`;

        command
            .complexFilter(filterStr)
            .map('[vmerged]')
            .map('[amerged]')
            .outputOptions([
                '-c:v libx264',
                '-preset ultrafast',
                '-crf 23',
                '-c:a aac',
                '-b:a 128k',
                '-movflags +faststart'
            ])
            .on('start', (cmd) => console.log(`[Merger] FFmpeg command: ${cmd}`))
            .on('end', () => {
                console.log('[Merger] Merge complete.');
                resolve();
            })
            .on('error', (err) => {
                console.error(`[Merger] FFmpeg error: ${err.message}`);
                reject(new Error(`FFmpeg merge error: ${err.message}`));
            })
            .save(outputPath);
    });
}
