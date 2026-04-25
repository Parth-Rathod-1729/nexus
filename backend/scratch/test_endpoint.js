async function testEndpoint() {
    try {
        const res = await fetch('http://localhost:4000/api/questions/check-answer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                type: 'mcq',
                userAnswer: 'A',
                correctAnswer: 'A'
            })
        });
        const data = await res.json();
        console.log("Endpoint Response:", data);
    } catch (err) {
        console.error("Endpoint Test Failed:", err.message);
    }
}

testEndpoint();
