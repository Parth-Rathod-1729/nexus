import React, { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { UploadCloud, File, Activity, Search, CheckCircle, AlertCircle, Cpu, Settings, Zap, ArrowRight } from 'lucide-react';
import { useVideo } from '../contexts';

const BACKEND = () => {
  const raw = import.meta.env.VITE_BACKEND_SERVER || 'http://localhost:4000';
  return raw.endsWith('/') ? raw.slice(0, -1) : raw;
};

const UploadSection = () => {
  const [isHovered, setIsHovered] = useState(false);
  const [isUploading, setIsUploading] = useState(false);
  const fileInputRef = useRef(null);

  const [jobId, setJobId] = useState(null);
  const [status, setStatus] = useState('idle'); // idle | processing | done | error
  const [statusMessage, setStatusMessage] = useState('');
  const [errorMsg, setErrorMsg] = useState('');
  
  // Parameters
  const [numMcqs, setNumMcqs] = useState(3);
  const [numShorts, setNumShorts] = useState(2);
  const [audioLanguage, setAudioLanguage] = useState('english');
  const [targetConcept, setTargetConcept] = useState('');
  
  const [showModal, setShowModal] = useState(false);
  const [pendingFile, setPendingFile] = useState(null);

  const { setVideoData } = useVideo();

  const handleFileChange = (e) => {
    const file = e.target.files && e.target.files[0];
    if (!file) return;
    setPendingFile(file);
    setShowModal(true);
  };

  const startGeneration = async () => {
    if (!pendingFile) return;
    setShowModal(false);
    setIsUploading(true);
    setStatus('processing');
    setStatusMessage('UPLOADING SOURCE MATERIAL...');
    setJobId(null);
    setErrorMsg('');
    setVideoData(null);

    const formData = new FormData();
    formData.append('document', pendingFile);
    formData.append('num_mcqs', numMcqs);
    formData.append('num_shorts', numShorts);
    formData.append('audio_language', audioLanguage);
    formData.append('target_concept', targetConcept);

    try {
      const res = await fetch(`${BACKEND()}/api/pipeline/generate`, {
        method: 'POST',
        body: formData
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'PIPELINE INITIATION FAILED');
      setJobId(data.jobId);
      setStatusMessage('INGESTION COMPLETE. SYNTHESIZING SCENES...');
    } catch (err) {
      setStatus('error');
      setErrorMsg(err.message);
      setIsUploading(false);
    }
  };

  const handleBoxClick = () => {
    if (!isUploading && fileInputRef.current) {
      fileInputRef.current.click();
    }
  };

  useEffect(() => {
    if (!jobId || status !== 'processing') return;

    const interval = setInterval(async () => {
      try {
        const res = await fetch(`${BACKEND()}/api/pipeline/status/${jobId}`);
        const data = await res.json();

        if (data.statusMessage) setStatusMessage(data.statusMessage.toUpperCase());

        if (data.status === 'done') {
          clearInterval(interval);
          setStatus('done');
          setIsUploading(false);

          const fullUrl = `${BACKEND()}${data.videoUrl}`;
          setVideoData({
            jobId: jobId,
            url: fullUrl,
            statusMessage: data.statusMessage || 'SYNTHESIS COMPLETE',
            scenesRendered: data.scenesRendered,
            scenesTotal: data.scenesTotal
          });

          setTimeout(() => {
            document.getElementById('preview')?.scrollIntoView({
              behavior: 'smooth', block: 'start'
            });
          }, 800);

        } else if (data.status === 'error') {
          clearInterval(interval);
          setStatus('error');
          setIsUploading(false);
          setErrorMsg(data.error || 'PIPELINE EXECUTION ERROR');
        }
      } catch (err) {
        console.error('Polling error:', err);
      }
    }, 3000);

    return () => clearInterval(interval);
  }, [jobId, status]);

  const reset = (e) => {
    e?.stopPropagation();
    setStatus('idle');
    setErrorMsg('');
    setStatusMessage('');
    setJobId(null);
    setIsUploading(false);
    setPendingFile(null);
    if (fileInputRef.current) fileInputRef.current.value = '';
  };

  return (
    <section style={{ position: 'relative' }}>
      <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
          style={{ 
            display: 'inline-flex', alignItems: 'center', gap: '8px', 
            padding: '8px 16px', background: 'hsla(var(--neon-cyan-h), 100%, 50%, 0.05)',
            border: '1px solid hsla(var(--neon-cyan-h), 100%, 50%, 0.2)', borderRadius: '20px',
            marginBottom: '1rem'
          }}
        >
          <Zap size={14} color="var(--neon-cyan)" />
          <span style={{ color: 'var(--neon-cyan)', fontSize: '0.75rem', fontWeight: 800, letterSpacing: '2px' }}>
            MODULE 01: DATA INGESTION
          </span>
        </motion.div>
        <h2 style={{ fontSize: '3rem', marginBottom: '1rem' }}>
          Initiate <span className="text-gradient">Protocol</span>
        </h2>
        <p style={{ color: 'var(--text-muted)', fontSize: '1.1rem' }}>Upload source material to prime the RAG pipeline synthesis.</p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1.2fr 0.8fr', gap: '3rem', alignItems: 'stretch' }}>

        {/* ── Upload Box ─────────────────────────────────────────────────── */}
        <motion.div
          className="glass-panel"
          whileHover={!isUploading ? { scale: 1.01 } : {}}
          onHoverStart={() => setIsHovered(true)}
          onHoverEnd={() => setIsHovered(false)}
          onClick={handleBoxClick}
          style={{
            padding: '5rem 2rem',
            textAlign: 'center',
            cursor: isUploading ? 'default' : 'pointer',
            border: isHovered && !isUploading
              ? '1px solid var(--neon-blue)'
              : status === 'done'
                ? '1px solid var(--neon-cyan)'
                : status === 'error'
                  ? '1px solid var(--neon-error)'
                  : '1px solid var(--glass-border)',
            background: isHovered && !isUploading ? 'hsla(var(--neon-blue-h), 100%, 50%, 0.02)' : 'var(--glass-bg)',
            minHeight: '340px',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            overflow: 'hidden'
          }}
        >
          {isUploading && <div className="scanline" />}
          
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleFileChange}
            accept=".pdf,.doc,.docx,.ppt,.pptx,.txt"
            style={{ display: 'none' }}
          />

          <AnimatePresence mode="wait">

            {status === 'idle' && (
              <motion.div key="idle" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
                <div style={{
                  background: 'hsla(var(--neon-blue-h), 100%, 50%, 0.05)', width: '100px', height: '100px',
                  borderRadius: '30%', display: 'flex', alignItems: 'center', justifyContent: 'center',
                  margin: '0 auto 2rem', border: '1px solid hsla(var(--neon-blue-h), 100%, 50%, 0.2)',
                  boxShadow: '0 0 30px hsla(var(--neon-blue-h), 100%, 50%, 0.1)'
                }}>
                  <UploadCloud size={48} color="var(--neon-blue)" className="text-glow" />
                </div>
                <h3 style={{ fontSize: '1.6rem', marginBottom: '0.5rem', fontWeight: 600 }}>DROP MATERIAL HERE</h3>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', letterSpacing: '1px' }}>PDF // DOCX // PPTX // TXT</p>
                <div style={{ marginTop: '2rem', display: 'flex', justifyContent: 'center' }}>
                  <motion.div animate={isHovered ? { y: [0, -8, 0] } : {}} transition={{ repeat: Infinity, duration: 1.5 }}>
                    <File size={28} color={isHovered ? 'var(--neon-cyan)' : 'var(--text-muted)'} style={{ opacity: isHovered ? 1 : 0.4 }} />
                  </motion.div>
                </div>
              </motion.div>
            )}

            {status === 'processing' && (
              <motion.div
                key="processing"
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0 }}
                style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', position: 'relative' }}
              >
                {/* ── Aesthetic Orbital Core ────────────────────────────────── */}
                <div style={{ position: 'relative', width: '180px', height: '180px', marginBottom: '2rem', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                  
                  {/* Outer Orbital Ring */}
                  <motion.div
                    animate={{ rotate: 360 }}
                    transition={{ duration: 8, repeat: Infinity, ease: 'linear' }}
                    style={{
                      position: 'absolute', width: '100%', height: '100%',
                      border: '1px dashed hsla(var(--neon-cyan-h), 100%, 50%, 0.15)',
                      borderRadius: '50%'
                    }}
                  />

                  {/* Inner Counter-Rotating Ring */}
                  <motion.div
                    animate={{ rotate: -360 }}
                    transition={{ duration: 12, repeat: Infinity, ease: 'linear' }}
                    style={{
                      position: 'absolute', width: '70%', height: '70%',
                      border: '1px solid hsla(var(--neon-violet-h), 100%, 50%, 0.1)',
                      borderRadius: '50%'
                    }}
                  />

                  {/* New Rotating Glow Circle */}
                  <motion.div
                    animate={{ rotate: 360 }}
                    transition={{ duration: 4, repeat: Infinity, ease: 'linear' }}
                    style={{
                      position: 'absolute', width: '45%', height: '45%',
                      border: '2px solid transparent',
                      borderTop: '2px solid var(--neon-cyan)',
                      borderRight: '2px solid hsla(var(--neon-cyan-h), 100%, 50%, 0.2)',
                      borderRadius: '50%',
                      boxShadow: 'inset 0 0 10px hsla(var(--neon-cyan-h), 100%, 50%, 0.1)'
                    }}
                  />

                  {/* Hex Data Particles */}
                  {[...Array(6)].map((_, i) => (
                    <motion.div
                      key={i}
                      initial={{ opacity: 0, y: 0 }}
                      animate={{ 
                        opacity: [0, 0.8, 0],
                        y: [-20, -60],
                        x: Math.sin(i) * 30
                      }}
                      transition={{ 
                        duration: 2, 
                        repeat: Infinity, 
                        delay: i * 0.4,
                        ease: "easeOut"
                      }}
                      style={{ 
                        position: 'absolute', 
                        fontSize: '0.6rem', 
                        fontFamily: 'monospace', 
                        color: 'var(--neon-cyan)',
                        pointerEvents: 'none'
                      }}
                    >
                      {Math.random().toString(16).substring(2, 6).toUpperCase()}
                    </motion.div>
                  ))}

                  <div style={{ position: 'relative', zIndex: 2 }}>
                    <motion.div
                      animate={{ 
                        scale: [1, 1.05, 1],
                        filter: ['drop-shadow(0 0 10px hsla(var(--neon-cyan-h), 100%, 50%, 0.2))', 'drop-shadow(0 0 25px hsla(var(--neon-cyan-h), 100%, 50%, 0.5))', 'drop-shadow(0 0 10px hsla(var(--neon-cyan-h), 100%, 50%, 0.2))']
                      }}
                      transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
                    >
                      <Cpu size={64} color="var(--neon-cyan)" />
                    </motion.div>
                  </div>
                </div>

                {/* ── Status Text ── */}
                <div style={{ textAlign: 'center' }}>
                  <motion.h3 
                    animate={{ opacity: [0.6, 1, 0.6] }}
                    transition={{ duration: 2, repeat: Infinity }}
                    style={{ 
                      fontSize: '1rem', 
                      color: 'var(--neon-cyan)', 
                      letterSpacing: '4px', 
                      fontWeight: 700,
                      marginBottom: '1.5rem'
                    }}
                  >
                    {statusMessage}
                  </motion.h3>

                  {/* ── Aesthetic Scanning Progress ── */}
                  <div style={{ 
                    width: '240px', 
                    height: '4px', 
                    background: 'var(--surface-1)', 
                    borderRadius: '100px', 
                    overflow: 'hidden', 
                    position: 'relative',
                    border: '1px solid var(--glass-border)'
                  }}>
                    <motion.div
                      animate={{ x: ['-100%', '200%'] }}
                      transition={{ duration: 2.5, repeat: Infinity, ease: "slow" }}
                      style={{ 
                        position: 'absolute', 
                        width: '40%', 
                        height: '100%', 
                        background: 'linear-gradient(90deg, transparent, var(--neon-cyan), var(--neon-blue), transparent)',
                        filter: 'blur(1px)'
                      }}
                    />
                  </div>
                </div>
              </motion.div>
            )}

            {status === 'done' && (
              <motion.div
                key="done"
                initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }}
                style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}
              >
                <div style={{ 
                  width: '80px', height: '80px', borderRadius: '50%', background: 'hsla(var(--neon-cyan-h), 100%, 50%, 0.1)',
                  display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '1.5rem',
                  border: '2px solid var(--neon-cyan)', boxShadow: '0 0 30px hsla(var(--neon-cyan-h), 100%, 50%, 0.3)'
                }}>
                  <CheckCircle size={40} color="var(--neon-cyan)" />
                </div>
                <h3 style={{ fontSize: '1.6rem', color: 'var(--neon-cyan)' }}>SYNTHESIS COMPLETE</h3>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', marginTop: '0.5rem', letterSpacing: '1px' }}>
                  ASSESSMENT PACKAGE READY FOR DEPLOYMENT
                </p>
                <button onClick={reset} className="btn-primary" style={{ marginTop: '2rem' }}>
                  NEW INGESTION
                </button>
              </motion.div>
            )}

            {status === 'error' && (
              <motion.div
                key="error"
                initial={{ opacity: 0 }} animate={{ opacity: 1 }}
                style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}
              >
                <AlertCircle size={64} color="var(--neon-error)" style={{ marginBottom: '1.5rem' }} />
                <h3 style={{ fontSize: '1.5rem', color: 'var(--neon-error)' }}>PROTOCOL ABORTED</h3>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', marginTop: '0.5rem', maxWidth: '300px' }}>
                  {errorMsg}
                </p>
                <button onClick={reset} className="btn-secondary" style={{ marginTop: '2rem' }}>
                  RETRY CONNECTION
                </button>
              </motion.div>
            )}

          </AnimatePresence>
        </motion.div>

        {/* ── Parameters Sidebar ─────────────────────────────────────────── */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <motion.div 
            className="glass-panel" 
            style={{ padding: '2.5rem', height: '100%' }}
            whileHover={{ borderColor: 'var(--neon-violet)' }}
          >
            <h3 style={{ marginBottom: '2rem', display: 'flex', alignItems: 'center', gap: '12px', fontSize: '1.2rem' }}>
              <Settings size={20} color="var(--neon-violet)" /> CONFIGURATION
            </h3>
            
            <div style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
              <div>
                <label style={{ display: 'block', color: 'var(--text-muted)', fontSize: '0.8rem', marginBottom: '0.8rem', letterSpacing: '1px' }}>
                  TARGET CONCEPT
                </label>
                <div style={{ position: 'relative' }}>
                  <Search size={18} style={{ position: 'absolute', left: '16px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
                  <input
                    type="text"
                    placeholder="E.g. Neural Networks"
                    value={targetConcept}
                    onChange={e => setTargetConcept(e.target.value)}
                    style={{
                      width: '100%', padding: '16px 16px 16px 48px',
                      background: 'var(--surface-1)', border: '1px solid var(--glass-border)',
                      borderRadius: '12px', color: '#fff', fontSize: '0.95rem', outline: 'none', transition: 'all 0.3s'
                    }}
                    onFocus={e => e.target.style.borderColor = 'var(--neon-blue)'}
                    onBlur={e => e.target.style.borderColor = 'var(--glass-border)'}
                  />
                </div>
              </div>

              <div style={{ paddingTop: '1rem', borderTop: '1px solid var(--glass-border)' }}>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.8rem', marginBottom: '1rem', letterSpacing: '1px' }}>
                  SUGGESTED VECTORS:
                </p>
                <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
                  {['Architecture', 'Deep Dive', 'History', 'Mechanics'].map((topic, i) => (
                    <motion.span
                      key={topic}
                      whileHover={{ scale: 1.05, background: 'hsla(var(--neon-violet-h), 100%, 50%, 0.1)', borderColor: 'var(--neon-violet)' }}
                      onClick={() => setTargetConcept(topic)}
                      style={{
                        padding: '6px 14px', background: 'var(--surface-1)',
                        border: '1px solid var(--glass-border)', borderRadius: '100px',
                        fontSize: '0.8rem', cursor: 'pointer', transition: 'all 0.2s', color: 'var(--text-muted)'
                      }}
                    >
                      {topic}
                    </motion.span>
                  ))}
                </div>
              </div>
            </div>
          </motion.div>
        </div>

      </div>

      {/* ── Parameter Modal ────────────────────────────────────────────── */}
      <AnimatePresence>
        {showModal && (
          <motion.div 
            initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            style={{
              position: 'fixed', inset: 0, background: 'rgba(5, 11, 20, 0.9)', backdropFilter: 'blur(12px)',
              zIndex: 2000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px'
            }}
          >
            <motion.div 
              initial={{ scale: 0.9, y: 40 }} animate={{ scale: 1, y: 0 }} exit={{ scale: 0.9, y: 40 }}
              className="glass-panel"
              style={{ padding: '3rem', width: '100%', maxWidth: '500px', border: '1px solid var(--neon-cyan)' }}
            >
              <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
                <h3 style={{ fontSize: '1.8rem', marginBottom: '0.5rem' }}>SYMBOLS CONFIG</h3>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>IDENTIFIED: <span style={{ color: 'var(--neon-cyan)' }}>{pendingFile?.name}</span></p>
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem', marginBottom: '3rem' }}>
                <div>
                  <label style={{ display: 'block', color: 'var(--text-muted)', fontSize: '0.75rem', marginBottom: '0.6rem' }}>MCQ COUNT</label>
                  <input type="number" min="0" max="10" value={numMcqs} onChange={e => setNumMcqs(e.target.value)}
                    style={{ width: '100%', padding: '14px', background: 'var(--surface-1)', border: '1px solid var(--glass-border)', borderRadius: '12px', color: '#fff', textAlign: 'center' }}
                  />
                </div>
                <div>
                  <label style={{ display: 'block', color: 'var(--text-muted)', fontSize: '0.75rem', marginBottom: '0.6rem' }}>SHORT ANS</label>
                  <input type="number" min="0" max="10" value={numShorts} onChange={e => setNumShorts(e.target.value)}
                    style={{ width: '100%', padding: '14px', background: 'var(--surface-1)', border: '1px solid var(--glass-border)', borderRadius: '12px', color: '#fff', textAlign: 'center' }}
                  />
                </div>
                <div style={{ gridColumn: 'span 2' }}>
                  <label style={{ display: 'block', color: 'var(--text-muted)', fontSize: '0.75rem', marginBottom: '0.6rem' }}>LINGUISTIC PROTOCOL</label>
                  <select value={audioLanguage} onChange={e => setAudioLanguage(e.target.value)}
                    style={{ width: '100%', padding: '14px', background: 'var(--surface-1)', border: '1px solid var(--glass-border)', borderRadius: '12px', color: '#fff', outline: 'none' }}
                  >
                    <option value="english">English (US/UK)</option>
                    <option value="hinglish">Hinglish (Hybrid)</option>
                    <option value="hindi">Hindi (Native)</option>
                  </select>
                </div>
              </div>

              <div style={{ display: 'flex', gap: '1rem' }}>
                <button onClick={() => { setShowModal(false); setPendingFile(null); }} className="btn-secondary" style={{ flex: 1 }}>ABORT</button>
                <button onClick={startGeneration} className="btn-primary" style={{ flex: 1 }}>
                  PRIME <ArrowRight size={16} />
                </button>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
};

export default UploadSection;

