import React from 'react';
import { motion } from 'framer-motion';

const AuthBackground = () => {
  return (
    <div style={{
      position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
      zIndex: -1, overflow: 'hidden',
      background: 'var(--bg-gradient)'
    }}>
      {/* Floating Particles */}
      {[...Array(20)].map((_, i) => (
        <motion.div
          key={i}
          animate={{
            y: ['0vh', '-100vh'],
            x: [Math.random() * 100 - 50, Math.random() * 100 - 50],
            opacity: [0, 0.5, 0]
          }}
          transition={{
            duration: Math.random() * 10 + 10,
            repeat: Infinity,
            ease: 'linear',
            delay: Math.random() * 5
          }}
          style={{
            position: 'absolute',
            bottom: '-10%',
            left: `${Math.random() * 100}%`,
            width: `${Math.random() * 4 + 2}px`,
            height: `${Math.random() * 4 + 2}px`,
            background: i % 2 === 0 ? 'var(--neon-cyan)' : 'var(--neon-violet)',
            borderRadius: '50%',
            boxShadow: `0 0 10px ${i % 2 === 0 ? 'var(--neon-cyan)' : 'var(--neon-violet)'}`
          }}
        />
      ))}
      
      {/* Giant Glowing Orbs */}
      <motion.div 
        animate={{ scale: [1, 1.1, 1], opacity: [0.1, 0.2, 0.1] }}
        transition={{ duration: 8, repeat: Infinity, ease: 'easeInOut' }}
        style={{
          position: 'absolute', top: '10%', left: '10%',
          width: '500px', height: '500px',
          background: 'var(--neon-blue)',
          filter: 'blur(200px)', borderRadius: '50%'
        }}
      />
      <motion.div 
        animate={{ scale: [1, 1.2, 1], opacity: [0.1, 0.3, 0.1] }}
        transition={{ duration: 10, repeat: Infinity, ease: 'easeInOut', delay: 2 }}
        style={{
          position: 'absolute', bottom: '10%', right: '10%',
          width: '600px', height: '600px',
          background: 'var(--neon-violet)',
          filter: 'blur(250px)', borderRadius: '50%'
        }}
      />
      
      {/* Grid Overlay */}
      <div style={{
        position: 'absolute', top: 0, left: 0, right: 0, bottom: 0,
        backgroundImage: 'linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px)',
        backgroundSize: '40px 40px',
        opacity: 0.5
      }} />
    </div>
  );
};

export default AuthBackground;
