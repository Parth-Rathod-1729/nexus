// ─── SDK: @google/genai (v1 endpoint — supports gemini-2.0+ models) ───────────
import { GoogleGenAI } from '@google/genai';

const apiKey = process.env.GEMINI_API_KEY_MANIM_CODE?.trim();
const genAI = new GoogleGenAI({ apiKey });

// Model preference list — tries each in order when service is unavailable
// All names below work on the v1 endpoint used by @google/genai
const MODEL_FALLBACKS = [
    process.env.GEMINI_MODEL || 'gemini-3-flash-preview',
    'gemini-3-flash-preview',
    'gemini-3.1-flash-lite-preview',
    'gemini-2.5-flash',
    'gemini-2.0-flash',
    'gemini-1.5-flash-latest',
];
const uniqueModels = [...new Set(MODEL_FALLBACKS)];

// Boot-time diagnostic
(async function testConnection() {
    const modelName = uniqueModels[0];
    console.log(`[Gemini] Booting with model '${modelName}'...`);
    try {
        await withRetry(async () => {
            const response = await genAI.models.generateContent({
                model: modelName,
                contents: 'ping',
            });
            if (!response?.text) throw new Error('Empty response');
        }, 'Diagnostic', 3);
        console.log(`[Gemini] Model '${modelName}' is online.`);
    } catch (err) {
        console.warn(`[Gemini] Diagnostic warning for '${modelName}': ${err.message?.slice(0, 100)}`);
    }
})();

// ─── Retry helper ─────────────────────────────────────────────────────────────
async function withRetry(fn, taskName = 'Gemini', maxRetries = 6) {
    let lastError;
    for (let i = 0; i < maxRetries; i++) {
        try {
            const result = await fn();
            if (i > 0) console.log(`[${taskName}] Recovered successfully after ${i} retry/ies.`);
            return result;
        } catch (err) {
            lastError = err;
            const msg = (err?.message || '').toLowerCase();
            // Status can be in err.status or err.httpErrorCode or parsed from JSON message
            let status = err?.status || err?.httpErrorCode || 0;
            
            // If message contains a JSON error with "code", try to extract it
            if (status === 0 && msg.includes('"code":')) {
                try {
                    const match = msg.match(/"code":\s*(\d+)/);
                    if (match) status = parseInt(match[1]);
                } catch (e) {}
            }

            const isRateLimit   = status === 429 || msg.includes('429') || msg.includes('resourceexhausted') || msg.includes('quota');
            const isUnavailable = status === 503 || msg.includes('503') || msg.includes('service unavailable') || msg.includes('overloaded');
            const isRetryable   = isRateLimit || isUnavailable;

            if (!isRetryable) throw err; // auth / bad-request / 404 — don't retry here

            const baseDelay = Math.min(4000 * Math.pow(2, i), 60000);
            const jitter    = baseDelay * 0.2 * (Math.random() - 0.5);
            const delay     = Math.round(Math.max(2000, baseDelay + jitter));

            console.warn(`[${taskName}] ${isRateLimit ? '429 Rate limit' : '503 Unavailable'} — retry ${i + 1}/${maxRetries} in ${(delay / 1000).toFixed(1)}s`);
            await new Promise(r => setTimeout(r, delay));
        }
    }
    throw lastError;
}

// ─── Low-level generation call ────────────────────────────────────────────────
async function callModel(modelName, prompt, jsonMode = false) {
    const config = jsonMode
        ? { responseMimeType: 'application/json' }
        : undefined;

    const response = await genAI.models.generateContent({
        model: modelName,
        contents: prompt,
        ...(config ? { config } : {}),
    });

    // @google/genai returns response.text directly as a string
    return response.text ?? '';
}

// ─── Model-fallback wrapper ───────────────────────────────────────────────────
async function tryWithFallback(buildFn, taskName, jsonMode = false) {
    for (const modelName of uniqueModels) {
        try {
            return await withRetry(
                () => buildFn((prompt) => callModel(modelName, prompt, jsonMode)),
                taskName
            );
        } catch (err) {
            const msg    = (err?.message || '').toLowerCase();
            let status = err?.status || err?.httpErrorCode || 0;
            if (status === 0 && msg.includes('"code":')) {
                try {
                    const match = msg.match(/"code":\s*(\d+)/);
                    if (match) status = parseInt(match[1]);
                } catch (e) {}
            }
            // Fall to next model on: 503 overloaded OR 404 deprecated/not-found
            const isCapacity = status === 503 || msg.includes('503') || msg.includes('service unavailable') || msg.includes('overloaded');
            const isNotFound = status === 404 || msg.includes('404') || msg.includes('not found') || msg.includes('not supported for generatecontent');
            const shouldFallback = (isCapacity || isNotFound) && modelName !== uniqueModels[uniqueModels.length - 1];
            if (shouldFallback) {
                console.warn(`[${taskName}] Model '${modelName}' unavailable (${isNotFound ? '404' : '503'}) — trying next fallback.`);
                continue;
            }
            throw err;
        }
    }
}

