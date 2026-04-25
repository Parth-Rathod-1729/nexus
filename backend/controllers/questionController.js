import Question from '../models/Question.js';
import { generateQuestionsFromText, evaluateShortAnswer } from '../services/questionService.js';
import { extractText } from '../utils/pdfExtractor.js'; // Assuming we might need it if manually triggered
import fs from 'fs';
import path from 'path';

/**
 * Fetches questions for a specific job.
 */
export async function getQuestions(req, res) {
    const { jobId } = req.params;
    try {
        const questionData = await Question.findOne({ jobId });
        if (!questionData) {
            return res.status(404).json({ error: 'Questions not found for this job.' });
        }
        res.json(questionData);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
}

/**
 * Manually trigger question generation (if needed outside pipeline).
 */
export async function generateQuestionsManual(req, res) {
    const { jobId, count } = req.body;
    // In a real app, you'd fetch the text from DB or a stored file.
    // For now, we assume the pipeline already handled it, or we'd need the text.
    // Let's assume we can't easily do it without the text source.
    res.status(501).json({ error: 'Manual generation requires stored document text. Use the pipeline.' });
}

/**
 * Evaluates an answer.
 */
export async function checkAnswer(req, res) {
    const { type, userAnswer, correctAnswer } = req.body;

    if (type === 'mcq') {
        const isCorrect = userAnswer === correctAnswer;
        return res.json({
            correct: isCorrect,
            score: isCorrect ? 100 : 0,
            feedback: isCorrect ? 'Perfect!' : `Incorrect. The correct answer was: ${correctAnswer}`
        });
    }

    if (type === 'short') {
        try {
            const evaluation = await evaluateShortAnswer(userAnswer, correctAnswer);
            res.json(evaluation);
        } catch (err) {
            res.status(500).json({ error: 'Evaluation failed.' });
        }
        return;
    }

    res.status(400).json({ error: 'Invalid question type.' });
}
