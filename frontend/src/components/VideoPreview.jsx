import React, { useRef, useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Play, Pause, Maximize, Download, Film, Layers, CheckCircle, AlertCircle, HelpCircle, ChevronDown, ChevronUp, Activity, Lightbulb, Send, RotateCcw } from 'lucide-react';
import { useVideo } from '../contexts';

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
  const [userAnswers, setUserAnswers] = useState({}); // { qId: { selected, result, score, feedback, showAnswer, showHint, everRevealed, currentInput } }
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

  useEffect(() => {
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
        [q.id]: { ...prev[q.id], selected: option, ...result }
      }));
    } catch (err) {
      console.error("MCQ check failed:", err);
    }
  };

  const handleShortSubmit = async (q) => {
    const answer = userAnswers[q.id]?.currentInput || '';
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
        [q.id]: { ...prev[q.id], submitted: answer, ...result, submitting: false }
      }));
    } catch (err) {
      console.error("Short answer check failed:", err);
      setUserAnswers(prev => ({
        ...prev,
        [q.id]: { ...prev[q.id], submitting: false }
      }));
    }
  };

  const handleInputChange = (qId, val) => {
    setUserAnswers(prev => ({
      ...prev,
      [qId]: { ...prev[qId], currentInput: val }
    }));
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
        everRevealed: true 
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
    <section id="preview">
      <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          style={{ 
            display: 'inline-flex', alignItems: 'center', gap: '8px', 
            padding: '8px 16px', background: 'hsla(var(--neon-violet-h), 100%, 50%, 0.05)',
            border: '1px solid hsla(var(--neon-violet-h), 100%, 50%, 0.2)', borderRadius: '20px',
            marginBottom: '1rem'
          }}
        >
          <Film size={14} color="var(--neon-violet)" />
          <span style={{ color: 'var(--neon-violet)', fontSize: '0.75rem', fontWeight: 800, letterSpacing: '2px' }}>
            MODULE 02: VISUAL SYNTHESIS
          </span>
        </motion.div>
        <h2 style={{ fontSize: '3rem', marginBottom: '1rem' }}>
          Final <span className="text-gradient">Render</span>
        </h2>
        <p style={{ color: 'var(--text-muted)', fontSize: '1.1rem' }}>
          Fully synthesized cinematic assessment ready for deployment.
        </p>
      </div>

      <div style={{ maxWidth: '1000px', margin: '0 auto' }}>
        <AnimatePresence mode="wait">

          {videoData ? (
            <motion.div
              key="player"
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 1.05 }}
              className="glass-panel"
              style={{
                padding: 0, overflow: 'hidden',
                boxShadow: '0 40px 100px hsla(var(--neon-blue-h), 100%, 50%, 0.1)',
                border: '1px solid hsla(var(--neon-cyan-h), 100%, 50%, 0.2)'
              }}
            >
              <div style={{
                display: 'flex', justifyContent: 'space-between', alignItems: 'center',
                padding: '16px 24px', background: 'hsla(var(--neon-cyan-h), 100%, 50%, 0.05)',
                borderBottom: '1px solid hsla(var(--neon-cyan-h), 100%, 50%, 0.1)'
              }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                  <motion.div
                    animate={{ scale: [1, 1.2, 1], opacity: [0.6, 1, 0.6] }}
                    transition={{ duration: 2, repeat: Infinity }}
                    style={{ width: '10px', height: '10px', borderRadius: '50%', background: 'var(--neon-cyan)', boxShadow: '0 0 10px var(--neon-cyan)' }}
                  />
                  <span style={{ color: 'var(--neon-cyan)', fontSize: '0.85rem', fontWeight: 800, letterSpacing: '1px' }}>
                    {videoData.statusMessage?.toUpperCase() || 'UPLINK STABLE'}
                  </span>
                </div>
                {videoData.scenesRendered !== undefined && (
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--text-muted)', fontSize: '0.8rem', fontWeight: 600 }}>
                    <Layers size={14} />
                    <span>{videoData.scenesRendered} / {videoData.scenesTotal} SECTORS</span>
                  </div>
                )}
              </div>

              <div style={{ width: '100%', aspectRatio: '16/9', background: '#000', position: 'relative' }}>
                <video
                  ref={videoRef}
                  src={videoData.url}
                  style={{ width: '100%', height: '100%', objectFit: 'contain' }}
                  onTimeUpdate={handleTimeUpdate}
                  onLoadedMetadata={handleLoadedMetadata}
                  onEnded={() => setIsPlaying(false)}
                  onClick={togglePlay}
                />

                <AnimatePresence>
                  {!isPlaying && (
                    <motion.div
                      key="play-overlay"
                      initial={{ opacity: 0, scale: 0.8 }}
                      animate={{ opacity: 1, scale: 1 }}
                      exit={{ opacity: 0, scale: 0.8 }}
                      onClick={togglePlay}
                      style={{
                        position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center',
                        background: 'rgba(0,0,0,0.3)', backdropFilter: 'blur(4px)', cursor: 'pointer'
                      }}
                    >
                      <div style={{
                        width: '90px', height: '90px', borderRadius: '50%',
                        background: 'hsla(var(--neon-blue-h), 100%, 50%, 0.1)',
                        border: '2px solid var(--neon-blue)',
                        display: 'flex', alignItems: 'center', justifyContent: 'center',
                        boxShadow: '0 0 40px hsla(var(--neon-blue-h), 100%, 50%, 0.3)'
                      }}>
                        <Play size={40} color="var(--neon-cyan)" fill="var(--neon-cyan)" style={{ marginLeft: '6px' }} />
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>

              <div style={{ padding: '1.5rem 2rem', background: 'var(--surface-1)' }}>
                <div
                  onClick={handleSeek}
                  style={{ width: '100%', height: '8px', background: 'var(--surface-2)', borderRadius: '4px', marginBottom: '1.5rem', cursor: 'pointer', position: 'relative', overflow: 'hidden' }}
                >
                  <motion.div
                    style={{ width: `${progress}%`, height: '100%', background: 'linear-gradient(90deg, var(--neon-blue), var(--neon-cyan))', position: 'absolute', left: 0, top: 0 }}
                  />
                </div>

                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div style={{ display: 'flex', gap: '2rem', alignItems: 'center' }}>
                    <motion.button whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.9 }} onClick={togglePlay} style={{ background: 'none', border: 'none', cursor: 'pointer' }}>
                      {isPlaying ? <Pause size={28} color="#fff" /> : <Play size={28} color="#fff" fill="#fff" />}
                    </motion.button>
                    <span style={{ color: 'var(--text-muted)', fontSize: '0.9rem', fontWeight: 600, fontFamily: 'monospace' }}>
                      {fmtTime(videoRef.current?.currentTime)} / {fmtTime(duration)}
                    </span>
                  </div>

                  <div style={{ display: 'flex', gap: '1.5rem', alignItems: 'center' }}>
                    <motion.a href={videoData.url} download whileHover={{ scale: 1.1 }} style={{ color: 'var(--text-muted)' }}>
                      <Download size={22} />
                    </motion.a>
                    <motion.button whileHover={{ scale: 1.1 }} onClick={handleFullscreen} style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-muted)' }}>
                      <Maximize size={22} />
                    </motion.button>
                  </div>
                </div>
              </div>
            </motion.div>
          ) : (
            <motion.div
              key="placeholder"
              className="glass-panel"
              style={{ padding: '10rem 2rem', textAlign: 'center', borderStyle: 'dashed', borderColor: 'var(--glass-border)' }}
            >
              <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1.5rem', opacity: 0.3 }}>
                <Film size={64} />
                <p style={{ fontSize: '1.1rem', letterSpacing: '2px' }}>WAITING FOR INGESTION MODULE...</p>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* ── Knowledge Assessment ────────────────────────────────────────── */}
        {videoData && (questions.length > 0 || isFetchingQuestions) && (
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            style={{ marginTop: '8rem' }}
          >
            <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
              <div style={{ 
                display: 'inline-flex', alignItems: 'center', gap: '10px', 
                padding: '10px 20px', background: 'hsla(var(--neon-cyan-h), 100%, 50%, 0.05)',
                border: '1px solid hsla(var(--neon-cyan-h), 100%, 50%, 0.2)', borderRadius: '100px',
                marginBottom: '1.5rem'
              }}>
                <Activity size={16} color="var(--neon-cyan)" />
                <span style={{ color: 'var(--neon-cyan)', fontSize: '0.8rem', fontWeight: 800, letterSpacing: '2px' }}>
                  POST-LOAD EVALUATION
                </span>
              </div>
              <h2 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>
                Cognitive <span className="text-gradient">Validation</span>
              </h2>
            </div>

            {isFetchingQuestions ? (
              <div style={{ textAlign: 'center', padding: '4rem' }}>
                <motion.div animate={{ rotate: 360 }} transition={{ duration: 3, repeat: Infinity, ease: 'linear' }}>
                  <RotateCcw size={48} color="var(--neon-blue)" style={{ opacity: 0.5 }} />
                </motion.div>
                <p style={{ color: 'var(--text-muted)', marginTop: '1.5rem', letterSpacing: '1px' }}>ANALYZING NEURAL PATTERNS...</p>
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '2.5rem' }}>
                {questions.map((q, idx) => (
                  <motion.div
                    key={q.id}
                    className="glass-panel"
                    initial={{ opacity: 0, x: -20 }}
                    whileInView={{ opacity: 1, x: 0 }}
                    transition={{ delay: idx * 0.1 }}
                    style={{ padding: '3rem', borderLeftWidth: '6px', borderLeftColor: q.type === 'mcq' ? 'var(--neon-cyan)' : 'var(--neon-violet)' }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '2.5rem' }}>
                      <h4 style={{ margin: 0, fontSize: '1.4rem', color: '#fff', lineHeight: 1.4, maxWidth: '85%' }}>
                        <span style={{ opacity: 0.3, marginRight: '15px' }}>{String(idx + 1).padStart(2, '0')}</span>
                        {q.question}
                      </h4>
                      <div style={{ padding: '4px 12px', borderRadius: '4px', background: 'var(--surface-1)', color: 'var(--text-muted)', fontSize: '0.7rem', fontWeight: 800 }}>
                        {q.type.toUpperCase()}
                      </div>
                    </div>

                    {q.type === 'mcq' ? (
                      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '1rem' }}>
                        {q.options.map(opt => {
                          const state = userAnswers[q.id] || {};
                          const isSelected = state.selected === opt;
                          const isCorrect = state.correct && isSelected;
                          const isWrong = state.correct === false && isSelected;
                          const disabled = !!state.selected || state.everRevealed;

                          return (
                            <motion.button
                              key={opt}
                              whileHover={!disabled ? { scale: 1.02, x: 5 } : {}}
                              onClick={() => !disabled && handleMcqClick(q, opt)}
                              disabled={disabled}
                              style={{
                                padding: '1.2rem', textAlign: 'left', borderRadius: '12px',
                                background: isCorrect ? 'hsla(var(--neon-cyan-h), 100%, 50%, 0.1)' : isWrong ? 'hsla(0, 100%, 50%, 0.1)' : 'var(--surface-1)',
                                border: '1px solid',
                                borderColor: isCorrect ? 'var(--neon-cyan)' : isWrong ? 'var(--neon-error)' : 'var(--glass-border)',
                                color: isCorrect ? 'var(--neon-cyan)' : isWrong ? 'var(--neon-error)' : '#fff',
                                cursor: disabled ? 'default' : 'pointer', transition: 'all 0.3s',
                                opacity: disabled && !isSelected ? 0.4 : 1
                              }}
                            >
                              {opt}
                            </motion.button>
                          );
                        })}
                      </div>
                    ) : (
                      <div>
                        <textarea
                          placeholder="SYNTHESIZE RESPONSE..."
                          disabled={userAnswers[q.id]?.everRevealed}
                          value={userAnswers[q.id]?.currentInput || ''}
                          onChange={(e) => handleInputChange(q.id, e.target.value)}
                          style={{
                            width: '100%', padding: '1.5rem', borderRadius: '16px',
                            background: 'var(--surface-1)', border: '1px solid var(--glass-border)',
                            color: '#fff', fontSize: '1rem', minHeight: '120px', outline: 'none', transition: 'all 0.3s'
                          }}
                        />
                        {!userAnswers[q.id]?.score && (
                          <button
                            disabled={userAnswers[q.id]?.submitting || userAnswers[q.id]?.everRevealed}
                            onClick={() => handleShortSubmit(q)}
                            className="btn-primary"
                            style={{ marginTop: '1.5rem' }}
                          >
                            {userAnswers[q.id]?.submitting ? <Activity className="rotate" /> : <Send size={18} />}
                            {userAnswers[q.id]?.submitting ? 'PROCESSING...' : 'SUBMIT ANALYSIS'}
                          </button>
                        )}
                        {userAnswers[q.id]?.score !== undefined && (
                          <motion.div initial={{ opacity: 0, scale: 0.95 }} animate={{ opacity: 1, scale: 1 }} style={{ marginTop: '2rem', padding: '2rem', background: 'hsla(var(--neon-violet-h), 100%, 50%, 0.05)', borderRadius: '16px', border: '1px solid hsla(var(--neon-violet-h), 100%, 50%, 0.2)' }}>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
                              <span style={{ color: 'var(--neon-violet)', fontWeight: 800, letterSpacing: '1px' }}>ACCURACY RATING</span>
                              <span style={{ fontSize: '1.5rem', fontWeight: 900 }}>{userAnswers[q.id].score}%</span>
                            </div>
                            <p style={{ margin: 0, color: 'var(--text-muted)', lineHeight: 1.6 }}>{userAnswers[q.id].feedback}</p>
                          </motion.div>
                        )}
                      </div>
                    )}

                    <div style={{ marginTop: '2.5rem', display: 'flex', justifyContent: 'flex-end', gap: '2rem' }}>
                      {q.hint && (
                        <button onClick={() => toggleShowHint(q.id)} style={{ display: 'flex', alignItems: 'center', gap: '8px', color: userAnswers[q.id]?.showHint ? 'var(--neon-yellow)' : 'var(--text-muted)', background: 'none', border: 'none', cursor: 'pointer', fontSize: '0.8rem', fontWeight: 600 }}>
                          <Lightbulb size={16} /> {userAnswers[q.id]?.showHint ? 'HIDE HINT' : 'REQUEST HINT'}
                        </button>
                      )}
                      <button onClick={() => toggleShowAnswer(q.id)} style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--text-muted)', background: 'none', border: 'none', cursor: 'pointer', fontSize: '0.8rem', fontWeight: 600 }}>
                        {userAnswers[q.id]?.showAnswer ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                        {userAnswers[q.id]?.showAnswer ? 'HIDE KEY' : 'REVEAL KEY'}
                      </button>
                    </div>

                    <AnimatePresence>
                      {userAnswers[q.id]?.showHint && (
                        <motion.div initial={{ height: 0, opacity: 0 }} animate={{ height: 'auto', opacity: 1 }} exit={{ height: 0, opacity: 0 }} style={{ overflow: 'hidden' }}>
                          <div style={{ marginTop: '1.5rem', padding: '1.2rem', background: 'hsla(60, 100%, 50%, 0.05)', borderRadius: '8px', border: '1px dashed hsla(60, 100%, 50%, 0.3)', color: 'var(--neon-yellow)', fontSize: '0.9rem' }}>
                            <strong>ENCRYPTED HINT:</strong> {q.hint}
                          </div>
                        </motion.div>
                      )}
                      {userAnswers[q.id]?.showAnswer && (
                        <motion.div initial={{ height: 0, opacity: 0 }} animate={{ height: 'auto', opacity: 1 }} exit={{ height: 0, opacity: 0 }} style={{ overflow: 'hidden' }}>
                          <div style={{ marginTop: '1rem', padding: '1.2rem', background: 'hsla(var(--neon-cyan-h), 100%, 50%, 0.05)', borderRadius: '8px', border: '1px dashed hsla(var(--neon-cyan-h), 100%, 50%, 0.3)', color: 'var(--neon-cyan)', fontSize: '0.9rem' }}>
                            <strong>MASTER KEY:</strong> {q.type === 'mcq' ? q.correct_answer : q.answer}
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
