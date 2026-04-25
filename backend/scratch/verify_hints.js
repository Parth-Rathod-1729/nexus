import 'dotenv/config';
import mongoose from 'mongoose';
import Question from '../models/Question.js';

async function runTest() {
    try {
        console.log('Connecting to DB...');
        await mongoose.connect(process.env.MONGO_DB_LINK);
        console.log('Connected.');

        const testJobId = 'test-job-' + Date.now();
        const testQuestions = [
            {
                id: 1,
                type: 'mcq',
                question: 'What is 2+2?',
                options: ['3', '4', '5'],
                correct_answer: '4',
                hint: 'It is the square of 2.'
            },
            {
                id: 2,
                type: 'short',
                question: 'Define gravity.',
                answer: 'A force that pulls objects toward each other.',
                hint: 'Think about falling apples.'
            }
        ];

        console.log('Saving test questions with hints...');
        await Question.create({
            jobId: testJobId,
            questions: testQuestions
        });

        console.log('Retrieving questions from DB...');
        const saved = await Question.findOne({ jobId: testJobId });

        if (!saved) {
            console.error('FAILED: Questions not found in DB.');
            process.exit(1);
        }

        console.log('Verifying hints...');
        saved.questions.forEach((q, idx) => {
            if (q.hint === testQuestions[idx].hint) {
                console.log(`SUCCESS: Question ${idx + 1} has correct hint: "${q.hint}"`);
            } else {
                console.error(`FAILED: Question ${idx + 1} hint mismatch! Expected "${testQuestions[idx].hint}", got "${q.hint}"`);
            }
        });

        // Cleanup
        await Question.deleteOne({ jobId: testJobId });
        console.log('Cleanup complete.');
        
        process.exit(0);
    } catch (err) {
        console.error('ERROR during verification:', err);
        process.exit(1);
    }
}

runTest();
