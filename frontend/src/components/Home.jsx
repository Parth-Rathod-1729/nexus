import React from 'react';
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { ShieldAlert, User, Cpu } from 'lucide-react';
import AuthBackground from './AuthBackground';

const pageVariants = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0, transition: { duration: 0.8, ease: 'easeOut', staggerChildren: 0.1 } },
  exit: { opacity: 0, y: -20, transition: { duration: 0.5, ease: 'easeIn' } }
};

const itemVariants = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0, transition: { duration: 0.5 } }
};

const Home = () => {
  const navigate = useNavigate();

  return (
    <div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative' }}>
      <AuthBackground />
      
      <motion.div
        variants={pageVariants}
        initial="initial"
        animate="animate"
        exit="exit"
        className="glass-panel"
        style={{
          width: '100%', maxWidth: '600px',
          padding: '4rem 3rem',
          textAlign: 'center',
          border: '1px solid var(--glass-border)',
        }}
      >
        <motion.div variants={itemVariants} style={{ display: 'flex', justifyContent: 'center', marginBottom: '1.5rem' }}>
          <Cpu size={60} color="var(--neon-cyan)" />
        </motion.div>
        
        <motion.h1 variants={itemVariants} style={{ fontSize: '2.5rem', marginBottom: '1rem', letterSpacing: '2px' }}>
          The Good <span style={{ color: 'var(--neon-cyan)' }}>Ultron</span>
        </motion.h1>
        
        <motion.p variants={itemVariants} style={{ color: 'var(--text-muted)', fontSize: '1rem', marginBottom: '3rem', lineHeight: '1.6' }}>
          Welcome to the centralized portal. Please authenticate yourself to access the system interfaces and subroutines.
        </motion.p>
        
        <motion.div variants={itemVariants} style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          
          <button 
            onClick={() => navigate('/login')}
            style={{
              display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '15px',
              padding: '18px 24px', background: 'rgba(0, 210, 255, 0.1)',
              border: '1px solid var(--neon-cyan)', borderRadius: '12px',
              color: 'var(--text-main)', fontSize: '1.1rem', cursor: 'pointer',
              transition: 'all 0.3s', boxShadow: '0 0 15px rgba(0, 255, 204, 0.1)'
            }}
            onMouseOver={(e) => {
              e.currentTarget.style.background = 'rgba(0, 255, 204, 0.2)';
              e.currentTarget.style.boxShadow = '0 0 25px rgba(0, 255, 204, 0.4)';
            }}
            onMouseOut={(e) => {
              e.currentTarget.style.background = 'rgba(0, 210, 255, 0.1)';
              e.currentTarget.style.boxShadow = '0 0 15px rgba(0, 255, 204, 0.1)';
            }}
          >
            <User size={24} color="var(--neon-cyan)" />
            <span>Student Portal Login</span>
          </button>

          <button 
            onClick={() => navigate('/admin/login')}
            style={{
              display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '15px',
              padding: '18px 24px', background: 'rgba(255, 165, 0, 0.05)',
              border: '1px solid #FFA500', borderRadius: '12px',
              color: 'var(--text-main)', fontSize: '1.1rem', cursor: 'pointer',
              transition: 'all 0.3s', boxShadow: '0 0 15px rgba(255, 165, 0, 0.1)'
            }}
            onMouseOver={(e) => {
              e.currentTarget.style.background = 'rgba(255, 165, 0, 0.15)';
              e.currentTarget.style.boxShadow = '0 0 25px rgba(255, 165, 0, 0.3)';
            }}
            onMouseOut={(e) => {
              e.currentTarget.style.background = 'rgba(255, 165, 0, 0.05)';
              e.currentTarget.style.boxShadow = '0 0 15px rgba(255, 165, 0, 0.1)';
            }}
          >
            <ShieldAlert size={24} color="#FFA500" />
            <span>Administrator Terminal</span>
          </button>

        </motion.div>

        <motion.div variants={itemVariants} style={{ marginTop: '2.5rem' }}>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>
            New user?{' '}
            <span 
              onClick={() => navigate('/register')}
              style={{ color: 'var(--neon-blue)', cursor: 'pointer', textDecoration: 'underline', fontWeight: 'bold' }}
            >
              Create a Student Account
            </span>
          </p>
        </motion.div>

      </motion.div>
    </div>
  );
};

export default Home;
