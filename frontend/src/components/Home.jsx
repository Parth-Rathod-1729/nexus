import React from 'react';
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { ShieldAlert, User, Cpu, ArrowRight } from 'lucide-react';
import AuthBackground from './AuthBackground';

const containerVariants = {
  initial: { opacity: 0 },
  animate: { 
    opacity: 1,
    transition: { staggerChildren: 0.2, delayChildren: 0.3 }
  }
};

const itemVariants = {
  initial: { opacity: 0, y: 30, filter: 'blur(10px)' },
  animate: { 
    opacity: 1, 
    y: 0, 
    filter: 'blur(0px)',
    transition: { duration: 0.8, ease: [0.22, 1, 0.36, 1] }
  }
};

const Home = () => {
  const navigate = useNavigate();

  return (
    <div style={{ 
      minHeight: '100vh', 
      display: 'flex', 
      alignItems: 'center', 
      justifyContent: 'center', 
      position: 'relative',
      overflow: 'hidden'
    }}>
      <AuthBackground />
      
      {/* Decorative Elements */}
      <motion.div 
        animate={{ 
          scale: [1, 1.2, 1],
          opacity: [0.1, 0.2, 0.1],
          rotate: [0, 90, 0]
        }}
        transition={{ duration: 20, repeat: Infinity, ease: "linear" }}
        style={{
          position: 'absolute',
          width: '600px',
          height: '600px',
          borderRadius: '50%',
          background: 'radial-gradient(circle, var(--neon-blue) 0%, transparent 70%)',
          filter: 'blur(80px)',
          top: '-20%',
          right: '-10%',
          zIndex: 0
        }}
      />

      <motion.div
        variants={containerVariants}
        initial="initial"
        animate="animate"
        className="glass-panel"
        style={{
          width: '90%',
          maxWidth: '540px',
          padding: '4rem 3rem',
          textAlign: 'center',
          zIndex: 1,
          border: '1px solid hsla(var(--neon-cyan-h), 100%, 50%, 0.2)',
          boxShadow: '0 20px 80px hsla(0, 0%, 0%, 0.5)'
        }}
      >
        <div className="scanline" />
        
        <motion.div variants={itemVariants} style={{ display: 'flex', justifyContent: 'center', marginBottom: '2rem' }}>
          <div style={{
            padding: '20px',
            background: 'hsla(var(--neon-cyan-h), 100%, 50%, 0.05)',
            borderRadius: '24px',
            border: '1px solid hsla(var(--neon-cyan-h), 100%, 50%, 0.2)',
            boxShadow: '0 0 40px hsla(var(--neon-cyan-h), 100%, 50%, 0.1)'
          }}>
            <Cpu size={56} color="var(--neon-cyan)" className="text-glow" />
          </div>
        </motion.div>
        
        <motion.h1 variants={itemVariants} style={{ fontSize: '3.5rem', marginBottom: '1rem', fontWeight: 800 }}>
          NEXUS<span className="text-gradient">.SYSTEM</span>
        </motion.h1>
        
        <motion.p variants={itemVariants} style={{ 
          color: 'var(--text-muted)', 
          fontSize: '1.1rem', 
          marginBottom: '3.5rem', 
          lineHeight: '1.6',
          maxWidth: '400px',
          marginInline: 'auto'
        }}>
          Initialize secure uplink to the central intelligence repository. Select your authorization protocol.
        </motion.p>
        
        <motion.div variants={itemVariants} style={{ display: 'flex', flexDirection: 'column', gap: '1.2rem' }}>
          
          <motion.button 
            whileHover={{ scale: 1.02, x: 5 }}
            whileTap={{ scale: 0.98 }}
            onClick={() => navigate('/login')}
            className="btn-primary"
            style={{ width: '100%', justifyContent: 'space-between' }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
              <User size={22} />
              <span>Student Interface</span>
            </div>
            <ArrowRight size={20} />
          </motion.button>

          <motion.button 
            whileHover={{ scale: 1.02, x: 5 }}
            whileTap={{ scale: 0.98 }}
            onClick={() => navigate('/admin/login')}
            className="btn-secondary"
            style={{ 
              width: '100%', 
              display: 'flex', 
              justifyContent: 'space-between',
              alignItems: 'center',
              border: '1px solid hsla(27, 100%, 50%, 0.2)',
              color: '#FFA500'
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
              <ShieldAlert size={22} />
              <span>Admin Terminal</span>
            </div>
            <ArrowRight size={20} />
          </motion.button>

        </motion.div>

        <motion.div variants={itemVariants} style={{ marginTop: '3rem' }}>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem' }}>
            New identity?{' '}
            <span 
              onClick={() => navigate('/register')}
              style={{ 
                color: 'var(--neon-blue)', 
                cursor: 'pointer', 
                fontWeight: 700,
                textDecoration: 'none',
                borderBottom: '1px solid transparent',
                transition: 'border 0.3s'
              }}
              onMouseOver={e => e.target.style.borderBottom = '1px solid var(--neon-blue)'}
              onMouseOut={e => e.target.style.borderBottom = '1px solid transparent'}
            >
              Request Access
            </span>
          </p>
        </motion.div>

      </motion.div>
    </div>
  );
};

export default Home;

