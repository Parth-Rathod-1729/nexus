import dotenv from 'dotenv';
import { GoogleGenAI } from '@google/genai';
dotenv.config();

const apiKey = process.env.GEMINI_API_KEY_MANIM_CODE?.trim();
const genAI = new GoogleGenAI({ apiKey });

const modelsToTest = [
    'gemini-3.1-flash-preview',
    'gemini-3-flash-preview',
    'gemini-2.5-flash',
    'gemini-2.0-flash'
];

async function testModels() {
    console.log(`Testing with key: ...${apiKey?.slice(-5)}`);
    for (const modelName of modelsToTest) {
        console.log(`\n--- Testing Model: ${modelName} ---`);
        try {
            const response = await genAI.models.generateContent({
                model: modelName,
                contents: "Say 'ready'",
            });
            console.log(`Success: ${response.text.trim()}`);
        } catch (err) {
            console.error(`Failed: ${err.message}`);
        }
    }
}

testModels();
