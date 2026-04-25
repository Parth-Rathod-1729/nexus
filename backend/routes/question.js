import express from 'express';
import { getQuestions, checkAnswer, generateQuestionsManual } from '../controllers/questionController.js';

const router = express.Router();

router.get('/:jobId', getQuestions);
router.post('/check-answer', checkAnswer);
router.post('/generate-questions', generateQuestionsManual);

export default router;
