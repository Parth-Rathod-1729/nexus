import { mergeVideos } from '../utils/videoMerger.js';
import path from 'path';
import fs from 'fs';

async function testMerge() {
    const video1 = path.resolve('temp/test_sync_output.mp4');
    const video2 = path.resolve('temp/test_sync_output.mp4'); // Just duplicate for test
    const outputPath = path.resolve('temp/test_merge_output.mp4');

    if (!fs.existsSync(video1)) {
        console.error("Test video not found. Run test_audio_sync.js first.");
        return;
    }

    console.log("Starting merge test...");
    try {
        await mergeVideos([video1, video2], outputPath);
        if (fs.existsSync(outputPath)) {
            console.log("Success! Merged video saved to:", outputPath);
        } else {
            console.error("Failed: Output file not created.");
        }
    } catch (error) {
        console.error("Merge failed:", error.message);
    }
}

testMerge();
