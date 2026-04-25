import ffmpeg from 'fluent-ffmpeg';
import ffmpegInstaller from '@ffmpeg-installer/ffmpeg';
import fs from 'fs';
import path from 'path';

ffmpeg.setFfmpegPath(ffmpegInstaller.path);

/**
 * Generates a fallback MP4 using FFmpeg lavfi (no external assets needed).
 * Creates a black background video with the topic titles as text overlay.
 * @param {Object[]} scenes  - Array of scene objects with .title
 * @param {string}   outputPath - Where to write final.mp4
 */
export async function generateFallbackVideo(scenes, outputPath) {
    return new Promise((resolve, reject) => {
        // Build a text that lists all scene titles
        const topicsText = scenes.map((s, i) => `${i + 1}. ${s.title}`).join('\\n');
        const safeTopics = topicsText
            .replace(/'/g, "\u2019")   // Replace single quotes (breaks drawtext)
            .replace(/:/g, '\\:')       // Escape colons for ffmpeg
            .replace(/\[/g, '\\[')
            .replace(/\]/g, '\\]');

        // We produce a 30-second 1280x720 black video with white text overlay
        const duration = 30;
        const width = 1280;
        const height = 720;

        const filterComplex = [
            // Black background
            `color=c=black:size=${width}x${height}:duration=${duration}:rate=24[bg]`,
            // Title text
            `[bg]drawtext=text='Educational Video':fontsize=52:fontcolor=white:` +
            `x=(w-text_w)/2:y=h/5:enable='between(t,0,${duration})'[titled]`,
            // Topics text
            `[titled]drawtext=text='${safeTopics}':fontsize=30:fontcolor=#aaaaff:` +
            `x=(w-text_w)/2:y=h/2:line_spacing=10:enable='between(t,0,${duration})'[final]`
        ].join(';');

        ffmpeg()
            .input('anullsrc=channel_layout=stereo:sample_rate=44100')
            .inputOptions(['-f', 'lavfi'])
            .complexFilter(filterComplex, 'final')
            .outputOptions([
                '-t', String(duration),
                '-c:v', 'libx264',
                '-preset', 'ultrafast',
                '-pix_fmt', 'yuv420p',
                '-an'    // no audio stream (avoid sync issues)
            ])
            .output(outputPath)
            .on('start', (cmd) => console.log('[Fallback] FFmpeg cmd:', cmd))
            .on('end', () => {
                console.log('[Fallback] Fallback video created at', outputPath);
                resolve();
            })
            .on('error', (err) => {
                console.error('[Fallback] FFmpeg error:', err.message);
                // Last resort: write a minimal valid MP4 via a 1-second color clip
                generateMinimalFallback(outputPath).then(resolve).catch(reject);
            })
            .run();
    });
}

/**
 * Absolute last-resort: 1-second solid-colour MP4 (always works).
 */
function generateMinimalFallback(outputPath) {
    return new Promise((resolve, reject) => {
        ffmpeg()
            .input('color=c=black:size=1280x720:duration=5:rate=24')
            .inputOptions(['-f', 'lavfi'])
            .outputOptions(['-c:v', 'libx264', '-preset', 'ultrafast', '-pix_fmt', 'yuv420p', '-an'])
            .output(outputPath)
            .on('end', resolve)
            .on('error', reject)
            .run();
    });
}
