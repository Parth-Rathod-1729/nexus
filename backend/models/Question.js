import mongoose from 'mongoose';

const questionSchema = new mongoose.Schema({
  jobId: {
    type: String,
    required: true,
    index: true,
  },
  questions: [
    {
      id: { type: Number, required: true },
      type: { type: String, enum: ['mcq', 'short'], required: true },
      question: { type: String, required: true },
      options: [String], // Only for MCQ
      correct_answer: String, // For MCQ correct option (e.g., "A" or the text)
      answer: String, // For short answer explanation
      hint: String, // Clue that helps guide thinking
    },
  ],
  created_at: {
    type: Date,
    default: Date.now,
  },
});

const Question = mongoose.model('Question', questionSchema);
export default Question;
