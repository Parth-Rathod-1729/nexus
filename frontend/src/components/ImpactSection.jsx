import React from 'react';
import { motion } from 'framer-motion';
import { Zap, Brain, Edit3 } from 'lucide-react';

const stats = [
  { 
    id: 1, 
    value: "90%", 
    label: "Faster Production", 
    desc: "From PDF to render in minutes instead of weeks.",
    icon: <Zap size={30} color="var(--neon-cyan)" />,
    color: "var(--neon-cyan)"
  },
  { 
    id: 2, 
    value: "3x", 
    label: "Higher Retention", 
    desc: "Visual storytelling drastically improves learning outcomes.",
    icon: <Brain size={30} color="var(--neon-violet)" />,
    color: "var(--neon-violet)"
  },
  { 
    id: 3, 
    value: "Zero", 
    label: "Manual Editing", 
    desc: "Autonomous workflow requires zero human intervention.",
    icon: <Edit3 size={30} color="var(--neon-blue)" />,
    color: "var(--neon-blue)"
  }
];

const ImpactSection = () => {
  return (
    <section style={{ paddingBottom: '4rem' }}>
      <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
        <h2 style={{ fontSize: '2.5rem', marginBottom: '1rem' }}>The <span className="text-gradient">Impact</span></h2>
        <p style={{ color: 'var(--text-muted)' }}>Metrics from The Good Ultron execution log.</p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '2rem' }}>
        {stats.map((stat, i) => (
          <motion.div
            key={stat.id}
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: i * 0.2 }}
            className="glass-panel"
            style={{ padding: '3rem 2rem', textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center' }}
          >
            <div style={{ 
              width: '70px', height: '70px', 
              borderRadius: '50%', 
              background: `rgba(${stat.color === 'var(--neon-cyan)' ? '0, 255, 204' : stat.color === 'var(--neon-violet)' ? '138, 43, 226' : '0, 210, 255'}, 0.1)`,
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              marginBottom: '1.5rem',
              boxShadow: `0 0 20px ${stat.color}40`
            }}>
              {stat.icon}
            </div>
            
            <h3 style={{ fontSize: '3rem', margin: '0', color: '#fff', textShadow: `0 0 15px ${stat.color}` }}>
              {stat.value}
            </h3>
            
            <h4 style={{ fontSize: '1.2rem', color: stat.color, margin: '0.5rem 0 1rem 0' }}>
              {stat.label}
            </h4>
            
            <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', lineHeight: 1.5 }}>
              {stat.desc}
            </p>
          </motion.div>
        ))}
      </div>
    </section>
  );
};

export default ImpactSection;
