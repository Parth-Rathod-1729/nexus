import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Power, ShieldAlert, Database, Lock } from 'lucide-react';

const LogoutOverlay = ({ isOpen }) => {
  const [step, setStep] = useState(0);
  
  const steps = [
    { text: "INITIALIZING DE-AUTHENTICATION SEQUENCE...", icon: <Power size={20} /> },
    { text: "CLEARING LOCAL SESSION CACHE...", icon: <Database size={20} /> },
    { text: "ENCRYPTING TRACE DATA...", icon: <Lock size={20} /> },
    { text: "TERMINATING SECURE CONNECTION...", icon: <ShieldAlert size={20} /> },
    { text: "SESSION TERMINATED. GOODBYE.", icon: null }
  ];

  useEffect(() => {
    if (isOpen) {
      setStep(0);
      const interval = setInterval(() => {
        setStep(prev => (prev < steps.length - 1 ? prev + 1 : prev));
      }, 500);
      return () => clearInterval(interval);
    }
  }, [isOpen]);

  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          style={{
            position: 'fixed',
            inset: 0,
            zIndex: 9999,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            background: 'rgba(5, 11, 20, 0.95)',
            backdropFilter: 'blur(12px)',
            color: 'var(--neon-cyan)',
            fontFamily: "'JetBrains Mono', monospace",
          }}
        >
          {/* Background Effects */}
          <div className="scanline" style={{ height: '100%', opacity: 0.1 }} />
          
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            style={{
              textAlign: 'center',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              gap: '24px',
              padding: '40px',
              borderRadius: '24px',
              border: '1px solid var(--glass-border)',
              background: 'var(--glass-bg)',
              boxShadow: '0 0 50px rgba(0, 255, 204, 0.1)',
              maxWidth: '500px',
              width: '90%'
            }}
          >
            <div style={{ position: 'relative' }}>
              <motion.div
                animate={{ 
                  rotate: 360,
                  scale: [1, 1.1, 1],
                  borderColor: ['var(--neon-cyan)', 'var(--neon-violet)', 'var(--neon-cyan)']
                }}
                transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
                style={{
                  width: '80px',
                  height: '80px',
                  borderRadius: '50%',
                  border: '2px solid var(--neon-cyan)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  boxShadow: '0 0 20px rgba(0, 255, 204, 0.3)'
                }}
              >
                <Power size={32} />
              </motion.div>
              
              <motion.div
                animate={{ opacity: [0, 1, 0] }}
                transition={{ duration: 1.5, repeat: Infinity }}
                style={{
                  position: 'absolute',
                  inset: '-10px',
                  borderRadius: '50%',
                  border: '1px solid var(--neon-cyan)',
                  opacity: 0.5
                }}
              />
            </div>

            <div style={{ width: '100%', display: 'flex', flexDirection: 'column', gap: '12px' }}>
              {steps.map((s, i) => (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, x: -10 }}
                  animate={{ 
                    opacity: i <= step ? 1 : 0.2,
                    x: i <= step ? 0 : -10,
                    color: i === step ? 'var(--neon-cyan)' : i < step ? 'var(--text-muted)' : 'rgba(255,255,255,0.1)'
                  }}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '12px',
                    fontSize: '0.85rem',
                    letterSpacing: '1px'
                  }}
                >
                  {i < step ? (
                    <span style={{ color: 'var(--neon-cyan)' }}>[OK]</span>
                  ) : i === step ? (
                    <motion.span
                      animate={{ opacity: [1, 0, 1] }}
                      transition={{ duration: 0.5, repeat: Infinity }}
                    >
                      {'>'}
                    </motion.span>
                  ) : (
                    <span>[ ]</span>
                  )}
                  <span>{s.text}</span>
                </motion.div>
              ))}
            </div>

            <motion.div
              style={{
                width: '100%',
                height: '2px',
                background: 'rgba(255,255,255,0.1)',
                borderRadius: '2px',
                overflow: 'hidden',
                marginTop: '10px'
              }}
            >
              <motion.div
                initial={{ width: '0%' }}
                animate={{ width: `${((step + 1) / steps.length) * 100}%` }}
                style={{
                  height: '100%',
                  background: 'linear-gradient(90deg, var(--neon-cyan), var(--neon-violet))',
                  boxShadow: '0 0 10px var(--neon-cyan)'
                }}
              />
            </motion.div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default LogoutOverlay;
