import React from 'react';
import { motion } from 'framer-motion';
import { FileText, Play, Clapperboard, Sparkles, Cpu, ArrowRight } from 'lucide-react';

const Hero = () => {
  return (
    <section style={{ 
      minHeight: '80vh', 
      display: 'flex', 
      flexDirection: 'column', 
      alignItems: 'center', 
      justifyContent: 'center',
      position: 'relative',
      textAlign: 'center',
      padding: '6rem 0'
    }}>
      {/* Abstract Background Orbs */}
      <motion.div 
        animate={{ 
          scale: [1, 1.1, 1],
          opacity: [0.2, 0.3, 0.2],
          x: [0, 30, 0],
          y: [0, -20, 0]
        }}
        transition={{ duration: 12, repeat: Infinity, ease: "easeInOut" }}
        style={{
          position: 'absolute', top: '10%', left: '15%',
          width: '500px', height: '500px',
          background: 'radial-gradient(circle, var(--neon-blue) 0%, transparent 70%)',
          filter: 'blur(100px)',
          borderRadius: '50%', zIndex: -1
        }}
      />
      <motion.div 
        animate={{ 
          scale: [1, 1.2, 1],
          opacity: [0.15, 0.25, 0.15],
          x: [0, -40, 0],
          y: [0, 30, 0]
        }}
        transition={{ duration: 15, repeat: Infinity, ease: "easeInOut", delay: 1 }}
        style={{
          position: 'absolute', top: '20%', right: '10%',
          width: '600px', height: '600px',
          background: 'radial-gradient(circle, var(--neon-violet) 0%, transparent 70%)',
          filter: 'blur(120px)',
          borderRadius: '50%', zIndex: -1
        }}
      />

      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1, ease: [0.22, 1, 0.36, 1] }}
      >
        <motion.div 
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.2 }}
          style={{ 
            display: 'inline-flex', alignItems: 'center', gap: '8px', 
            padding: '8px 20px', background: 'hsla(var(--neon-cyan-h), 100%, 50%, 0.05)', 
            border: '1px solid hsla(var(--neon-cyan-h), 100%, 50%, 0.2)', 
            borderRadius: '100px', marginBottom: '2.5rem',
            boxShadow: '0 0 20px hsla(var(--neon-cyan-h), 100%, 50%, 0.05)'
          }}
        >
          <Sparkles size={16} color="var(--neon-cyan)" />
          <span style={{ color: 'var(--neon-cyan)', fontSize: '0.75rem', fontWeight: 800, letterSpacing: '2px' }}>
            NEXUS MULTI-AGENT ARCHITECTURE ACTIVATED
          </span>
        </motion.div>
        
        <h1 style={{ 
          fontSize: 'clamp(3.5rem, 8vw, 6.5rem)', 
          lineHeight: 1, 
          marginBottom: '2rem',
          maxWidth: '1100px',
          marginInline: 'auto',
          fontWeight: 800
        }}>
          Transform Data into <br />
          <span className="text-gradient">Cinematic Intelligence</span>
        </h1>
        
        <p style={{ 
          fontSize: '1.25rem', 
          color: 'var(--text-muted)', 
          maxWidth: '650px', 
          margin: '0 auto 4rem auto',
          lineHeight: 1.6,
          fontWeight: 400
        }}>
          Powered by the NEXUS Director Agent & Manim synthesis engine. Upload any document and watch our autonomous pipeline weave it into an engaging visual sequence.
        </p>

        <div style={{ display: 'flex', gap: '1.5rem', justifyContent: 'center' }}>
          <motion.button 
            whileHover={{ scale: 1.05, boxShadow: '0 0 40px hsla(var(--neon-cyan-h), 100%, 50%, 0.3)' }}
            whileTap={{ scale: 0.95 }}
            onClick={() => {
              const el = document.getElementById('upload');
              if (el) el.scrollIntoView({ behavior: 'smooth' });
            }}
            className="btn-primary" 
            style={{ padding: '18px 40px', fontSize: '1.1rem' }}
          >
            <Play size={20} fill="currentColor" />
            INITIALIZE PROTOCOL
          </motion.button>
          
          <motion.button 
            whileHover={{ scale: 1.05, background: 'var(--surface-1)' }}
            whileTap={{ scale: 0.95 }}
            onClick={() => {
              const el = document.getElementById('pipeline');
              if (el) el.scrollIntoView({ behavior: 'smooth' });
            }}
            className="btn-secondary" 
            style={{ padding: '18px 40px', fontSize: '1.1rem', display: 'flex', alignItems: 'center', gap: '12px' }}
          >
            VIEW ARCHITECTURE
            <ArrowRight size={20} />
          </motion.button>
        </div>

        {/* Status Indicators */}
        <div style={{ 
          marginTop: '6rem', display: 'flex', gap: '4rem', justifyContent: 'center',
          color: 'var(--text-muted)', fontSize: '0.8rem', fontWeight: 700, letterSpacing: '2px'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: 'var(--neon-cyan)', boxShadow: '0 0 10px var(--neon-cyan)' }} />
            RAG PIPELINE: ONLINE
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: 'var(--neon-violet)', boxShadow: '0 0 10px var(--neon-violet)' }} />
            SYNTHESIS ENGINE: READY
          </div>
        </div>
      </motion.div>
    </section>
  );
};

export default Hero;

