import React, { createContext, useContext, useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation, useNavigate } from 'react-router-dom';
import { motion, useScroll, useSpring, AnimatePresence } from 'framer-motion';
import { Cpu, LogOut, Menu, X } from 'lucide-react';
import './App.css';

// Component imports
import Hero from './components/Hero';
import UploadSection from './components/UploadSection';
import PipelineVisualizer from './components/PipelineVisualizer';
import SceneGenerator from './components/SceneGenerator';
import VideoPreview from './components/VideoPreview';
import ImpactSection from './components/ImpactSection';
import Login from './components/Login';
import Register from './components/Register';
import AdminLogin from './components/AdminLogin';
import AdminDashboard from './components/AdminDashboard';
import Home from './components/Home';

// ── Video Context ────────────────────────────────────────────────────────────
export const VideoContext = createContext(null);

export function useVideo() {
  return useContext(VideoContext);
}

function VideoProvider({ children }) {
  const [videoData, setVideoData] = useState(null); 
  return (
    <VideoContext.Provider value={{ videoData, setVideoData }}>
      {children}
    </VideoContext.Provider>
  );
}

// ── Page Wrapper for Transitions ─────────────────────────────────────────────
const PageWrapper = ({ children }) => (
  <motion.div
    initial={{ opacity: 0, y: 20 }}
    animate={{ opacity: 1, y: 0 }}
    exit={{ opacity: 0, y: -20 }}
    transition={{ duration: 0.5, ease: [0.22, 1, 0.36, 1] }}
  >
    {children}
  </motion.div>
);

// ── Navbar ───────────────────────────────────────────────────────────────────
const Navbar = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 50);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleLogout = () => {
    localStorage.clear();
    navigate('/');
  };

  return (
    <motion.nav
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      style={{
        position: 'fixed', top: 0, left: 0, right: 0, zIndex: 1000,
        padding: isScrolled ? '15px 40px' : '25px 40px',
        display: 'flex', justifyContent: 'space-between', alignItems: 'center',
        background: isScrolled ? 'rgba(5, 11, 20, 0.8)' : 'transparent',
        backdropFilter: isScrolled ? 'blur(20px)' : 'none',
        borderBottom: isScrolled ? '1px solid var(--glass-border)' : '1px solid transparent',
        transition: 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)'
      }}
    >
      <div 
        style={{ display: 'flex', alignItems: 'center', gap: '12px', cursor: 'pointer' }}
        onClick={() => navigate('/dashboard')}
      >
        <Cpu size={32} className="text-glow" color="var(--neon-cyan)" />
        <span className="text-gradient" style={{
          fontFamily: "'Space Grotesk', sans-serif",
          fontWeight: 800, fontSize: '1.5rem', letterSpacing: '1px'
        }}>
          NEXUS
        </span>
      </div>
      
      <div style={{ display: 'flex', gap: '32px', alignItems: 'center' }}>
        {['Pipeline', 'Generator', 'Impact'].map((item) => (
          <a 
            key={item}
            href={`#${item.toLowerCase()}`} 
            className="nav-link"
            style={{ 
              color: 'var(--text-muted)', 
              textDecoration: 'none', 
              fontSize: '0.9rem', 
              fontWeight: 600,
              textTransform: 'uppercase',
              letterSpacing: '1px'
            }}
          >
            {item}
          </a>
        ))}
        <button 
          className="btn-primary" 
          style={{ padding: '10px 24px', fontSize: '0.85rem' }}
          onClick={handleLogout}
        >
          <LogOut size={16} />
          TERMINATE SESSION
        </button>
      </div>
    </motion.nav>
  );
};

// ── Dashboard ────────────────────────────────────────────────────────────────
const Dashboard = () => {
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, { stiffness: 100, damping: 30, restDelta: 0.001 });

  return (
    <PageWrapper>
      <motion.div style={{
        position: 'fixed', top: 0, left: 0, right: 0, height: '4px',
        background: 'linear-gradient(90deg, var(--neon-cyan), var(--neon-blue), var(--neon-violet))',
        transformOrigin: '0%', scaleX, zIndex: 1001
      }} />
      <Navbar />
      <main className="app-container" style={{ paddingTop: '120px' }}>
        <section id="hero"><Hero /></section>
        <section id="upload"><UploadSection /></section>
        <section id="pipeline"><PipelineVisualizer /></section>
        <section id="generator"><SceneGenerator /></section>
        <section id="preview"><VideoPreview /></section>
        <section id="impact"><ImpactSection /></section>
      </main>
      <footer style={{
        marginTop: '120px', padding: '60px 40px', textAlign: 'center',
        borderTop: '1px solid var(--glass-border)', color: 'var(--text-muted)',
        background: 'rgba(0,0,0,0.2)'
      }}>
        <p style={{ fontSize: '0.9rem', letterSpacing: '1px' }}>
          PROJECT NEXUS // CINEMATIC AI SYSTEMS © {new Date().getFullYear()}
        </p>
      </footer>
    </PageWrapper>
  );
};

// ── Routing ──────────────────────────────────────────────────────────────────
const AnimatedRoutes = () => {
  const location = useLocation();
  return (
    <AnimatePresence mode="wait">
      <Routes location={location} key={location.pathname}>
        <Route path="/" element={<PageWrapper><Home /></PageWrapper>} />
        <Route path="/login" element={<PageWrapper><Login /></PageWrapper>} />
        <Route path="/register" element={<PageWrapper><Register /></PageWrapper>} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/admin/login" element={<PageWrapper><AdminLogin /></PageWrapper>} />
        <Route path="/admin/dashboard" element={<PageWrapper><AdminDashboard /></PageWrapper>} />
      </Routes>
    </AnimatePresence>
  );
};

function App() {
  return (
    <VideoProvider>
      <Router>
        <AnimatedRoutes />
      </Router>
    </VideoProvider>
  );
}

export default App;
