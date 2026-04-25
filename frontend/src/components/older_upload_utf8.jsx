import React, { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { UploadCloud, File, Activity, Search, CheckCircle, AlertCircle, Cpu } from 'lucide-react';
import { useVideo } from '../App';

const BACKEND = () => {
  const raw = import.meta.env.VITE_BACKEND_SERVER || 'http://localhost:4000';
  return raw.endsWith('/') ? raw.slice(0, -1) : raw;
};

const UploadSection = () => {
  const [isHovered, setIsHovered] = useState(false);
  const [isUploading, setIsUploading] = useState(false);
  const fileInputRef = useRef(null);
  const videoSectionRef = useRef(null);

  const [jobId, setJobId] = useState(null);
  const [status, setStatus] = useState('idle'); // idle | processing | done | error
  const [statusMessage, setStatusMessage] = useState('');
  const [errorMsg, setErrorMsg] = useState('');
  const [numMcqs, setNumMcqs] = useState(3);
  const [numShorts, setNumShorts] = useState(2);
  const [audioLanguage, setAudioLanguage] = useState('english');
  const [showModal, setShowModal] = useState(false);
  const [pendingFile, setPendingFile] = useState(null);

  const { setVideoData } = useVideo();

  // ΓöÇΓöÇ File upload ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇ
  const handleFileChange = (e) => {
    const file = e.target.files && e.target.files[0];
    if (!file) return;
    setPendingFile(file);
    setShowModal(true); // Show modal instead of uploading immediately
  };

  const startGeneration = async () => {
    if (!pendingFile) return;
    setShowModal(false);
    setIsUploading(true);
    setStatus('processing');
    setStatusMessage('Uploading document...');
    setJobId(null);
    setErrorMsg('');
    setVideoData(null);

    const formData = new FormData();
    formData.append('document', pendingFile);
    formData.append('num_mcqs', numMcqs);
    formData.append('num_shorts', numShorts);
    formData.append('audio_language', audioLanguage);

    try {
      const res = await fetch(`${BACKEND()}/api/pipeline/generate`, {
        method: 'POST',
        body: formData
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Failed to start generation');
      setJobId(data.jobId);
      setStatusMessage('Pipeline started ΓÇö generating scenes...');
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

  // ΓöÇΓöÇ Polling ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇ
  useEffect(() => {
    if (!jobId || status !== 'processing') return;

    const interval = setInterval(async () => {
      try {
        const res = await fetch(`${BACKEND()}/api/pipeline/status/${jobId}`);
        const data = await res.json();

        // Always update status message if present
        if (data.statusMessage) setStatusMessage(data.statusMessage);

        if (data.status === 'done') {
          clearInterval(interval);
          setStatus('done');
          setIsUploading(false);

          const fullUrl = `${BACKEND()}${data.videoUrl}`;
          setVideoData({
            jobId: jobId,
            url: fullUrl,
            statusMessage: data.statusMessage || 'Done',
            scenesRendered: data.scenesRendered,
            scenesTotal: data.scenesTotal
          });


          // Auto-scroll to VideoPreview section after a short delay
          setTimeout(() => {
            document.getElementById('video-preview-section')?.scrollIntoView({
              behavior: 'smooth', block: 'start'
            });
          }, 800);

        } else if (data.status === 'error') {
          clearInterval(interval);
          setStatus('error');
          setIsUploading(false);
          setErrorMsg(data.error || 'Server processing error');
        }
      } catch (err) {
        console.error('Polling error:', err);
      }
    }, 3000);

    return () => clearInterval(interval);
  }, [jobId, status]);

  // ΓöÇΓöÇ Reset ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇ
  const reset = (e) => {
    e?.stopPropagation();
    setStatus('idle');
    setErrorMsg('');
    setStatusMessage('');
    setJobId(null);
    setIsUploading(false);
    if (fileInputRef.current) fileInputRef.current.value = '';
  };

  return (
    <section>
      <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
        <h2 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>
          Initiate <span style={{ color: 'var(--neon-blue)' }}>Data Ingestion</span>
        </h2>
        <p style={{ color: 'var(--text-muted)' }}>Upload source material to prime the RAG pipeline.</p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem', alignItems: 'start' }}>

        {/* ΓöÇΓöÇ Upload Box ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇ */}
        <motion.div
          className="glass-panel"
          whileHover={!isUploading ? { scale: 1.02 } : {}}
          onHoverStart={() => setIsHovered(true)}
          onHoverEnd={() => setIsHovered(false)}
          onClick={handleBoxClick}
          style={{
            padding: '4rem 2rem',
            textAlign: 'center',
            cursor: isUploading ? 'default' : 'pointer',
            border: isHovered && !isUploading
              ? '1px solid var(--neon-blue)'
              : status === 'done'
                ? '1px solid var(--neon-cyan)'
                : status === 'error'
                  ? '1px solid var(--neon-error, #ff3366)'
                  : '1px solid var(--glass-border)',
            transition: 'border 0.3s',
            position: 'relative',
            minHeight: '280px',
            display: 'flex', alignItems: 'center', justifyContent: 'center'
          }}
        >
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleFileChange}
            accept=".pdf,.doc,.docx,.ppt,.pptx,.txt"
            style={{ display: 'none' }}
          />

          <AnimatePresence mode="wait">

            {/* Idle */}
            {status === 'idle' && (
              <motion.div key="idle" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
                <div style={{
                  background: 'rgba(0,210,255,0.1)', width: '80px', height: '80px',
                  borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center',
                  margin: '0 auto 1.5rem'
                }}>
                  <UploadCloud size={40} color="var(--neon-blue)" />
                </div>
                <h3 style={{ fontSize: '1.4rem', marginBottom: '0.5rem' }}>Drag & Drop Document</h3>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>Supports PDF, TXT, DOCX</p>
                <div style={{ marginTop: '2rem' }}>
                  <motion.div animate={isHovered ? { y: [0, -5, 0] } : {}} transition={{ repeat: Infinity, duration: 1.5 }}>
                    <File size={24} color={isHovered ? 'var(--neon-cyan)' : 'var(--text-muted)'} />
                  </motion.div>
                </div>
              </motion.div>
            )}

            {/* Processing */}
            {status === 'processing' && (
              <motion.div
                key="processing"
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0 }}
                style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}
              >
                <motion.div
                  animate={{ rotate: 360 }}
                  transition={{ duration: 2, repeat: Infinity, ease: 'linear' }}
                  style={{ marginBottom: '1rem' }}
                >
                  <Cpu size={50} color="var(--neon-violet)" />
                </motion.div>
                <h3 style={{ fontSize: '1.3rem', color: 'var(--neon-violet)' }} className="text-neon">
                  Pipeline Executing...
                </h3>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.82rem', marginTop: '0.6rem', maxWidth: '240px' }}>
                  {statusMessage || `Processing... (Job: ${jobId?.substring(0, 6)}...)`}
                </p>
                <div style={{ display: 'flex', gap: '4px', marginTop: '1.5rem' }}>
                  {[...Array(6)].map((_, i) => (
                    <motion.div
                      key={i}
                      animate={{ height: ['8px', '36px', '8px'] }}
                      transition={{ duration: 0.7, repeat: Infinity, delay: i * 0.1 }}
                      style={{ width: '5px', background: 'var(--neon-cyan)', borderRadius: '3px' }}
                    />
                  ))}
                </div>
              </motion.div>
            )}

            {/* Done */}
            {status === 'done' && (
              <motion.div
                key="done"
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}
              >
                <CheckCircle size={50} color="#00ffcc" style={{ marginBottom: '1rem' }} />
                <h3 style={{ fontSize: '1.4rem', color: '#00ffcc' }}>Generation Complete!</h3>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', marginTop: '0.4rem' }}>
                  {statusMessage}
                </p>
                <p style={{ color: 'var(--neon-cyan)', fontSize: '0.8rem', marginTop: '0.5rem' }}>
                  Γåô Scroll down to watch your video
                </p>
                <button
                  onClick={reset}
                  style={{
                    marginTop: '1.2rem', padding: '8px 20px',
                    background: 'transparent', border: '1px solid #00ffcc',
                    color: '#00ffcc', borderRadius: '20px', cursor: 'pointer', fontSize: '0.9rem'
                  }}
                >
                  Generate Another
                </button>
              </motion.div>
            )}

            {/* Error */}
            {status === 'error' && (
              <motion.div
                key="error"
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}
              >
                <AlertCircle size={50} color="#ff3366" style={{ marginBottom: '1rem' }} />
                <h3 style={{ fontSize: '1.4rem', color: '#ff3366' }}>Generation Failed</h3>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', marginTop: '0.5rem', wordBreak: 'break-word', maxWidth: '260px' }}>
                  {errorMsg}
                </p>
                <button
                  onClick={reset}
                  style={{
                    marginTop: '1.2rem', padding: '8px 20px',
                    background: 'transparent', border: '1px solid #ff3366',
                    color: '#ff3366', borderRadius: '20px', cursor: 'pointer', fontSize: '0.9rem'
                  }}
                >
                  Try Again
                </button>
              </motion.div>
            )}

          </AnimatePresence>
        </motion.div>

        {/* ΓöÇΓöÇ Modal Overlay ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇ */}
        <AnimatePresence>
          {showModal && (
            <motion.div 
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              style={{
                position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
                background: 'rgba(5, 11, 20, 0.85)', backdropFilter: 'blur(8px)',
                zIndex: 1000, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: '20px'
              }}
            >
              <motion.div 
                initial={{ scale: 0.9, y: 20 }}
                animate={{ scale: 1, y: 0 }}
                exit={{ scale: 0.9, y: 20 }}
                className="glass-panel"
                style={{
                  padding: '2.5rem', width: '100%', maxWidth: '450px',
                  border: '1px solid var(--neon-cyan)', boxShadow: '0 0 30px rgba(0,255,204,0.1)'
                }}
              >
                <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                  <div style={{ 
                    width: '60px', height: '60px', borderRadius: '50%', background: 'rgba(0,210,255,0.1)',
                    display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 1rem'
                  }}>
                    <Cpu size={30} color="var(--neon-cyan)" />
                  </div>
                  <h3 style={{ fontSize: '1.5rem', color: '#fff' }}>Generation Parameters</h3>
                  <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', marginTop: '0.5rem' }}>
                    Configure the knowledge assessment for <br/>
                    <span style={{ color: 'var(--neon-cyan)' }}>{pendingFile?.name}</span>
                  </p>
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem', marginBottom: '2rem' }}>
                  <div>
                    <label style={{ display: 'block', color: 'var(--text-muted)', fontSize: '0.8rem', marginBottom: '0.5rem' }}>MCQs</label>
                    <input 
                      type="number" min="0" max="10" value={numMcqs}
                      onChange={e => setNumMcqs(e.target.value)}
                      style={{
                        width: '100%', padding: '12px', background: 'rgba(0,0,0,0.3)',
                        border: '1px solid var(--glass-border)', borderRadius: '8px', color: '#fff', textAlign: 'center'
                      }}
                    />
                  </div>
                  <div>
                    <label style={{ display: 'block', color: 'var(--text-muted)', fontSize: '0.8rem', marginBottom: '0.5rem' }}>Short Ans</label>
                    <input 
                      type="number" min="0" max="10" value={numShorts}
                      onChange={e => setNumShorts(e.target.value)}
                      style={{
                        width: '100%', padding: '12px', background: 'rgba(0,0,0,0.3)',
                        border: '1px solid var(--glass-border)', borderRadius: '8px', color: '#fff', textAlign: 'center'
                      }}
                    />
                  </div>
                  <div style={{ gridColumn: 'span 2' }}>
                    <label style={{ display: 'block', color: 'var(--text-muted)', fontSize: '0.8rem', marginBottom: '0.5rem' }}>Audio Language</label>
                    <select 
                      value={audioLanguage}
                      onChange={e => setAudioLanguage(e.target.value)}
                      style={{
                        width: '100%', padding: '12px', background: 'rgba(0,0,0,0.3)',
                        border: '1px solid var(--glass-border)', borderRadius: '8px', color: '#fff'
                      }}
                    >
                      <option value="english" style={{ color: '#000' }}>English</option>
                      <option value="hinglish" style={{ color: '#000' }}>Hinglish (Roman Script)</option>
                      <option value="hindi" style={{ color: '#000' }}>Hindi (Devanagari)</option>
                    </select>
                  </div>
                </div>

                <div style={{ display: 'flex', gap: '1rem' }}>
                  <button 
                    onClick={() => { setShowModal(false); setPendingFile(null); }}
                    style={{
                      flex: 1, padding: '12px', background: 'transparent',
                      border: '1px solid var(--glass-border)', color: 'var(--text-muted)',
                      borderRadius: '8px', cursor: 'pointer'
                    }}
                  >
                    Abort
                  </button>
                  <button 
                    onClick={startGeneration}
                    className="btn-primary"
                    style={{ flex: 1, padding: '12px', borderRadius: '8px' }}
                  >
                    Prime Pipeline
                  </button>
                </div>
              </motion.div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* ΓöÇΓöÇ Topic Input ΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇΓöÇ */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <div className="glass-panel" style={{ padding: '2rem' }}>
            <h3 style={{ marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
              <Search size={20} color="var(--neon-cyan)" /> Target Concept
            </h3>
            <div style={{ position: 'relative' }}>
              <input
                type="text"
                placeholder="What should the AI focus on?"
                style={{
                  width: '100%', padding: '16px 20px',
                  background: 'rgba(0,0,0,0.4)',
                  border: '1px solid var(--glass-border)',
                  borderRadius: '12px', color: '#fff', fontSize: '1rem',
                  outline: 'none', transition: 'all 0.3s'
                }}
                onFocus={e => {
                  e.target.style.borderColor = 'var(--neon-cyan)';
                  e.target.style.boxShadow = '0 0 15px rgba(0,255,204,0.2)';
                }}
                onBlur={e => {
                  e.target.style.borderColor = 'var(--glass-border)';
                  e.target.style.boxShadow = 'none';
                }}
              />
            </div>

            <div style={{ paddingTop: '1.5rem' }}>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', marginBottom: '1rem' }}>
                AI Suggested Angles:
              </p>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '10px' }}>
                {['History of Neural Nets', 'Backpropagation Deep Dive', 'Transformer Architecture'].map((topic, i) => (
                  <motion.span
                    key={i}
                    whileHover={{ scale: 1.05, background: 'rgba(138,43,226,0.2)', borderColor: 'var(--neon-violet)' }}
                    style={{
                      padding: '8px 16px', background: 'var(--glass-bg)',
                      border: '1px solid var(--glass-border)', borderRadius: '20px',
                      fontSize: '0.85rem', cursor: 'pointer', transition: 'all 0.2s'
                    }}
                  >
                    {topic}
                  </motion.span>
                ))}
              </div>
            </div>
          </div>
        </div>

      </div>
    </section>
  );
};

export default UploadSection;
