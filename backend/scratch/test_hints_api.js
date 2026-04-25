import "dotenv/config";
import { generateQuestionsFromText } from '../services/questionService.js';

async function testHintsAPI() {
    const testText = "The OSI model has seven layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application. The Network layer is responsible for routing packets.";
    console.log("Testing Question + Hint Generation...");
    
    try {
        const questions = await generateQuestionsFromText(testText, 1, 1);
        console.log("API Result:", JSON.stringify(questions, null, 2));
        
        const hasHints = questions.every(q => q.hint && q.hint.length > 0);
        if (hasHints) {
            console.log("\nSUCCESS: All generated questions have hints!");
        } else {
            console.error("\nFAILURE: Some questions are missing hints.");
        }
    } catch (err) {
        console.error("API Test Failed:", err);
    }
}

testHintsAPI();
