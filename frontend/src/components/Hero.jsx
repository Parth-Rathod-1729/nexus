import React from 'react';
import { motion } from 'framer-motion';
import { FileText, Play, Clapperboard, Sparkles, Cpu } from 'lucide-react';

const Hero = () => {
  return (
    <section style={{ 
      minHeight: '85vh', 
      display: 'flex', 
      flexDirection: 'column', 
      alignItems: 'center', 
      justifyContent: 'center',
      position: 'relative',
      textAlign: 'center',
      padding: '4rem 0'
    }}>
      {/* Abstract Background Orbs */}
      <motion.div 
        animate={{ 
          scale: [1, 1.2, 1],
          opacity: [0.3, 0.5, 0.3],
          x: [0, 50, 0],
          y: [0, -30, 0]
        }}
        transition={{ duration: 8, repeat: Infinity, ease: "easeInOut" }}
        style={{
          position: 'absolute', top: '10%', left: '20%',
          width: '300px', height: '300px',
          background: 'var(--neon-blue)',
          filter: 'blur(120px)',
          borderRadius: '50%', zIndex: -1
        }}
      />
      <motion.div 
        animate={{ 
          scale: [1, 1.5, 1],
          opacity: [0.2, 0.4, 0.2],
          x: [0, -60, 0],
          y: [0, 40, 0]
        }}
        transition={{ duration: 10, repeat: Infinity, ease: "easeInOut", delay: 1 }}
        style={{
          position: 'absolute', top: '30%', right: '15%',
          width: '400px', height: '400px',
          background: 'var(--neon-violet)',
          filter: 'blur(150px)',
          borderRadius: '50%', zIndex: -1
        }}
      />

      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
      >
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', padding: '6px 16px', background: 'rgba(0, 210, 255, 0.1)', border: '1px solid var(--neon-blue)', borderRadius: '20px', marginBottom: '2rem' }}>
          <Sparkles size={16} color="var(--neon-blue)" />
          <span style={{ color: 'var(--neon-blue)', fontSize: '0.85rem', fontWeight: 600, letterSpacing: '1px' }}>THE GOOD ULTRON MULTI-AGENT SYSTEM ACTIVATED</span>
        </div>
        
        <h1 style={{ 
          fontSize: 'clamp(3rem, 6vw, 5.5rem)', 
          lineHeight: 1.1, 
          marginBottom: '1.5rem',
          maxWidth: '1000px',
          margin: '0 auto 1.5rem auto'
        }}>
          Transform PDFs into <br />
          <span className="text-gradient">Cinematic Learning</span>
        </h1>
        
        <p style={{ 
          fontSize: '1.2rem', 
          color: 'var(--text-muted)', 
          maxWidth: '600px', 
          margin: '0 auto 3rem auto',
          lineHeight: 1.6
        }}>
          Powered by our Director Agent & Manim visual engine. Upload any document and watch our autonomous AI pipeline weave it into an engaging sequence.
        </p>

        {/* Dynamic Pipeline Preview */}
        <motion.div 
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '1rem',
            margin: '0 auto 3rem auto',
            background: 'var(--glass-bg)',
            padding: '1rem 2rem',
            borderRadius: '50px',
            border: '1px solid var(--glass-border)'
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--text-muted)' }}>
            <FileText size={18} /> <span>PDF</span>
          </div>
          <motion.div animate={{ opacity: [0.3, 1, 0.3] }} transition={{ duration: 2, repeat: Infinity }}>→</motion.div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--neon-blue)' }}>
            <Cpu size={18} /> <span>AI Agents</span>
          </div>
          <motion.div animate={{ opacity: [0.3, 1, 0.3] }} transition={{ duration: 2, repeat: Infinity, delay: 0.6 }}>→</motion.div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--neon-violet)' }}>
            <Clapperboard size={18} /> <span>Animation Engine</span>
          </div>
        </motion.div>

        <button className="btn-primary" style={{ padding: '16px 36px', fontSize: '1.1rem' }}>
          <Play size={20} fill="var(--neon-cyan)" />
          Start Director Protocol
        </button>
      </motion.div>
    </section>
  );
};

export default Hero;
