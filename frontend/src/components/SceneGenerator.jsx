import React from 'react';
import { motion } from 'framer-motion';
import { Layers, Volume2, Code } from 'lucide-react';

const scenes = [
  { id: 1, text: "Introduction to Neural Networks.", duration: "2s", code: "Text('Neural Nets')" },
  { id: 2, text: "Wait, what's a perceptron?", duration: "3s", code: "Circle(color=BLUE)" },
  { id: 3, text: "It's literally just a mathematical function.", duration: "4s", code: "MathTex('y = mx + b')" },
  { id: 4, text: "Zooming out, we see the layers.", duration: "5s", code: "VGroup(*layers).arrange()" },
];

const containerVariants = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.3 }
  }
};

const itemVariants = {
  hidden: { opacity: 0, x: -50 },
  show: { opacity: 1, x: 0, transition: { type: 'spring', stiffness: 50 } }
};

const Waveform = () => (
  <div style={{ display: 'flex', gap: '3px', alignItems: 'center', height: '20px' }}>
    {[...Array(12)].map((_, i) => (
      <motion.div
        key={i}
        animate={{ height: ['4px', `${Math.random() * 16 + 4}px`, '4px'] }}
        transition={{ duration: 0.5 + Math.random() * 0.5, repeat: Infinity, repeatType: 'reverse' }}
        style={{ width: '3px', background: 'var(--neon-blue)', borderRadius: '2px' }}
      />
    ))}
  </div>
);

const SceneGenerator = () => {
  return (
    <section id="generator" style={{ scrollMarginTop: '120px' }}>
      <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
        <h2 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>Director Agent <span style={{ color: 'var(--neon-violet)' }}>Timeline</span></h2>
        <p style={{ color: 'var(--text-muted)' }}>Dynamically generated scene blocks with synchronized TTS and Manim code.</p>
      </div>

      <motion.div 
        variants={containerVariants} 
        initial="hidden" 
        whileInView="show" 
        viewport={{ once: true, margin: "-100px" }}
        style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem', maxWidth: '800px', margin: '0 auto' }}
      >
        {scenes.map((scene, index) => (
          <motion.div 
            key={scene.id} 
            variants={itemVariants}
            className="glass-panel"
            style={{ 
              display: 'flex', 
              padding: '1.5rem', 
              gap: '2rem', 
              alignItems: 'center',
              borderLeft: `4px solid ${index % 2 === 0 ? 'var(--neon-blue)' : 'var(--neon-cyan)'}`
            }}
          >
            {/* Scene Index */}
            <div style={{ 
              width: '50px', height: '50px', 
              borderRadius: '12px', 
              background: 'rgba(255,255,255,0.05)',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontWeight: 'bold', fontSize: '1.2rem',
              color: 'var(--text-muted)'
            }}>
              {scene.id}
            </div>

            {/* Content */}
            <div style={{ flex: 1 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
                <span style={{ fontSize: '0.85rem', color: 'var(--neon-violet)', textTransform: 'uppercase', letterSpacing: '1px' }}>
                  Scene Duration: {scene.duration}
                </span>
                <span style={{ display: 'flex', gap: '6px', alignItems: 'center', fontSize: '0.85rem', color: 'var(--text-muted)' }}>
                  <Volume2 size={14} /> TTS Active
                </span>
              </div>
              <p style={{ fontSize: '1.1rem', marginBottom: '12px' }}>"{scene.text}"</p>
              
              <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                <Waveform />
              </div>
            </div>

            {/* Manim Code Preview */}
            <div style={{ 
              background: '#0d1117', 
              padding: '1rem', 
              borderRadius: '8px',
              border: '1px solid var(--glass-border)',
              width: '200px',
              fontFamily: 'monospace',
              fontSize: '0.8rem',
              color: '#58a6ff',
              display: 'flex', flexDirection: 'column', gap: '8px'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px', color: 'var(--text-muted)' }}>
                <Code size={14} /> Manim Output
              </div>
              <div>{scene.code}</div>
            </div>
          </motion.div>
        ))}
      </motion.div>
    </section>
  );
};

export default SceneGenerator;
