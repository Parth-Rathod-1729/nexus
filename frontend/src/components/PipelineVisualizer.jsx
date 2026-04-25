import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';

const nodes = [
  { id: 1, label: 'PDF Parsing', color: 'var(--neon-cyan)' },
  { id: 2, label: 'RAG Retrieval', color: 'var(--neon-blue)' },
  { id: 3, label: 'Director Agent', color: 'var(--neon-violet)' },
  { id: 4, label: 'Scene JSON', color: '#ff00ff' },
  { id: 5, label: 'Agent Mesh', color: 'var(--neon-cyan)' },
  { id: 6, label: 'Manim Engine', color: 'var(--neon-blue)' },
  { id: 7, label: 'Final Output', color: 'var(--text-main)' }
];

const PipelineVisualizer = () => {
  const [activeNode, setActiveNode] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setActiveNode((prev) => (prev + 1) % (nodes.length + 1));
    }, 1500);
    return () => clearInterval(interval);
  }, []);

  return (
    <section id="pipeline" style={{ scrollMarginTop: '120px' }}>
      <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
        <h2 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>Autonomous <span className="text-gradient">Agent Pipeline</span></h2>
        <p style={{ color: 'var(--text-muted)' }}>Watch the neural handoff between specialized AI agents.</p>
      </div>

      <div className="glass-panel" style={{ padding: '4rem 2rem', overflowX: 'auto' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', minWidth: '900px', position: 'relative' }}>
          
          {/* Animated Connector Line */}
          <div style={{
            position: 'absolute',
            top: '50%',
            left: '50px',
            right: '50px',
            height: '2px',
            background: 'var(--glass-border)',
            zIndex: 0,
            transform: 'translateY(-50%)'
          }}>
            <motion.div 
              initial={{ width: '0%' }}
              animate={{ width: `${(activeNode / (nodes.length - 1)) * 100}%` }}
              transition={{ duration: 0.5 }}
              style={{
                height: '100%',
                background: 'linear-gradient(90deg, var(--neon-cyan), var(--neon-violet))',
                boxShadow: '0 0 10px var(--neon-cyan)'
              }}
            />
          </div>

          {/* Nodes */}
          {nodes.map((node, i) => {
            const isActive = i <= activeNode;
            const isCurrent = i === activeNode;
            
            return (
              <div key={node.id} style={{ 
                position: 'relative', zIndex: 1, 
                display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1rem' 
              }}>
                <motion.div 
                  animate={{
                    scale: isCurrent ? 1.3 : 1,
                    backgroundColor: isActive ? node.color : 'var(--bg-color)',
                    borderColor: isActive ? node.color : 'var(--glass-border)',
                    boxShadow: isCurrent ? `0 0 20px ${node.color}, inset 0 0 10px rgba(0,0,0,0.5)` : 'none'
                  }}
                  transition={{ duration: 0.3 }}
                  style={{
                    width: '30px', height: '30px',
                    borderRadius: '50%',
                    border: '2px solid',
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    background: 'var(--bg-color)',
                    transition: 'all 0.3s ease'
                  }}
                >
                  {isActive && <div style={{ width: '10px', height: '10px', background: '#fff', borderRadius: '50%' }} />}
                </motion.div>
                
                <motion.span 
                  animate={{
                    color: isActive ? '#fff' : 'var(--text-muted)',
                    textShadow: isCurrent ? `0 0 10px ${node.color}` : 'none'
                  }}
                  style={{ 
                    fontSize: '0.85rem', 
                    fontWeight: isCurrent ? 700 : 500,
                    width: '100px',
                    textAlign: 'center'
                  }}
                >
                  {node.label}
                </motion.span>
                
                {/* Floating Particle Flow if Current */}
                {isCurrent && i < nodes.length - 1 && (
                  <motion.div
                    animate={{ x: [0, 100], opacity: [0, 1, 0] }}
                    transition={{ duration: 1, repeat: Infinity }}
                    style={{
                      position: 'absolute',
                      top: '13px',
                      left: '30px',
                      width: '6px', height: '6px',
                      borderRadius: '50%',
                      background: '#fff',
                      boxShadow: `0 0 10px ${node.color}`
                    }}
                  />
                )}
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
};

export default PipelineVisualizer;
