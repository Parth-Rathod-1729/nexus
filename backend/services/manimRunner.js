import { spawn } from 'child_process';
import path from 'path';
import { fixManimCode } from './gemini.js';
import fs from 'fs';

/**
 * Runs the Manim python runner with a timeout limit.
 */
function execPythonRunner(pyFilePath, sceneName, jobId) {
    return new Promise((resolve) => {
        const runnerPath = path.resolve('../python-service/runner.py');
        const processArgs = [runnerPath, pyFilePath, sceneName, jobId];

        const child = spawn('python', processArgs, {
            cwd: path.resolve('../python-service')
        });

        let stdoutData = '';
        let stderrData = '';

        child.stdout.on('data', (data) => { stdoutData += data.toString(); });
        child.stderr.on('data', (data) => { stderrData += data.toString(); });

        // 300s timeout
        const timeout = setTimeout(() => {
            child.kill();
            resolve({ success: false, error: 'Execution timeout exceeded (300s).' });
        }, 300000);

        child.on('close', () => {
            clearTimeout(timeout);
            try {
                const lines = stdoutData.trim().split('\n');
                const lastLine = lines[lines.length - 1];
                const result = JSON.parse(lastLine);
                resolve(result);
            } catch (e) {
                resolve({
                    success: false,
                    error: `JSON Parse error. Stdout: ${stdoutData.slice(-500)}. Stderr: ${stderrData.slice(-500)}`
                });
            }
        });
    });
}

/**
 * Executes a scene with up to 3 Gemini auto-fix retries.
 * Returns { success: boolean, error?: string } — never throws.
 */
export async function runManimCodeWithRetry(code, scene, jobId) {
    const sceneName = `Scene${scene.scene_id}`;
    let currentCode = code;

    const pyDir = path.resolve(`./temp/videos/${jobId}`);
    if (!fs.existsSync(pyDir)) {
        fs.mkdirSync(pyDir, { recursive: true });
    }

    const pyFilePath = path.join(pyDir, `scene${scene.scene_id}_code.py`);

    for (let i = 0; i < 3; i++) {
        fs.writeFileSync(pyFilePath, currentCode);

        console.log(`[Job ${jobId}] Running manim for ${sceneName} (Attempt ${i + 1}/3)`);
        const result = await execPythonRunner(pyFilePath, sceneName, jobId);

        if (result.success) {
            console.log(`[Job ${jobId}] ${sceneName} rendered successfully.`);
            return { success: true };
        }

        console.error(`[Job ${jobId}] ${sceneName} failed (attempt ${i + 1}):`, result.error?.slice(0, 300));

        if (i < 2) {
            console.log(`[Job ${jobId}] Auto-fixing ${sceneName} via Gemini...`);
            try {
                currentCode = await fixManimCode(result.error, currentCode);
            } catch (fixErr) {
                console.error(`[Job ${jobId}] Gemini fix failed: ${fixErr.message}`);
            }
        }
    }

    console.error(`[Job ${jobId}] ${sceneName} failed all 3 attempts — skipping.`);
    return { success: false, error: `${sceneName} failed after 3 attempts.` };
}
