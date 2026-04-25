import React, { useRef, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Play, Pause, Maximize, Download, Film, Layers, CheckCircle, AlertCircle, HelpCircle, ChevronDown, ChevronUp, Activity, Lightbulb } from 'lucide-react';
import { useVideo } from '../App';

const BACKEND = () => {
  const raw = import.meta.env.VITE_BACKEND_SERVER || 'http://localhost:4000';
  return raw.endsWith('/') ? raw.slice(0, -1) : raw;
};


const VideoPreview = () => {
  const { videoData } = useVideo();
  const videoRef = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [progress, setProgress] = useState(0);
  const [duration, setDuration] = useState(0);

  // Quiz state
  const [questions, setQuestions] = useState([]);
  const [userAnswers, setUserAnswers] = useState({}); // { qId: { result: null, score: null, feedback: null, showAnswer: false } }
  const [isFetchingQuestions, setIsFetchingQuestions] = useState(false);


  const togglePlay = () => {
    if (!videoRef.current) return;
    if (isPlaying) {
      videoRef.current.pause();
    } else {
      videoRef.current.play();
    }
    setIsPlaying(!isPlaying);
  };

  const handleTimeUpdate = () => {
    if (!videoRef.current) return;
    const pct = (videoRef.current.currentTime / videoRef.current.duration) * 100;
    setProgress(isNaN(pct) ? 0 : pct);
  };

  const handleLoadedMetadata = () => {
    if (videoRef.current) setDuration(videoRef.current.duration);
  };

  const handleSeek = (e) => {
    if (!videoRef.current) return;
    const rect = e.currentTarget.getBoundingClientRect();
    const pct = (e.clientX - rect.left) / rect.width;
    videoRef.current.currentTime = pct * videoRef.current.duration;
  };

  const handleFullscreen = () => {
    videoRef.current?.requestFullscreen?.();
  };

  // ── Quiz Logic ────────────────────────────────────────────────────────────
  React.useEffect(() => {
    if (videoData?.jobId) {
      fetchQuestions(videoData.jobId);
    }
  }, [videoData?.jobId]);

  const fetchQuestions = async (id) => {
    setIsFetchingQuestions(true);
    try {
      const res = await fetch(`${BACKEND()}/api/questions/${id}`);
      if (res.ok) {
        const data = await res.json();
        setQuestions(data.questions || []);
      }
    } catch (err) {
      console.error("Failed to fetch questions:", err);
    } finally {
      setIsFetchingQuestions(false);
    }
  };

  const handleMcqClick = async (q, option) => {
    try {
      const res = await fetch(`${BACKEND()}/api/questions/check-answer`, {
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
    } catch (err) {
      console.error("MCQ check failed:", err);
    }
  };

  const handleShortSubmit = async (q, answer) => {
    if (!answer.trim()) return;
    setUserAnswers(prev => ({
      ...prev,
      [q.id]: { ...prev[q.id], submitting: true }
    }));

    try {
      const res = await fetch(`${BACKEND()}/api/questions/check-answer`, {
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
        [q.id]: { submitted: answer, ...result, submitting: false }
      }));
    } catch (err) {
      console.error("Short answer check failed:", err);
      setUserAnswers(prev => ({
        ...prev,
        [q.id]: { ...prev[q.id], submitting: false }
      }));
    }
  };


  const toggleShowHint = (qId) => {
    setUserAnswers(prev => ({
      ...prev,
      [qId]: { ...prev[qId], showHint: !prev[qId]?.showHint }
    }));
  };

  const toggleShowAnswer = (qId) => {

    setUserAnswers(prev => ({
      ...prev,
      [qId]: { 
        ...prev[qId], 
        showAnswer: !prev[qId]?.showAnswer,
        everRevealed: true // Mark that they've seen it at least once
      }
    }));
  };



  const fmtTime = (s) => {
    if (!s || isNaN(s)) return '0:00';
    const m = Math.floor(s / 60);
    const sec = Math.floor(s % 60).toString().padStart(2, '0');
    return `${m}:${sec}`;
  };

  return (
    <section id="video-preview-section">
      <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
        <h2 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>
          Final <span style={{ color: 'var(--neon-cyan)' }}>Render</span>
        </h2>
        <p style={{ color: 'var(--text-muted)' }}>
          {videoData
            ? 'Your AI-generated educational video is ready.'
            : 'The fully synthesized educational video ready for deployment.'}
        </p>
      </div>

      <div style={{ maxWidth: '1000px', margin: '0 auto' }}>
        <AnimatePresence mode="wait">

          {/* ── Real Video Player ─────────────────────────────────────────── */}
          {videoData ? (
            <motion.div
              key="real-player"
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.6 }}
              className="glass-panel"
              style={{
                padding: 0, overflow: 'hidden',
                boxShadow: '0 0 60px rgba(0, 255, 204, 0.15), 0 20px 50px rgba(0,0,0,0.5)',
                border: '1px solid rgba(0,255,204,0.3)'
              }}
            >
              {/* Status badge */}
              <div style={{
                display: 'flex', justifyContent: 'space-between', alignItems: 'center',
                padding: '12px 20px',
                background: 'rgba(0,255,204,0.05)',
                borderBottom: '1px solid rgba(0,255,204,0.1)'
              }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <motion.div
                    animate={{ scale: [1, 1.3, 1], opacity: [0.7, 1, 0.7] }}
                    transition={{ duration: 2, repeat: Infinity }}
                    style={{ width: '10px', height: '10px', borderRadius: '50%', background: '#00ffcc', boxShadow: '0 0 8px #00ffcc' }}
                  />
                  <span style={{ color: '#00ffcc', fontSize: '0.85rem', fontWeight: 600 }}>
                    {videoData.statusMessage || 'Video Ready'}
                  </span>
                </div>
                {videoData.scenesRendered !== undefined && (
                  <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <Layers size={14} color="var(--text-muted)" />
                    <span style={{ color: 'var(--text-muted)', fontSize: '0.8rem' }}>
                      {videoData.scenesRendered}/{videoData.scenesTotal} scenes rendered
                    </span>
                  </div>
                )}
              </div>

              {/* Video element */}
              <div style={{
                width: '100%', aspectRatio: '16/9',
                background: '#000', position: 'relative',
                display: 'flex', alignItems: 'center', justifyContent: 'center'
              }}>
                <video
                  ref={videoRef}
                  src={videoData.url}
                  style={{ width: '100%', height: '100%', objectFit: 'contain' }}
                  onTimeUpdate={handleTimeUpdate}
                  onLoadedMetadata={handleLoadedMetadata}
                  onEnded={() => setIsPlaying(false)}
                  onClick={togglePlay}
                />

                {/* Play overlay when paused */}
                <AnimatePresence>
                  {!isPlaying && (
                    <motion.div
                      key="overlay"
                      initial={{ opacity: 0, scale: 0.8 }}
                      animate={{ opacity: 1, scale: 1 }}
                      exit={{ opacity: 0, scale: 0.8 }}
                      onClick={togglePlay}
                      style={{
                        position: 'absolute',
                        width: '80px', height: '80px', borderRadius: '50%',
                        background: 'rgba(0,210,255,0.2)',
                        border: '1px solid var(--neon-blue)',
                        display: 'flex', alignItems: 'center', justifyContent: 'center',
                        cursor: 'pointer',
                        boxShadow: '0 0 30px rgba(0,210,255,0.4)',
                        backdropFilter: 'blur(4px)'
                      }}
                    >
                      <Play size={36} color="var(--neon-cyan)" style={{ marginLeft: '4px' }} />
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>

              {/* Controls */}
              <div style={{ padding: '1.2rem 1.5rem', background: 'rgba(0,0,0,0.7)' }}>
                {/* Seek bar */}
                <div
                  onClick={handleSeek}
                  style={{
                    width: '100%', height: '6px',
                    background: 'var(--glass-border)',
                    borderRadius: '3px',
                    marginBottom: '1rem',
                    cursor: 'pointer',
                    position: 'relative', overflow: 'hidden'
                  }}
                >
                  <motion.div
                    style={{
                      width: `${progress}%`, height: '100%',
                      background: 'linear-gradient(90deg, var(--neon-blue), var(--neon-cyan))',
                      position: 'absolute', left: 0, top: 0,
                      transition: 'width 0.2s linear'
                    }}
                  />
                </div>

                {/* Button row */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div style={{ display: 'flex', gap: '1.2rem', alignItems: 'center' }}>
                    <motion.button
                      whileHover={{ scale: 1.1 }}
                      whileTap={{ scale: 0.95 }}
                      onClick={togglePlay}
                      style={{
                        background: 'none', border: 'none', cursor: 'pointer',
                        display: 'flex', alignItems: 'center'
                      }}
                    >
                      {isPlaying
                        ? <Pause size={26} color="#fff" />
                        : <Play size={26} color="#fff" />}
                    </motion.button>
                    <span style={{ color: 'var(--text-muted)', fontSize: '0.82rem' }}>
                      {fmtTime(videoRef.current?.currentTime)} / {fmtTime(duration)}
                    </span>
                  </div>

                  <div style={{ display: 'flex', gap: '1.2rem', alignItems: 'center' }}>
                    <motion.a
                      href={videoData.url}
                      download="educational_video.mp4"
                      whileHover={{ scale: 1.1 }}
                      style={{ display: 'flex', alignItems: 'center', color: 'var(--text-muted)' }}
                      title="Download"
                    >
                      <Download size={20} />
                    </motion.a>
                    <motion.button
                      whileHover={{ scale: 1.1 }}
                      onClick={handleFullscreen}
                      style={{ background: 'none', border: 'none', cursor: 'pointer', display: 'flex', alignItems: 'center' }}
                      title="Fullscreen"
                    >
                      <Maximize size={20} color="var(--text-muted)" />
                    </motion.button>
                  </div>
                </div>
              </div>
            </motion.div>
          ) : (

            /* ── Placeholder (no video yet) ────────────────────────────────── */
            <motion.div
              key="placeholder"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="glass-panel"
              style={{ padding: 0, overflow: 'hidden', boxShadow: '0 20px 50px rgba(0,0,0,0.5)' }}
            >
              <div style={{
                width: '100%', aspectRatio: '16/9',
                background: 'radial-gradient(circle at center, #111827 0%, #030712 100%)',
                position: 'relative', display: 'flex', alignItems: 'center', justifyContent: 'center',
                flexDirection: 'column', gap: '1rem'
              }}>
                <motion.div
                  animate={{ rotate: 360 }}
                  transition={{ duration: 20, repeat: Infinity, ease: 'linear' }}
                  style={{
                    position: 'absolute', top: '20%', left: '25%',
                    width: '150px', height: '150px',
                    border: '2px solid rgba(255,255,255,0.05)', borderRadius: '30%'
                  }}
                />
                <motion.div
                  animate={{ scale: [1, 1.2, 1], opacity: [0.5, 0.8, 0.5] }}
                  transition={{ duration: 4, repeat: Infinity }}
                  style={{
                    position: 'absolute', bottom: '30%', right: '25%',
                    width: '100px', height: '100px',
                    background: 'rgba(138,43,226,0.15)', borderRadius: '50%', filter: 'blur(10px)'
                  }}
                />
                <Film size={48} color="rgba(255,255,255,0.15)" />
                <p style={{ color: 'rgba(255,255,255,0.25)', fontSize: '0.95rem' }}>
                  Upload a document above to generate your video
                </p>
              </div>

              {/* Static controls bar */}
              <div style={{ padding: '1.5rem', background: 'rgba(0,0,0,0.6)' }}>
                <div style={{
                  width: '100%', height: '6px',
                  background: 'var(--glass-border)', borderRadius: '3px',
                  marginBottom: '1rem', overflow: 'hidden'
                }}>
                  <div style={{ width: '0%', height: '100%', background: 'linear-gradient(90deg, var(--neon-blue), var(--neon-cyan))' }} />
                </div>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div style={{ display: 'flex', gap: '1.2rem', alignItems: 'center' }}>
                    <Play size={26} color="rgba(255,255,255,0.2)" />
                    <span style={{ color: 'var(--text-muted)', fontSize: '0.82rem' }}>0:00 / 0:00</span>
                  </div>
                  <div style={{ display: 'flex', gap: '1.2rem' }}>
                    <Download size={20} color="rgba(255,255,255,0.15)" />
                    <Maximize size={20} color="rgba(255,255,255,0.15)" />
                  </div>
                </div>
              </div>
            </motion.div>
          )}

        </AnimatePresence>

        {/* ── Knowledge Assessment (Quiz) ─────────────────────────────────── */}
        {videoData && (questions.length > 0 || isFetchingQuestions) && (
          <motion.div
            initial={{ opacity: 0, y: 40 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5, duration: 0.8 }}
            style={{ marginTop: '5rem', marginBottom: '4rem' }}
          >
            <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
              <div style={{ 
                display: 'inline-flex', alignItems: 'center', gap: '8px', 
                padding: '8px 16px', background: 'rgba(0,210,255,0.05)',
                border: '1px solid rgba(0,210,255,0.2)', borderRadius: '20px',
                marginBottom: '1rem'
              }}>
                <Activity size={16} color="var(--neon-cyan)" />
                <span style={{ color: 'var(--neon-cyan)', fontSize: '0.8rem', fontWeight: 600, letterSpacing: '1px' }}>
                  POST-LOAD ASSESSMENT
                </span>
              </div>
              <h2 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>
                Knowledge <span style={{ color: 'var(--neon-blue)' }}>Validation</span>
              </h2>
              <p style={{ color: 'var(--text-muted)' }}>
                Test your comprehension of the generated material below.
              </p>
            </div>

            {isFetchingQuestions ? (
              <div style={{ textAlign: 'center', padding: '3rem' }}>
                <motion.div animate={{ rotate: 360 }} transition={{ duration: 2, repeat: Infinity, ease: 'linear' }}>
                  <HelpCircle size={40} color="var(--neon-blue)" style={{ opacity: 0.5 }} />
                </motion.div>
                <p style={{ color: 'var(--text-muted)', marginTop: '1rem' }}>Fetching AI-generated questions...</p>
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
                {questions.map((q, idx) => (
                  <motion.div
                    key={q.id}
                    className="glass-panel"
                    whileHover={{ scale: 1.01 }}
                    style={{
                      padding: '2rem',
                      border: '1px solid var(--glass-border)',
                      position: 'relative',
                      overflow: 'hidden'
                    }}
                  >
                    <div style={{ 
                      position: 'absolute', top: 0, left: 0, width: '4px', height: '100%',
                      background: q.type === 'mcq' ? 'var(--neon-cyan)' : 'var(--neon-violet)'
                    }} />
                    
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                      <h4 style={{ margin: 0, fontSize: '1.2rem', color: '#fff', lineHeight: 1.4, maxWidth: '90%' }}>
                        <span style={{ color: q.type === 'mcq' ? 'var(--neon-cyan)' : 'var(--neon-violet)', marginRight: '10px' }}>
                          {idx + 1}.
                        </span>
                        {q.question}
                      </h4>
                      <span style={{ 
                        fontSize: '0.7rem', padding: '4px 8px', borderRadius: '4px', 
                        background: 'rgba(255,255,255,0.05)', color: 'var(--text-muted)', fontWeight: 600
                      }}>
                        {q.type.toUpperCase()}
                      </span>
                    </div>

                    {q.type === 'mcq' ? (
                      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginTop: '2rem' }}>
                        {q.options.map(opt => {
                          const isSelected = userAnswers[q.id]?.selected === opt;
                          const isCorrect = userAnswers[q.id]?.correct && isSelected;
                          const isWrong = userAnswers[q.id]?.correct === false && isSelected;
                          const hasAlreadySelected = !!userAnswers[q.id]?.selected;
                          const isRevealed = !!userAnswers[q.id]?.everRevealed;

                          return (
                            <motion.button
                              key={opt}
                              whileHover={(!hasAlreadySelected && !isRevealed) ? { x: 5 } : {}}
                              onClick={() => (!hasAlreadySelected && !isRevealed) && handleMcqClick(q, opt)}
                              disabled={hasAlreadySelected || isRevealed}

                              style={{
                                padding: '12px 16px', textAlign: 'left', borderRadius: '8px',
                                border: '1px solid var(--glass-border)',
                                background: isCorrect ? 'rgba(0,255,204,0.1)' : isWrong ? 'rgba(255,51,102,0.1)' : 'rgba(255,255,255,0.02)',
                                color: isCorrect ? '#00ffcc' : isWrong ? '#ff3366' : '#eee',
                                cursor: (hasAlreadySelected || isRevealed) ? 'default' : 'pointer', transition: 'all 0.3s',
                                borderColor: isCorrect ? '#00ffcc' : isWrong ? '#ff3366' : 'var(--glass-border)',
                                opacity: (hasAlreadySelected || isRevealed) && !isSelected ? 0.6 : 1
                              }}
                            >
                              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                                <div style={{ 
                                  width: '18px', height: '18px', borderRadius: '50%', 
                                  border: `2px solid ${isCorrect ? '#00ffcc' : isWrong ? '#ff3366' : '#555'}`,
                                  display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '10px'
                                }}>
                                  {isSelected && <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: isCorrect ? '#00ffcc' : isWrong ? '#ff3366' : 'var(--neon-blue)' }} />}
                                </div>
                                {opt}
                              </div>
                            </motion.button>
                          );
                        })}
                      </div>
                    ) : (
                      <div style={{ marginTop: '2rem' }}>
                        <div style={{ position: 'relative' }}>
                          <textarea 
                            id={`short-ans-${q.id}`}
                            disabled={userAnswers[q.id]?.everRevealed}
                            placeholder={userAnswers[q.id]?.everRevealed ? "Answer was revealed — submission disabled" : "Synthesize your response here..."}
                            style={{ 
                              width: '100%', padding: '16px', borderRadius: '12px', 
                              background: 'rgba(0,0,0,0.3)', border: '1px solid var(--glass-border)',
                              color: userAnswers[q.id]?.everRevealed ? '#555' : '#fff', 
                              fontSize: '0.95rem', minHeight: '100px', outline: 'none', transition: 'all 0.3s',
                              cursor: userAnswers[q.id]?.everRevealed ? 'not-allowed' : 'text'
                            }}

                            onFocus={e => e.target.style.borderColor = 'var(--neon-violet)'}
                          />
                        </div>

                        {!userAnswers[q.id]?.score && (
                          <button 
                            disabled={userAnswers[q.id]?.submitting || userAnswers[q.id]?.everRevealed}
                            onClick={() => {
                              const val = document.getElementById(`short-ans-${q.id}`).value;
                              handleShortSubmit(q, val);
                            }}
                            style={{
                              marginTop: '1rem', padding: '10px 20px', 
                              backgroundColor: (userAnswers[q.id]?.submitting || userAnswers[q.id]?.everRevealed) ? 'rgba(138,43,226,0.3)' : 'var(--neon-violet)',
                              color: 'white', border: 'none', borderRadius: '8px', 
                              cursor: (userAnswers[q.id]?.submitting || userAnswers[q.id]?.everRevealed) ? 'not-allowed' : 'pointer',

                              fontWeight: 600, fontSize: '0.85rem',
                              display: 'flex', alignItems: 'center', gap: '8px'
                            }}
                          >
                            {userAnswers[q.id]?.submitting ? (
                              <>
                                <motion.div 
                                  animate={{ rotate: 360 }} 
                                  transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
                                  style={{ width: '14px', height: '14px', border: '2px solid white', borderTopColor: 'transparent', borderRadius: '50%' }}
                                />
                                Analyzing Response...
                              </>
                            ) : 'Submit Analysis'}
                          </button>
                        )}


                        
                        {userAnswers[q.id]?.score !== undefined && (
                          <motion.div 
                            initial={{ opacity: 0, x: -10 }}
                            animate={{ opacity: 1, x: 0 }}
                            style={{ 
                              marginTop: '1.5rem', padding: '1.5rem', 
                              background: 'rgba(138,43,226,0.05)', borderRadius: '12px',
                              borderLeft: '4px solid var(--neon-violet)'
                            }}
                          >
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.8rem' }}>
                              <span style={{ fontWeight: 700, color: 'var(--neon-violet)' }}>AI ANALYSIS COMPLETE</span>
                              <span style={{ fontSize: '1.2rem', fontWeight: 800, color: '#fff' }}>{userAnswers[q.id].score}% Accuracy</span>
                            </div>
                            <p style={{ margin: 0, color: 'var(--text-muted)', fontSize: '0.9rem', lineHeight: 1.5 }}>
                              {userAnswers[q.id].feedback}
                            </p>
                          </motion.div>
                        )}
                      </div>
                    )}


                    <div style={{ marginTop: '1.5rem', display: 'flex', justifyContent: 'flex-end', gap: '20px' }}>
                      {q.hint && (
                        <button 
                          onClick={() => toggleShowHint(q.id)}
                          style={{ 
                            display: 'flex', alignItems: 'center', gap: '6px',
                            fontSize: '0.8rem', color: userAnswers[q.id]?.showHint ? 'var(--neon-yellow)' : 'var(--text-muted)', 
                            background: 'none', border: 'none', cursor: 'pointer', transition: 'color 0.3s'
                          }}
                        >
                          <Lightbulb size={14} />
                          {userAnswers[q.id]?.showHint ? 'Hide Hint' : 'Show Hint'}
                        </button>
                      )}
                      
                      <button 
                        onClick={() => toggleShowAnswer(q.id)}
                        style={{ 
                          display: 'flex', alignItems: 'center', gap: '6px',
                          fontSize: '0.8rem', color: 'var(--text-muted)', background: 'none', 
                          border: 'none', cursor: 'pointer', transition: 'color 0.3s'
                        }}
                        onMouseOver={e => e.target.style.color = 'var(--neon-cyan)'}
                        onMouseOut={e => e.target.style.color = 'var(--text-muted)'}
                      >
                        {userAnswers[q.id]?.showAnswer ? <ChevronUp size={14} /> : <ChevronDown size={14} />}
                        {userAnswers[q.id]?.showAnswer ? 'Hide Intelligence Key' : 'Reveal Intelligence Key'}
                      </button>
                    </div>

                    <AnimatePresence>
                      {userAnswers[q.id]?.showHint && q.hint && (
                        <motion.div 
                          initial={{ height: 0, opacity: 0 }}
                          animate={{ height: 'auto', opacity: 1 }}
                          exit={{ height: 0, opacity: 0 }}
                          style={{ overflow: 'hidden' }}
                        >
                          <div style={{ 
                            marginTop: '1rem', padding: '1rem', 
                            background: 'rgba(255,255,0,0.05)', borderRadius: '8px',
                            border: '1px dashed rgba(255,255,0,0.3)', color: '#ffee00', fontSize: '0.9rem',
                            display: 'flex', alignItems: 'flex-start', gap: '10px'
                          }}>
                            <Lightbulb size={16} style={{ marginTop: '2px' }} />
                            <span><strong>Hint:</strong> {q.hint}</span>
                          </div>
                        </motion.div>
                      )}

                      {userAnswers[q.id]?.showAnswer && (

                        <motion.div 
                          initial={{ height: 0, opacity: 0 }}
                          animate={{ height: 'auto', opacity: 1 }}
                          exit={{ height: 0, opacity: 0 }}
                          style={{ overflow: 'hidden' }}
                        >
                          <div style={{ 
                            marginTop: '1rem', padding: '1rem', 
                            background: 'rgba(0,255,204,0.05)', borderRadius: '8px',
                            border: '1px dashed rgba(0,255,204,0.3)', color: '#00ffcc', fontSize: '0.9rem'
                          }}>
                            <strong>Reference Answer:</strong> {q.type === 'mcq' ? q.correct_answer : q.answer}
                          </div>
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </motion.div>
                ))}
              </div>
            )}
          </motion.div>
        )}
      </div>
    </section>

  );
};

export default VideoPreview;
