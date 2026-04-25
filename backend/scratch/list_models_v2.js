import dotenv from 'dotenv';
dotenv.config();

async function listModels() {
    const apiKey = process.env.GEMINI_API_KEY_MANIM_CODE;
    const url = `https://generativelanguage.googleapis.com/v1beta/models?key=${apiKey}`;
    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log("Full names of available models:");
        data.models.forEach(model => {
            console.log(`- ${model.name}`);
        });
    } catch (error) {
        console.error("Fetch Error:", error.message);
    }
}

listModels();
