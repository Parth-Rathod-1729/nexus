import 'dotenv/config';
import { generateQuestionsFromText } from '../services/questionService.js';

async function testHints() {
    const text = "A switch is a networking device that connects devices on a computer network by using packet switching to receive and forward data to the destination device. Unlike a hub, which broadcasts the same data to all its ports, a switch forwards data only to the specific device that needs it. This reduces network congestion and improves performance. Switches operate at the Data Link Layer (Layer 2) of the OSI model.";
    
    try {
        console.log("Generating questions...");
        const questions = await generateQuestionsFromText(text, 1, 1);
        console.log("Questions generated:");
        console.log(JSON.stringify(questions, null, 2));
        
        const missingHints = questions.filter(q => !q.hint);
        if (missingHints.length > 0) {
            console.error("FAILED: Some questions are missing hints!");
        } else {
            console.log("SUCCESS: All questions have hints.");
        }
    } catch (err) {
        console.error("Error:", err);
    }
}

testHints();
