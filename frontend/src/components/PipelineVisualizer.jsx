import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Database, Cpu, Layout, FileJson, Share2, Layers, Video, Zap } from 'lucide-react';

const nodes = [
  { id: 1, label: 'PDF INGESTION', icon: Database, color: 'var(--neon-cyan)' },
  { id: 2, label: 'RAG CONTEXT', icon: Share2, color: 'var(--neon-blue)' },
  { id: 3, label: 'DIRECTOR AGENT', icon: Cpu, color: 'var(--neon-violet)' },
  { id: 4, label: 'SCENE SYNTHESIS', icon: FileJson, color: 'var(--neon-blue)' },
  { id: 5, label: 'AGENT MESH', icon: Layers, color: 'var(--neon-cyan)' },
  { id: 6, label: 'MANIM ENGINE', icon: Video, color: 'var(--neon-violet)' },
  { id: 7, label: 'FINAL DEPLOY', icon: Zap, color: '#fff' }
];

const PipelineVisualizer = () => {
  const [activeNode, setActiveNode] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setActiveNode((prev) => (prev + 1) % nodes.length);
    }, 2500);
    return () => clearInterval(interval);
  }, []);

  return (
    <section id="pipeline" style={{ scrollMarginTop: '120px' }}>
      <div style={{ textAlign: 'center', marginBottom: '5rem' }}>
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          style={{ 
            display: 'inline-flex', alignItems: 'center', gap: '8px', 
            padding: '8px 16px', background: 'hsla(var(--neon-blue-h), 100%, 50%, 0.05)',
            border: '1px solid hsla(var(--neon-blue-h), 100%, 50%, 0.2)', borderRadius: '20px',
            marginBottom: '1rem'
          }}
        >
          <Cpu size={14} color="var(--neon-blue)" />
          <span style={{ color: 'var(--neon-blue)', fontSize: '0.75rem', fontWeight: 800, letterSpacing: '2px' }}>
            MODULE 02: AUTONOMOUS UPLINK
          </span>
        </motion.div>
        <h2 style={{ fontSize: '3rem', marginBottom: '1.2rem', fontWeight: 800 }}>
          Autonomous <span style={{ color: 'var(--neon-cyan)' }}>Agent Pipeline</span>
        </h2>
        <p style={{ color: 'var(--text-muted)', fontSize: '1.1rem', maxWidth: '600px', marginInline: 'auto' }}>
          Visualizing the real-time neural handoff between specialized AI sub-routines.
        </p>
      </div>

      <div className="glass-panel" style={{ padding: '6rem 3rem', overflowX: 'auto' }}>
        <div className="scanline" />
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', minWidth: '1000px', position: 'relative', padding: '0 40px' }}>
          
          {/* Progress Connector */}
          <div style={{
            position: 'absolute', top: '42.5px', left: '80px', right: '80px', height: '2px',
            background: 'var(--glass-border)', zIndex: 0
          }}>
            <motion.div 
              initial={{ width: '0%' }}
              animate={{ width: `${(activeNode / (nodes.length - 1)) * 100}%` }}
              transition={{ duration: 0.8, ease: "easeInOut" }}
              style={{
                height: '100%',
                background: 'linear-gradient(90deg, var(--neon-cyan), var(--neon-blue), var(--neon-violet))',
                boxShadow: '0 0 20px var(--neon-blue)'
              }}
            />
          </div>

          {/* Nodes */}
          {nodes.map((node, i) => {
            const isActive = i <= activeNode;
            const isCurrent = i === activeNode;
            const Icon = node.icon;
            
            return (
              <div key={node.id} style={{ 
                position: 'relative', zIndex: 1, 
                display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1.5rem' 
              }}>
                <motion.div 
                  animate={{
                    scale: isCurrent ? 1.15 : 1,
                    borderColor: isActive ? node.color : 'var(--glass-border)',
                    boxShadow: isCurrent ? `0 0 40px ${node.color}33` : 'none',
                    backgroundColor: 'var(--bg-color)'
                  }}
                  transition={{ duration: 0.5 }}
                  style={{
                    width: '85px', height: '85px',
                    borderRadius: '24px',
                    border: '2px solid',
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    background: 'var(--bg-color)',
                    position: 'relative',
                    zIndex: 2
                  }}
                >
                  <Icon 
                    size={32} 
                    color={isActive ? node.color : 'var(--text-muted)'} 
                    style={{ transition: 'color 0.3s', position: 'relative', zIndex: 3 }}
                    className={isCurrent ? 'text-glow' : ''}
                  />
                  {isCurrent && (
                    <motion.div
                      layoutId="active-ring"
                      style={{
                        position: 'absolute', inset: '-8px', borderRadius: '28px',
                        border: `1px solid ${node.color}`, opacity: 0.3
                      }}
                      animate={{ scale: [1, 1.1, 1] }}
                      transition={{ duration: 2, repeat: Infinity }}
                    />
                  )}
                </motion.div>
                
                <div style={{ textAlign: 'center', width: '120px' }}>
                  <motion.div 
                    animate={{
                      color: isActive ? '#fff' : 'var(--text-muted)',
                      opacity: isActive ? 1 : 0.5
                    }}
                    style={{ 
                      fontSize: '0.7rem', 
                      fontWeight: 800,
                      letterSpacing: '1.5px',
                      marginBottom: '4px'
                    }}
                  >
                    STEP 0{i + 1}
                  </motion.div>
                  <motion.div 
                    animate={{
                      color: isActive ? '#fff' : 'var(--text-muted)',
                      opacity: isActive ? 1 : 0.5
                    }}
                    style={{ 
                      fontSize: '0.85rem', 
                      fontWeight: isCurrent ? 700 : 500
                    }}
                  >
                    {node.label}
                  </motion.div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default PipelineVisualizer;

