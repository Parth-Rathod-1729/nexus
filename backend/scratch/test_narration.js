import { isNarrationGeneric } from '../services/gemini.js';

const testCases = [
    {
        name: "Generic Definition",
        scene: { narration: "A triangle is a polygon with three edges and three vertices." },
        expected: true
    },
    {
        name: "Visual Linked",
        scene: { narration: "In this scene, we see a blue triangle appearing on the left side of the screen." },
        expected: false
    },
    {
        name: "Empty",
        scene: { narration: "" },
        expected: true
    },
    {
        name: "Too Short",
        scene: { narration: "Hi." },
        expected: true
    },
    {
        name: "Visual Marker - Represents",
        scene: { narration: "This circle represents the starting point of our journey." },
        expected: false
    }
];

console.log("Testing isNarrationGeneric...");
testCases.forEach(tc => {
    const result = isNarrationGeneric(tc.scene);
    console.log(`[${tc.name}] Result: ${result === tc.expected ? 'PASS' : 'FAIL'} (Got: ${result})`);
});
