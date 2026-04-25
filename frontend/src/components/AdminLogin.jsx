import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { ShieldAlert, User, Lock, Activity, CheckCircle } from 'lucide-react';
import AuthBackground from './AuthBackground';

const pageVariants = {
  initial: { opacity: 0, scale: 0.95, filter: 'blur(10px)' },
  animate: { opacity: 1, scale: 1, filter: 'blur(0px)', transition: { duration: 0.6, ease: 'easeOut', staggerChildren: 0.1 } },
  exit: { opacity: 0, scale: 1.05, filter: 'blur(10px)', transition: { duration: 0.4, ease: 'easeIn' } }
};

const itemVariants = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0, transition: { duration: 0.5 } }
};

const AdminLogin = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [focusedId, setFocusedId] = useState(null);
  
  const [status, setStatus] = useState('idle'); // idle, loading, error, success
  const navigate = useNavigate();

  const [errorMsg, setErrorMsg] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    if (!username || !password) {
      setErrorMsg('Please fill in all fields.');
      setStatus('error');
      setTimeout(() => setStatus('idle'), 2000);
      return;
    }

    setStatus('loading');
    
    try {
      const BACKEND_SERVER = import.meta.env.VITE_BACKEND_SERVER || 'http://localhost:4000';
      const res = await fetch(`${BACKEND_SERVER}/api/admin/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      });

      const data = await res.json();

      if (!res.ok) {
        setErrorMsg(data.message || 'Login failed.');
        setStatus('error');
        setTimeout(() => setStatus('idle'), 2500);
        return;
      }

      // Store token
      localStorage.setItem('adminToken', data.token);

      setStatus('success');
      setTimeout(() => {
        navigate('/admin/dashboard');
      }, 1500);
    } catch (err) {
      setErrorMsg('Unable to connect to server.');
      setStatus('error');
      setTimeout(() => setStatus('idle'), 2500);
    }
  };

  return (
    <div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative' }}>
      <AuthBackground />
      
      <motion.div
        variants={pageVariants}
        initial="initial"
        animate="animate"
        exit="exit"
        className={`glass-panel ${status === 'error' ? 'shake' : ''}`}
        style={{
          width: '100%', maxWidth: '450px',
          padding: '3rem 2.5rem',
          boxShadow: status === 'error' ? '0 0 30px rgba(255, 68, 68, 0.4)' : status === 'success' ? '0 0 40px rgba(255, 165, 0, 0.5)' : 'var(--glass-glow)',
          border: status === 'error' ? '1px solid var(--neon-error)' : status === 'success' ? '1px solid #FFA500' : '1px solid var(--glass-border)',
          transition: 'box-shadow 0.3s ease, border 0.3s ease'
        }}
      >
        <AnimatePresence mode="wait">
          {status === 'loading' && (
            <motion.div 
              key="loading"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(5, 11, 20, 0.8)', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', zIndex: 10 }}
            >
              <Activity size={50} color="#FFA500" style={{ marginBottom: '1rem' }} />
              <h3 className="text-neon" style={{ color: '#FFA500' }}>Authenticating Admin...</h3>
              <div style={{ display: 'flex', gap: '4px', marginTop: '1rem' }}>
                {[...Array(8)].map((_, i) => (
                  <motion.div 
                    key={i}
                    animate={{ height: ['10px', '30px', '10px'] }}
                    transition={{ duration: 0.6, repeat: Infinity, delay: i * 0.1 }}
                    style={{ width: '4px', background: '#FFA500', borderRadius: '2px' }}
                  />
                ))}
              </div>
            </motion.div>
          )}

          {status === 'success' && (
            <motion.div 
              key="success"
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0 }}
              style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(255, 165, 0, 0.1)', backdropFilter: 'blur(10px)', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', zIndex: 10 }}
            >
              <motion.div animate={{ scale: [1, 1.2, 1] }} transition={{ duration: 1, repeat: Infinity }}>
                <CheckCircle size={60} color="#FFA500" style={{ marginBottom: '1rem', filter: 'drop-shadow(0 0 10px rgba(255, 165, 0, 0.8))' }} />
              </motion.div>
              <h3 className="text-neon" style={{ color: '#FFA500' }}>Admin Access Granted</h3>
            </motion.div>
          )}
        </AnimatePresence>

        <motion.div variants={itemVariants} style={{ textAlign: 'center', marginBottom: '2.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '1rem' }}>
            <div style={{ padding: '15px', background: 'rgba(255, 165, 0, 0.1)', borderRadius: '50%', boxShadow: '0 0 15px rgba(255, 165, 0, 0.3)' }}>
              <ShieldAlert size={32} color="#FFA500" />
            </div>
          </div>
          <h2 style={{ fontSize: '1.8rem', letterSpacing: '1px' }}>Admin <span style={{ color: '#FFA500' }}>Terminal</span></h2>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', marginTop: '0.5rem' }}>Enter master credentials.</p>
        </motion.div>

        <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          
          <motion.div variants={itemVariants} style={{ position: 'relative' }}>
            <div style={{ position: 'absolute', top: '50%', left: '16px', transform: 'translateY(-50%)', color: focusedId === 'id' ? '#FFA500' : 'var(--text-muted)', transition: 'color 0.3s' }}>
              <User size={20} />
            </div>
            <input 
              type="text" 
              placeholder="Admin Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              onFocus={() => setFocusedId('id')}
              onBlur={() => setFocusedId(null)}
              style={{
                width: '100%', padding: '16px 20px 16px 48px',
                background: 'rgba(0,0,0,0.4)',
                border: `1px solid ${focusedId === 'id' ? '#FFA500' : 'var(--glass-border)'}`,
                borderRadius: '12px', color: '#fff', fontSize: '1rem', outline: 'none',
                boxShadow: focusedId === 'id' ? '0 0 15px rgba(255, 165, 0, 0.2)' : 'none',
                transition: 'all 0.3s'
              }}
            />
          </motion.div>

          <motion.div variants={itemVariants} style={{ position: 'relative' }}>
            <div style={{ position: 'absolute', top: '50%', left: '16px', transform: 'translateY(-50%)', color: focusedId === 'pass' ? '#FFA500' : 'var(--text-muted)', transition: 'color 0.3s' }}>
              <Lock size={20} />
            </div>
            <input 
              type="password" 
              placeholder="Admin Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              onFocus={() => setFocusedId('pass')}
              onBlur={() => setFocusedId(null)}
              style={{
                width: '100%', padding: '16px 20px 16px 48px',
                background: 'rgba(0,0,0,0.4)',
                border: `1px solid ${focusedId === 'pass' ? '#FFA500' : 'var(--glass-border)'}`,
                borderRadius: '12px', color: '#fff', fontSize: '1rem', outline: 'none',
                boxShadow: focusedId === 'pass' ? '0 0 15px rgba(255, 165, 0, 0.2)' : 'none',
                transition: 'all 0.3s'
              }}
            />
          </motion.div>

          {status === 'error' && (
            <motion.p initial={{ opacity: 0 }} animate={{ opacity: 1 }} style={{ color: 'var(--neon-error)', fontSize: '0.85rem', textAlign: 'center', marginTop: '-0.5rem' }}>
              Access Denied. {errorMsg}
            </motion.p>
          )}

          <motion.div variants={itemVariants} style={{ marginTop: '1rem' }}>
            <motion.button 
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              className="btn-primary" 
              type="submit"
              disabled={status !== 'idle' && status !== 'error'}
              style={{ width: '100%', display: 'flex', justifyContent: 'center', padding: '16px', fontSize: '1.1rem', letterSpacing: '2px', color: '#FFA500', borderColor: '#FFA500' }}
            >
              VERIFY
            </motion.button>
          </motion.div>
        </form>
      </motion.div>
    </div>
  );
};

export default AdminLogin;
