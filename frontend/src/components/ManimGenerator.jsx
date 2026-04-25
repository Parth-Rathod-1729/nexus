import React, { useState, useEffect } from 'react';

const API_BASE = 'http://localhost:4000/api'; // Or your backend URL

export default function ManimGenerator() {
  const [numMcqs, setNumMcqs] = useState(2);
  const [numShorts, setNumShorts] = useState(1);
  const [questions, setQuestions] = useState([]);
  const [userAnswers, setUserAnswers] = useState({}); // { qId: { result: null, score: null, feedback: null } }
    const [file, setFile] = useState(null);
  const [jobId, setJobId] = useState(null);
  const [status, setStatus] = useState(''); // 'processing', 'done', 'error'
  const [videoUrl, setVideoUrl] = useState('');
  const [showModal, setShowModal] = useState(false);
  const [errorMsg, setErrorMsg] = useState('');
  // Handle file select
  const handleFileChange = (e) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
      setShowModal(true); // Open modal when file is selected
    }
  };

  // Upload to generate pipeline
  const handleUpload = async () => {
    if (!file) return;
    setShowModal(false); // Close modal before starting

    // Reset state
    setJobId(null);
    setStatus('processing');
    setVideoUrl('');
    setErrorMsg('');
    setQuestions([]);
    setUserAnswers({});

    const formData = new FormData();
    formData.append('document', file);
    formData.append('num_mcqs', numMcqs);
    formData.append('num_shorts', numShorts);

    try {
      const response = await fetch(`${API_BASE}/pipeline/generate`, {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.error || 'Failed to start job');
      }

      setJobId(data.jobId);
    } catch (err) {
      setStatus('error');
      setErrorMsg(err.message);
    }
  };

  const fetchQuestions = async (id) => {
    try {
      const res = await fetch(`${API_BASE}/questions/${id}`);
      if (res.ok) {
        const data = await res.json();
        setQuestions(data.questions || []);
      }
    } catch (err) {
      console.error("Failed to fetch questions:", err);
    }
  };

  // Polling logic
  useEffect(() => {
    let interval;
    if (jobId && status === 'processing') {
      interval = setInterval(async () => {
        try {
          const res = await fetch(`${API_BASE}/pipeline/status/${jobId}`);
          const data = await res.json();

          if (data.status === 'done') {
            setStatus('done');
            setVideoUrl(`http://localhost:4000${data.videoUrl}`);
            
            // If questions were generated, fetch them
            if (data.questionsGenerated) {
              fetchQuestions(jobId);
            }
          } else if (data.status === 'error') {
            setStatus('error');
            setErrorMsg(data.error || 'An unknown error occurred during generation.');
          }
        } catch (err) {
          console.error("Polling error:", err);
        }
      }, 3000);
    }

    return () => clearInterval(interval);
  }, [jobId, status]);

  const handleMcqClick = async (q, option) => {
    const res = await fetch(`${API_BASE}/questions/check-answer`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        type: 'mcq',
        userAnswer: option,
        correctAnswer: q.correct_answer
      })
    });
    const result = await res.json();
    setUserAnswers(prev => ({
      ...prev,
      [q.id]: { selected: option, ...result }
    }));
  };

  const handleShortSubmit = async (q, answer) => {
    const res = await fetch(`${API_BASE}/questions/check-answer`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        type: 'short',
        userAnswer: answer,
        correctAnswer: q.answer
      })
    });
    const result = await res.json();
    setUserAnswers(prev => ({
      ...prev,
      [q.id]: { submitted: answer, ...result }
    }));
  };

  const toggleShowAnswer = (qId) => {
    setUserAnswers(prev => ({
      ...prev,
      [qId]: { ...prev[qId], showAnswer: !prev[qId]?.showAnswer }
    }));
  };

  return (
    <div style={{ padding: '2rem', maxWidth: '800px', margin: '0 auto', fontFamily: 'sans-serif', backgroundColor: '#f9f9f9', borderRadius: '12px' }}>
      <h1 style={{ textAlign: 'center', color: '#333' }}>Nexus AI Video Generator</h1>
      
      <div style={{ backgroundColor: 'white', padding: '1.5rem', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.05)' }}>
        <div style={{ marginBottom: '1rem' }}>
          <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 'bold' }}>Upload PDF/PPT</label>
          <input type="file" accept=".pdf,.ppt,.pptx" onChange={handleFileChange} />
        </div>

        {file && !jobId && status !== 'processing' && (
          <p style={{ fontSize: '0.8rem', color: '#666' }}>Selected: {file.name}</p>
        )}
      </div>

      {showModal && (
        <div style={{
          position: 'fixed', top: 0, left: 0, width: '100%', height: '100%',
          backgroundColor: 'rgba(0,0,0,0.5)', display: 'flex', justifyContent: 'center', alignItems: 'center',
          zIndex: 1000
        }}>
          <div style={{
            backgroundColor: 'white', padding: '2rem', borderRadius: '12px', width: '350px',
            boxShadow: '0 10px 25px rgba(0,0,0,0.2)', textAlign: 'center'
          }}>
            <h3 style={{ marginTop: 0 }}>Question Preferences</h3>
            <p style={{ fontSize: '0.9rem', color: '#666' }}>How many questions should we generate for "{file?.name}"?</p>
            
            <div style={{ display: 'flex', justifyContent: 'space-around', margin: '1.5rem 0' }}>
              <div>
                <label style={{ display: 'block', marginBottom: '0.3rem' }}>MCQs</label>
                <input 
                  type="number" min="0" max="10" value={numMcqs} 
                  onChange={e => setNumMcqs(e.target.value)} 
                  style={{ width: '60px', padding: '0.4rem', textAlign: 'center' }} 
                />
              </div>
              <div>
                <label style={{ display: 'block', marginBottom: '0.3rem' }}>Short Ans</label>
                <input 
                  type="number" min="0" max="10" value={numShorts} 
                  onChange={e => setNumShorts(e.target.value)} 
                  style={{ width: '60px', padding: '0.4rem', textAlign: 'center' }} 
                />
              </div>
            </div>

            <div style={{ display: 'flex', gap: '1rem' }}>
              <button 
                onClick={() => setShowModal(false)}
                style={{ flex: 1, padding: '0.6rem', border: '1px solid #ccc', borderRadius: '4px', cursor: 'pointer' }}
              >
                Cancel
              </button>
              <button 
                onClick={handleUpload}
                style={{ flex: 1, padding: '0.6rem', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
              >
                Start Pipeline
              </button>
            </div>
          </div>
        </div>
      )}


      {status === 'processing' && jobId && (
        <div style={{ margin: '2rem 0', textAlign: 'center', color: '#666' }}>
          <div className="spinner" style={{ marginBottom: '1rem' }}>⚙️</div>
          Pipeline is processing (Job ID: {jobId})...
        </div>
      )}

      {status === 'error' && (
        <div style={{ margin: '2rem 0', padding: '1rem', backgroundColor: '#fff5f5', color: '#c53030', borderRadius: '4px', border: '1px solid #feb2b2' }}>
          <strong>Error:</strong> {errorMsg}
        </div>
      )}

      {status === 'done' && videoUrl && (
        <div style={{ marginTop: '2rem' }}>
          <h2 style={{ color: '#333' }}>1. Watch Video</h2>
          <video 
            controls 
            src={videoUrl} 
            style={{ width: '100%', borderRadius: '8px', boxShadow: '0 4px 12px rgba(0,0,0,0.15)' }}
          >
            Your browser does not support HTML5 video.
          </video>

          {questions.length > 0 && (
            <div style={{ marginTop: '3rem' }}>
              <h2 style={{ color: '#333' }}>2. Test Your Knowledge</h2>
              {questions.map((q, idx) => (
                <div key={q.id} style={{ backgroundColor: 'white', padding: '1.5rem', borderRadius: '8px', marginBottom: '1.5rem', boxShadow: '0 2px 4px rgba(0,0,0,0.05)' }}>
                  <p style={{ fontWeight: 'bold', fontSize: '1.1rem' }}>Q{idx+1}: {q.question}</p>
                  
                  {q.type === 'mcq' ? (
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.5rem', marginTop: '1rem' }}>
                      {q.options.map(opt => {
                        const isSelected = userAnswers[q.id]?.selected === opt;
                        const isCorrect = userAnswers[q.id]?.correct && isSelected;
                        const isWrong = userAnswers[q.id]?.correct === false && isSelected;

                        return (
                          <button
                            key={opt}
                            onClick={() => handleMcqClick(q, opt)}
                            style={{
                              padding: '0.5rem',
                              textAlign: 'left',
                              borderRadius: '4px',
                              border: '1px solid #ddd',
                              backgroundColor: isCorrect ? '#c6f6d5' : isWrong ? '#fed7d7' : 'white',
                              cursor: 'pointer'
                            }}
                          >
                            {opt}
                          </button>
                        );
                      })}
                    </div>
                  ) : (
                    <div style={{ marginTop: '1rem' }}>
                      <textarea 
                        placeholder="Type your answer here..."
                        style={{ width: '100%', padding: '0.5rem', borderRadius: '4px', border: '1px solid #ddd', minHeight: '80px' }}
                        onBlur={(e) => handleShortSubmit(q, e.target.value)}
                      />
                      {userAnswers[q.id]?.score !== undefined && (
                        <div style={{ marginTop: '0.5rem', padding: '0.5rem', backgroundColor: '#f0f4f8', borderRadius: '4px' }}>
                          <p><strong>Score:</strong> {userAnswers[q.id].score}%</p>
                          <p><strong>Feedback:</strong> {userAnswers[q.id].feedback}</p>
                        </div>
                      )}
                    </div>
                  )}

                  <div style={{ marginTop: '1rem' }}>
                    <button 
                      onClick={() => toggleShowAnswer(q.id)}
                      style={{ fontSize: '0.8rem', color: '#007bff', background: 'none', border: 'none', cursor: 'pointer', textDecoration: 'underline' }}
                    >
                      {userAnswers[q.id]?.showAnswer ? 'Hide Answer' : 'Show Answer'}
                    </button>
                    {userAnswers[q.id]?.showAnswer && (
                      <div style={{ marginTop: '0.5rem', padding: '0.5rem', backgroundColor: '#fff9db', borderRadius: '4px', borderLeft: '4px solid #fcc419' }}>
                        <strong>Correct Answer:</strong> {q.type === 'mcq' ? q.correct_answer : q.answer}
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );

}
