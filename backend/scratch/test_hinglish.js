import { generateScenes } from '../services/gemini.js';
import dotenv from 'dotenv';
dotenv.config();

async function test() {
    const text = "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods from carbon dioxide and water. Photosynthesis in plants generally involves the green pigment chlorophyll and generates oxygen as a byproduct.";
    console.log("Generating Hinglish scenes...");
    try {
        const scenes = await generateScenes(text, 'hinglish');
        console.log(JSON.stringify(scenes, null, 2));
    } catch (e) {
        console.error("Error:", e);
    }
}

test();
