import { spawn } from 'child_process';
import path from 'path';

/**
 * Syncs audio (generated from narration) with a video file.
 */
export async function syncAudioWithVideo(videoPath, narration, outputPath, audioLanguage = 'english') {
    return new Promise((resolve) => {
        const handlerPath = path.resolve('../python-service/audio_handler.py');
        const processArgs = [handlerPath, videoPath, narration, outputPath, audioLanguage];

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
