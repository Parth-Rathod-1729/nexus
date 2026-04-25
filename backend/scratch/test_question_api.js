import "dotenv/config";
import { GoogleGenAI } from '@google/genai';

async function test() {
    const apiKey = process.env.GEMINI_API_KEY_QUESTION_GENERATOR?.trim();
    console.log("Testing API Key:", apiKey ? "Present" : "Missing");
    if (!apiKey) return;

    const genAI = new GoogleGenAI({ apiKey });
    try {
        const response = await genAI.models.generateContent({
            model: 'gemini-3-flash-preview',
            contents: 'Say "API Key is working"',
        });

        console.log("Gemini Response:", response.text);
    } catch (err) {
        console.error("Gemini Test Failed:", err.message);
    }
}

test();
