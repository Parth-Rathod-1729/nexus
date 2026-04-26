import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate, Link } from 'react-router-dom';
import { ShieldCheck, User, Lock, Mail, Activity, CheckCircle, ArrowLeft, Eye, EyeOff } from 'lucide-react';
import AuthBackground from './AuthBackground';

const pageVariants = {
  initial: { opacity: 0, x: -50, filter: 'blur(10px)' },
  animate: { opacity: 1, x: 0, filter: 'blur(0px)', transition: { duration: 0.6, ease: 'easeOut', staggerChildren: 0.1 } },
  exit: { opacity: 0, x: 50, filter: 'blur(10px)', transition: { duration: 0.4, ease: 'easeIn' } }
};

const itemVariants = {
  initial: { opacity: 0, x: -20 },
  animate: { opacity: 1, x: 0, transition: { duration: 0.5 } }
};

const Register = () => {
  const [formData, setFormData] = useState({ name: '', email: '', password: '', confirm: '' });
  const [focusedId, setFocusedId] = useState(null);
  const [status, setStatus] = useState('idle'); // idle, loading, success, error
  const [errorMsg, setErrorMsg] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirm, setShowConfirm] = useState(false);
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    if (formData.password !== formData.confirm) return;

    setStatus('loading');
    
    try {
      const BACKEND_SERVER = import.meta.env.VITE_BACKEND_SERVER || 'http://localhost:4000';
      const res = await fetch(`${BACKEND_SERVER}/api/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: formData.name,
          email: formData.email,
          password: formData.password,
          // You could collect institute here if you add a field for it
        }),
      });

      const data = await res.json();

      if (!res.ok) {
        setErrorMsg(data.message || 'Registration failed.');
        setStatus('error');
        setTimeout(() => setStatus('idle'), 2500);
        return;
      }

      setStatus('success');
      setTimeout(() => {
        navigate('/login');
      }, 2000);
    } catch (err) {
      setErrorMsg('Unable to connect to server.');
      setStatus('error');
      setTimeout(() => setStatus('idle'), 2500);
    }
  };

  return (
    <div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative', padding: '2rem 0' }}>
      <AuthBackground />
      
      {/* Back Button */}
      <motion.button
        initial={{ opacity: 0, x: -20 }}
        animate={{ opacity: 1, x: 0 }}
        whileHover={{ x: -5, color: 'var(--neon-violet)' }}
        onClick={() => navigate('/')}
        style={{
          position: 'absolute',
          top: '40px',
          left: '40px',
          background: 'none',
          border: 'none',
          color: 'var(--text-muted)',
          display: 'flex',
          alignItems: 'center',
          gap: '10px',
          cursor: 'pointer',
          zIndex: 100,
          fontFamily: "'Space Grotesk', sans-serif",
          fontWeight: 600,
          fontSize: '0.9rem',
          letterSpacing: '1px',
          textTransform: 'uppercase'
        }}
      >
        <ArrowLeft size={20} />
        RETURN TO NEXUS
      </motion.button>
      
      <motion.div
        variants={pageVariants}
        initial="initial"
        animate="animate"
        exit="exit"
        className="glass-panel"
        style={{
          width: '100%', maxWidth: '500px',
          padding: '3rem 2.5rem',
          boxShadow: status === 'success' ? '0 0 40px rgba(0, 255, 204, 0.5)' : 'var(--glass-glow)',
          border: status === 'success' ? '1px solid var(--neon-cyan)' : '1px solid var(--glass-border)',
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
              style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(5, 11, 20, 0.9)', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', zIndex: 10 }}
            >
              <Activity size={60} color="var(--neon-violet)" style={{ marginBottom: '1rem' }} />
              <h3 className="text-neon" style={{ color: 'var(--neon-violet)' }}>Provisioning Neural Mesh</h3>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', marginTop: '0.5rem' }}>Allocating agent resources...</p>
              
              <div style={{ width: '60%', height: '4px', background: 'var(--glass-border)', borderRadius: '2px', marginTop: '1.5rem', overflow: 'hidden', position: 'relative' }}>
                <motion.div 
                  initial={{ width: '0%' }}
                  animate={{ width: '100%' }}
                  transition={{ duration: 2.8, ease: "easeInOut" }}
                  style={{ position: 'absolute', top: 0, left: 0, height: '100%', background: 'linear-gradient(90deg, var(--neon-blue), var(--neon-violet))', boxShadow: '0 0 10px var(--neon-violet)' }}
                />
              </div>
            </motion.div>
          )}

          {status === 'success' && (
            <motion.div 
              key="success"
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0 }}
              style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, background: 'rgba(0, 255, 204, 0.1)', backdropFilter: 'blur(10px)', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', zIndex: 10 }}
            >
              <motion.div animate={{ scale: [1, 1.2, 1] }} transition={{ duration: 1, repeat: Infinity }}>
                <ShieldCheck size={60} color="var(--neon-cyan)" style={{ marginBottom: '1rem', filter: 'drop-shadow(0 0 10px rgba(0, 255, 204, 0.8))' }} />
              </motion.div>
              <h3 className="text-neon" style={{ color: 'var(--neon-cyan)' }}>Entity Registered</h3>
              <p style={{ color: 'var(--text-main)', marginTop: '0.5rem', fontSize: '0.9rem' }}>Return to Login Portal...</p>
            </motion.div>
          )}
        </AnimatePresence>

        <motion.div variants={itemVariants} style={{ textAlign: 'center', marginBottom: '2.5rem' }}>
          <h2 style={{ fontSize: '1.8rem', letterSpacing: '1px' }}>Initialize <span style={{ color: 'var(--neon-violet)' }}>New User</span></h2>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', marginTop: '0.5rem' }}>Establish connection parameters to access The Good Ultron.</p>
        </motion.div>

        <form onSubmit={handleRegister} style={{ display: 'flex', flexDirection: 'column', gap: '1.2rem' }}>
          
          <motion.div variants={itemVariants} style={{ position: 'relative' }}>
            <div style={{ position: 'absolute', top: '50%', left: '16px', transform: 'translateY(-50%)', color: focusedId === 'name' ? 'var(--neon-blue)' : 'var(--text-muted)', transition: 'color 0.3s' }}>
              <User size={18} />
            </div>
            <input 
              required
              type="text" 
              placeholder="Designation / Name"
              value={formData.name}
              onChange={(e) => setFormData({...formData, name: e.target.value})}
              onFocus={() => setFocusedId('name')}
              onBlur={() => setFocusedId(null)}
              style={{
                width: '100%', padding: '14px 20px 14px 48px',
                background: 'rgba(0,0,0,0.4)',
                border: `1px solid ${focusedId === 'name' ? 'var(--neon-blue)' : 'var(--glass-border)'}`,
                borderRadius: '12px', color: '#fff', fontSize: '0.95rem', outline: 'none',
                boxShadow: focusedId === 'name' ? '0 0 15px rgba(0, 210, 255, 0.2)' : 'none',
                transition: 'all 0.3s'
              }}
            />
          </motion.div>

          <motion.div variants={itemVariants} style={{ position: 'relative' }}>
            <div style={{ position: 'absolute', top: '50%', left: '16px', transform: 'translateY(-50%)', color: focusedId === 'email' ? 'var(--neon-cyan)' : 'var(--text-muted)', transition: 'color 0.3s' }}>
              <Mail size={18} />
            </div>
            <input 
              required
              type="email" 
              placeholder="Communication Uplink (Email)"
              value={formData.email}
              onChange={(e) => setFormData({...formData, email: e.target.value})}
              onFocus={() => setFocusedId('email')}
              onBlur={() => setFocusedId(null)}
              style={{
                width: '100%', padding: '14px 20px 14px 48px',
                background: 'rgba(0,0,0,0.4)',
                border: `1px solid ${focusedId === 'email' ? 'var(--neon-cyan)' : 'var(--glass-border)'}`,
                borderRadius: '12px', color: '#fff', fontSize: '0.95rem', outline: 'none',
                boxShadow: focusedId === 'email' ? '0 0 15px rgba(0, 255, 204, 0.2)' : 'none',
                transition: 'all 0.3s'
              }}
            />
          </motion.div>

          <motion.div variants={itemVariants} style={{ position: 'relative' }}>
            <div style={{ position: 'absolute', top: '50%', left: '16px', transform: 'translateY(-50%)', color: focusedId === 'pass1' ? 'var(--neon-violet)' : 'var(--text-muted)', transition: 'color 0.3s' }}>
              <Lock size={18} />
            </div>
            <input 
              required
              type={showPassword ? "text" : "password"} 
              placeholder="Encryption Key (Password)"
              value={formData.password}
              onChange={(e) => setFormData({...formData, password: e.target.value})}
              onFocus={() => setFocusedId('pass1')}
              onBlur={() => setFocusedId(null)}
              style={{
                width: '100%', padding: '14px 48px 14px 48px',
                background: 'rgba(0,0,0,0.4)',
                border: `1px solid ${focusedId === 'pass1' ? 'var(--neon-violet)' : 'var(--glass-border)'}`,
                borderRadius: '12px', color: '#fff', fontSize: '0.95rem', outline: 'none',
                boxShadow: focusedId === 'pass1' ? '0 0 15px rgba(138, 43, 226, 0.2)' : 'none',
                transition: 'all 0.3s'
              }}
            />
            <button
              type="button"
              onClick={() => setShowPassword(!showPassword)}
              style={{
                position: 'absolute', top: '50%', right: '16px', transform: 'translateY(-50%)',
                background: 'none', border: 'none', cursor: 'pointer', padding: '4px',
                color: focusedId === 'pass1' ? 'var(--neon-violet)' : 'var(--text-muted)',
                transition: 'color 0.3s', display: 'flex', alignItems: 'center'
              }}
            >
              {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
            </button>
          </motion.div>

          <motion.div variants={itemVariants} style={{ position: 'relative' }}>
            <div style={{ position: 'absolute', top: '50%', left: '16px', transform: 'translateY(-50%)', color: focusedId === 'pass2' ? 'var(--neon-violet)' : 'var(--text-muted)', transition: 'color 0.3s' }}>
              <Lock size={18} />
            </div>
            <input 
              required
              type={showConfirm ? "text" : "password"} 
              placeholder="Verify Encryption Key"
              value={formData.confirm}
              onChange={(e) => setFormData({...formData, confirm: e.target.value})}
              onFocus={() => setFocusedId('pass2')}
              onBlur={() => setFocusedId(null)}
              style={{
                width: '100%', padding: '14px 48px 14px 48px',
                background: 'rgba(0,0,0,0.4)',
                border: `1px solid ${focusedId === 'pass2' ? 'var(--neon-violet)' : 'var(--glass-border)'}`,
                borderRadius: '12px', color: '#fff', fontSize: '0.95rem', outline: 'none',
                boxShadow: focusedId === 'pass2' ? '0 0 15px rgba(138, 43, 226, 0.2)' : 'none',
                transition: 'all 0.3s'
              }}
            />
            <button
              type="button"
              onClick={() => setShowConfirm(!showConfirm)}
              style={{
                position: 'absolute', top: '50%', right: '16px', transform: 'translateY(-50%)',
                background: 'none', border: 'none', cursor: 'pointer', padding: '4px',
                color: focusedId === 'pass2' ? 'var(--neon-violet)' : 'var(--text-muted)',
                transition: 'color 0.3s', display: 'flex', alignItems: 'center'
              }}
            >
              {showConfirm ? <EyeOff size={18} /> : <Eye size={18} />}
            </button>
            {formData.password && formData.confirm && formData.password !== formData.confirm && (
              <p style={{ color: 'var(--neon-error)', fontSize: '0.8rem', position: 'absolute', right: '10px', top: '50%', transform: 'translateY(-50%)' }}>Mismatch</p>
            )}
          </motion.div>

          {status === 'error' && (
            <motion.p initial={{ opacity: 0 }} animate={{ opacity: 1 }} style={{ color: 'var(--neon-error)', fontSize: '0.85rem', textAlign: 'center', marginTop: '-0.5rem' }}>
              Registration Failed. {errorMsg}
            </motion.p>
          )}

          <motion.div variants={itemVariants} style={{ marginTop: '1.5rem' }}>
            <motion.button 
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              className="btn-primary" 
              type="submit"
              disabled={status !== 'idle' || (formData.password !== formData.confirm)}
              style={{ 
                width: '100%', display: 'flex', justifyContent: 'center', padding: '16px', fontSize: '1.05rem', letterSpacing: '1px',
                borderColor: 'var(--neon-violet)', color: 'var(--neon-violet)',
                boxShadow: '0 0 10px rgba(138, 43, 226, 0.2)'
              }}
            >
              CREATE ENTITY
            </motion.button>
          </motion.div>
        </form>

        <motion.div variants={itemVariants} style={{ textAlign: 'center', marginTop: '2rem' }}>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>
            Existing Entity?{' '}
            <Link to="/login" style={{ color: 'var(--neon-cyan)', textDecoration: 'none', fontWeight: 'bold' }}>
              Initiate Login
            </Link>
          </p>
        </motion.div>
      </motion.div>
    </div>
  );
};

export default Register;
