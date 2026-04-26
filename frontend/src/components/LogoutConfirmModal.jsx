import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ShieldAlert, Power, X } from 'lucide-react';

const LogoutConfirmModal = ({ isOpen, onConfirm, onCancel }) => {
  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.3 }}
          style={{
            position: 'fixed',
            inset: 0,
            zIndex: 9998,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            background: 'rgba(5, 11, 20, 0.85)',
            backdropFilter: 'blur(12px)',
          }}
          onClick={onCancel}
        >
          <motion.div
            initial={{ scale: 0.8, opacity: 0, y: 30 }}
            animate={{ scale: 1, opacity: 1, y: 0 }}
            exit={{ scale: 0.8, opacity: 0, y: 30 }}
            transition={{ duration: 0.4, ease: [0.22, 1, 0.36, 1] }}
            onClick={(e) => e.stopPropagation()}
            style={{
              width: '90%',
              maxWidth: '440px',
              borderRadius: '24px',
              border: '1px solid rgba(255, 68, 68, 0.3)',
              background: 'linear-gradient(145deg, rgba(15, 25, 40, 0.95), rgba(10, 15, 30, 0.98))',
              boxShadow: '0 0 60px rgba(255, 68, 68, 0.15), 0 20px 60px rgba(0, 0, 0, 0.5)',
              padding: '2.5rem 2rem',
              position: 'relative',
              overflow: 'hidden',
              fontFamily: "'JetBrains Mono', 'Space Grotesk', monospace",
            }}
          >
            {/* Background glow effect */}
            <div style={{
              position: 'absolute',
              top: '-50%',
              left: '50%',
              transform: 'translateX(-50%)',
              width: '300px',
              height: '300px',
              background: 'radial-gradient(circle, rgba(255, 68, 68, 0.08) 0%, transparent 70%)',
              pointerEvents: 'none',
            }} />

            {/* Scanline effect */}
            <div className="scanline" style={{ height: '100%', opacity: 0.05, position: 'absolute', inset: 0, pointerEvents: 'none' }} />

            {/* Close button */}
            <motion.button
              whileHover={{ scale: 1.1, rotate: 90 }}
              whileTap={{ scale: 0.9 }}
              onClick={onCancel}
              style={{
                position: 'absolute',
                top: '16px',
                right: '16px',
                background: 'rgba(255, 255, 255, 0.05)',
                border: '1px solid rgba(255, 255, 255, 0.1)',
                borderRadius: '50%',
                width: '36px',
                height: '36px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                cursor: 'pointer',
                color: 'var(--text-muted)',
                transition: 'all 0.3s',
              }}
            >
              <X size={18} />
            </motion.button>

            {/* Warning icon */}
            <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '1.5rem' }}>
              <motion.div
                animate={{
                  boxShadow: [
                    '0 0 20px rgba(255, 68, 68, 0.3)',
                    '0 0 40px rgba(255, 68, 68, 0.5)',
                    '0 0 20px rgba(255, 68, 68, 0.3)',
                  ],
                }}
                transition={{ duration: 2, repeat: Infinity }}
                style={{
                  width: '72px',
                  height: '72px',
                  borderRadius: '50%',
                  border: '2px solid rgba(255, 68, 68, 0.5)',
                  background: 'rgba(255, 68, 68, 0.08)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                }}
              >
                <ShieldAlert size={32} color="#FF4444" />
              </motion.div>
            </div>

            {/* Title */}
            <h3 style={{
              textAlign: 'center',
              fontSize: '1.3rem',
              fontWeight: 700,
              letterSpacing: '2px',
              color: '#FF4444',
              marginBottom: '0.75rem',
              textTransform: 'uppercase',
            }}>
              ⚠ CRITICAL WARNING
            </h3>

            {/* Message */}
            <p style={{
              textAlign: 'center',
              color: 'var(--text-muted)',
              fontSize: '0.9rem',
              lineHeight: '1.6',
              marginBottom: '2rem',
              letterSpacing: '0.5px',
            }}>
              You are about to terminate your secure session.
              <br />
              All active connections will be severed and local data will be purged.
            </p>

            {/* Divider */}
            <div style={{
              height: '1px',
              background: 'linear-gradient(90deg, transparent, rgba(255, 68, 68, 0.3), transparent)',
              marginBottom: '1.5rem',
            }} />

            {/* Buttons */}
            <div style={{ display: 'flex', gap: '12px' }}>
              <motion.button
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                onClick={onCancel}
                style={{
                  flex: 1,
                  padding: '14px 20px',
                  borderRadius: '12px',
                  border: '1px solid var(--glass-border)',
                  background: 'rgba(255, 255, 255, 0.05)',
                  color: 'var(--text-muted)',
                  fontSize: '0.85rem',
                  fontWeight: 600,
                  letterSpacing: '1px',
                  cursor: 'pointer',
                  transition: 'all 0.3s',
                  fontFamily: "'JetBrains Mono', 'Space Grotesk', monospace",
                }}
                onMouseOver={(e) => {
                  e.currentTarget.style.background = 'rgba(255, 255, 255, 0.1)';
                  e.currentTarget.style.borderColor = 'rgba(255, 255, 255, 0.2)';
                }}
                onMouseOut={(e) => {
                  e.currentTarget.style.background = 'rgba(255, 255, 255, 0.05)';
                  e.currentTarget.style.borderColor = 'var(--glass-border)';
                }}
              >
                ABORT
              </motion.button>

              <motion.button
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                onClick={onConfirm}
                style={{
                  flex: 1,
                  padding: '14px 20px',
                  borderRadius: '12px',
                  border: '1px solid rgba(255, 68, 68, 0.4)',
                  background: 'linear-gradient(135deg, rgba(255, 68, 68, 0.15), rgba(255, 68, 68, 0.25))',
                  color: '#FF4444',
                  fontSize: '0.85rem',
                  fontWeight: 700,
                  letterSpacing: '1px',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  gap: '8px',
                  transition: 'all 0.3s',
                  fontFamily: "'JetBrains Mono', 'Space Grotesk', monospace",
                }}
                onMouseOver={(e) => {
                  e.currentTarget.style.background = 'linear-gradient(135deg, rgba(255, 68, 68, 0.25), rgba(255, 68, 68, 0.4))';
                  e.currentTarget.style.boxShadow = '0 0 20px rgba(255, 68, 68, 0.3)';
                }}
                onMouseOut={(e) => {
                  e.currentTarget.style.background = 'linear-gradient(135deg, rgba(255, 68, 68, 0.15), rgba(255, 68, 68, 0.25))';
                  e.currentTarget.style.boxShadow = 'none';
                }}
              >
                <Power size={16} />
                TERMINATE
              </motion.button>
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default LogoutConfirmModal;
