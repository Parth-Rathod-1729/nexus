import { syncAudioWithVideo } from '../services/audioService.js';
import path from 'path';
import fs from 'fs';

async function testSync() {
    const videoPath = path.resolve('temp/videos/c116d554-ec36-4a97-8534-03f8e8461f64/scene1.mp4');
    const narration = "Doston, aaj hum photosynthesis ke baare mein baat karenge. Yeh process plants ke liye bahut important hai.";
    const outputPath = path.resolve('temp/test_hinglish_sync_output.mp4');

    if (!fs.existsSync(videoPath)) {
        console.error("Test video not found at:", videoPath);
        return;
    }

    console.log("Starting Hinglish audio sync test...");
    const result = await syncAudioWithVideo(videoPath, narration, outputPath, 'hinglish');

    if (result.success) {
        console.log("Success! Hinglish output saved to:", outputPath);
    } else {
        console.error("Failed:", result.error);
    }
}

testSync();