// ─── Public API ───────────────────────────────────────────────────────────────

export async function checkRelevance(text) {
    return tryWithFallback(async (generate) => {
        const prompt = `Task: Is the following content educational/STEM? Output ONLY valid JSON: {"valid": true} or {"valid": false}.\nContent: ${text.slice(0, 4000)}`;
        const raw  = await generate(prompt);
        const json = JSON.parse(raw.replace(/```json|```/g, '').trim());
        return json.valid === true;
    }, 'Relevance Check', true);
}

export async function generateScenes(text, audioLanguage = 'english') {
    return tryWithFallback(async (generate) => {
        let narrationRule = "narration: 1-2 clear, teacher-like sentences explaining the scene's concept.";
        if (audioLanguage === 'hinglish') {
            narrationRule = "narration: 1-2 clear, teacher-like sentences explaining the scene's concept in Hinglish (Mix of Hindi + English using Roman script ONLY. Example: 'Ab hum dekhte hain ki graph kaise increase ho raha hai').";
        } else if (audioLanguage === 'hindi') {
            narrationRule = "narration: 1-2 clear, teacher-like sentences explaining the scene's concept in pure Hindi (written in Devanagari script).";
        }

        const prompt = `Convert the following text to a JSON array of max 3 educational animation scenes.
Rules:
- scene_id must be an integer (1, 2, 3)
- Keys: scene_id (int), title (string), concept (string), explanation (string), visual_plan (string), narration (string)
- ${narrationRule}
- Output ONLY the JSON array, no markdown.
Text: ${text.slice(0, 6000)}`;
        const raw     = await generate(prompt);
        const cleaned = raw.replace(/```json|```/g, '').trim();
        return JSON.parse(cleaned);
    }, 'Scene Generation', true);
}

export async function generateManimCode(scene) {
    return tryWithFallback(async (generate) => {
        const prompt = `Generate ManimCE Python code for this educational scene.
STRICT RULES:
- Class name MUST be exactly: Scene${scene.scene_id}
- Use ONLY: Text, MathTex, Circle, Square, Arrow, Line, NumberPlane, VGroup, Rectangle, Dot
- FORBIDDEN: SVGMobject, Grid, ImageMobject, any file loading
- FORBIDDEN: self.mobjects or *self.mobjects in animations
- FORBIDDEN: self.wait() calls longer than 3 seconds.
- Use VGroup (not Group) for collections used in Create/Write
- Positioning: use .move_to(), .next_to(), .to_edge() — never let objects overlap
- Colors: use named Manim colors (BLUE, GREEN, TEAL, GOLD, RED, WHITE, YELLOW)
- Use fill_opacity= instead of opacity= for shapes
- KEEP IT CONCISE: The entire scene should be 10-25 seconds long.
- Output ONLY Python code. NO markdown fences.
Scene: ${JSON.stringify(scene)}`;
        const raw = await generate(prompt);
        return raw.replace(/```python|```/g, '').trim();
    }, `Code Gen Scene${scene.scene_id}`);
}

export async function fixManimCode(error, code) {
    return tryWithFallback(async (generate) => {
        const prompt = `Fix this ManimCE Python error. Output ONLY corrected Python code, no markdown.
RULES:
- If "Create only works for VMobjects": replace Group with VGroup
- If "unexpected keyword argument 'opacity'": replace opacity= with fill_opacity=
- If NameError for Grid: use NumberPlane instead
- If FileNotFoundError: remove asset-loading lines
- If AttributeError on self.mobjects: remove that usage entirely
Error: ${String(error).slice(0, 800)}
Code:
${code}`;
        const raw = await generate(prompt);
        return raw.replace(/```python|```/g, '').trim();
    }, 'Code Fix');
}
