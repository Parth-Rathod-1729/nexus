import mongoose from 'mongoose';
import dotenv from 'dotenv';
dotenv.config();

const QuestionSchema = new mongoose.Schema({
    jobId: String,
    questions: Array
});

const Question = mongoose.model('Question', QuestionSchema);

async function injectHints() {
    await mongoose.connect(process.env.MONGO_DB_LINK);
    const lastJob = await Question.findOne().sort({ _id: -1 });
    if (lastJob) {
        console.log("Found job:", lastJob.jobId);
        lastJob.questions = lastJob.questions.map(q => ({
            ...q,
            hint: q.hint || "This is a manually injected test hint to verify the UI!"
        }));
        await lastJob.save();
        console.log("Hints injected successfully.");
    } else {
        console.log("No jobs found.");
    }
    await mongoose.disconnect();
}

injectHints();
