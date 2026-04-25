import dotenv from 'dotenv';
dotenv.config(); // This will look for .env in the current working directory

async function listModels() {
    const apiKey = process.env.GEMINI_API_KEY_MANIM_CODE;
    if (!apiKey) {
        console.error("No API key found in .env. Keys found:", Object.keys(process.env).filter(k => k.includes('GEMINI')));
        return;
    }

    const url = `https://generativelanguage.googleapis.com/v1beta/models?key=${apiKey}`;
    try {
        const response = await fetch(url);
        const data = await response.json();
        
        if (data.error) {
            console.error("API Error:", data.error.message);
            return;
        }

        console.log("\n--- Available Gemini Models ---");
        data.models.forEach(model => {
            const shortName = model.name.replace('models/', '');
            // Only list models that support content generation
            if (model.supportedGenerationMethods.includes('generateContent')) {
                console.log(`- ${shortName}`);
                console.log(`  Display Name: ${model.displayName}`);
                console.log(`  Description: ${model.description}`);
            }
        });
    } catch (error) {
        console.error("Fetch Error:", error.message);
    }
}

listModels();
