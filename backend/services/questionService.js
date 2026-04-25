import { GoogleGenAI } from '@google/genai';

const apiKey = process.env.GEMINI_API_KEY_QUESTION_GENERATOR?.trim();
const genAI = new GoogleGenAI({ apiKey });
const modelName = process.env.GEMINI_MODEL || 'gemini-3-flash-preview';

/**
 * Generates questions based on educational text.
 */
export async function generateQuestionsFromText(text, numMcqs, numShorts) {
    const prompt = `
Task: Generate ${numMcqs} Multiple Choice Questions (mcq) and ${numShorts} Short Answer Questions (short) based on the text below.
Rules:
1. Total questions must be exactly ${numMcqs + numShorts}.
2. For MCQ: Provide 4 options and the correct_answer.
3. For Short: Provide the question and a clear, concise reference answer.
4. HINT: Every question must include a "hint" field (1-2 lines) that guides the user without revealing the answer.
5. Output MUST be a strictly valid JSON object with the key "questions".

Use this exact JSON structure:
{
  "questions": [
    {
      "id": 1,
      "type": "mcq",
      "question": "What is ...?",
      "options": ["A", "B", "C", "D"],
      "correct_answer": "B",
      "hint": "Clue that helps guide thinking..."
    },
    {
      "id": 2,
      "type": "short",
      "question": "Explain ...",
      "answer": "Correct explanation here",
      "hint": "Focus on the definition..."
    }
  ]
}


Text: ${text.slice(0, 10000)}
`;

    console.log(`[questionService] Calling Gemini with ${numMcqs} MCQs and ${numShorts} Short Ans...`);
    
    let response;
    let attempts = 0;
    const maxAttempts = 3;
    let delay = 2000;

    while (attempts < maxAttempts) {
        try {
            response = await genAI.models.generateContent({
                model: modelName,
                contents: prompt,
            });
            if (response && response.text) break;
            throw new Error("Empty response from Gemini");
        } catch (err) {
            attempts++;
            const is503 = err.message?.includes('503') || err.status === 503 || err.message?.includes('UNAVAILABLE');
            
            if (is503 && attempts < maxAttempts) {
                console.warn(`[questionService] Gemini 503 (Attempt ${attempts}/${maxAttempts}). Retrying in ${delay}ms...`);
                await new Promise(resolve => setTimeout(resolve, delay));
                delay *= 2;
                continue;
            }
            throw err;
        }
    }

    if (!response || !response.text) {
        console.error(`[questionService] Gemini returned empty response!`, response);
        throw new Error("Gemini returned an empty response for questions.");
    }


    console.log(`[questionService] Gemini responded. Raw text length: ${response.text.length}`);
    const raw = response.text;
    const cleaned = raw.replace(/```json|```/g, '').trim();
    
    try {
        const parsed = JSON.parse(cleaned);
        return parsed.questions || [];
    } catch (parseErr) {
        console.error(`[questionService] JSON Parse Error. Raw: ${raw}`);
        throw parseErr;
    }

}

/**
 * Evaluates a user's short answer against the correct answer.
 */
export async function evaluateShortAnswer(userAnswer, correctAnswer) {
    const prompt = `
Task: Evaluate the similarity between a student's answer and the correct answer.
Student's Answer: "${userAnswer}"
Correct Answer: "${correctAnswer}"

Output ONLY a JSON object in this format:
{
  "correct": true/false,
  "score": 0-100,
  "feedback": "brief explanation of what was missed or why it is correct"
}
`;

    const response = await genAI.models.generateContent({
        model: modelName,
        contents: prompt,
    });

    const raw = response.text || '';
    const cleaned = raw.replace(/```json|```/g, '').trim();
    return JSON.parse(cleaned);
}

