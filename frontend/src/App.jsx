import React, { createContext, useContext, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import { motion, useScroll, useSpring, AnimatePresence } from 'framer-motion';
import { Cpu } from 'lucide-react';
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
  // videoData = { url, statusMessage, scenesRendered, scenesTotal } | null
  return (
    <VideoContext.Provider value={{ videoData, setVideoData }}>
      {children}
    </VideoContext.Provider>
  );
}

// ── Navbar ───────────────────────────────────────────────────────────────────
const Navbar = () => {
  return (
    <motion.nav
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ duration: 0.8, ease: 'easeOut' }}
      style={{
        position: 'fixed', top: 0, left: 0, right: 0, zIndex: 100,
        padding: '20px 40px',
        display: 'flex', justifyContent: 'space-between', alignItems: 'center',
        background: 'rgba(5, 11, 20, 0.6)',
        backdropFilter: 'blur(10px)',
        borderBottom: '1px solid var(--glass-border)'
      }}
    >
      <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
        <Cpu size={28} color="var(--neon-cyan)" />
        <span style={{
          fontFamily: "'Space Grotesk', sans-serif",
          fontWeight: 800, fontSize: '1.4rem', letterSpacing: '1px'
        }} className="text-gradient">
          The Good Ultron
        </span>
      </div>
      <div style={{ display: 'flex', gap: '24px', alignItems: 'center' }}>
        <a href="#pipeline" style={{ color: 'var(--text-muted)', textDecoration: 'none', fontSize: '0.9rem', fontWeight: 500, transition: 'color 0.3s' }}
          onMouseOver={e => e.target.style.color = 'var(--neon-cyan)'}
          onMouseOut={e => e.target.style.color = 'var(--text-muted)'}>
          Pipeline
        </a>
        <a href="#generator" style={{ color: 'var(--text-muted)', textDecoration: 'none', fontSize: '0.9rem', fontWeight: 500, transition: 'color 0.3s' }}
          onMouseOver={e => e.target.style.color = 'var(--neon-cyan)'}
          onMouseOut={e => e.target.style.color = 'var(--text-muted)'}>
          Scene Demo
        </a>
        <button className="btn-primary" style={{ padding: '8px 20px' }}
          onClick={() => window.location.href = '/'}>
          System Logout
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
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1, transition: { duration: 0.8 } }}
      exit={{ opacity: 0, y: 50, transition: { duration: 0.5 } }}
    >
      <motion.div style={{
        position: 'fixed', top: 0, left: 0, right: 0, height: '3px',
        background: 'linear-gradient(90deg, var(--neon-cyan), var(--neon-blue), var(--neon-violet))',
        transformOrigin: '0%', scaleX, zIndex: 101
      }} />
      <Navbar />
      <main className="app-container" style={{ paddingTop: '100px' }}>
        <Hero />
        <UploadSection />
        <PipelineVisualizer />
        <SceneGenerator />
        <VideoPreview />
        <ImpactSection />
      </main>
      <footer style={{
        marginTop: '100px', padding: '40px', textAlign: 'center',
        borderTop: '1px solid var(--glass-border)', color: 'var(--text-muted)'
      }}>
        <p style={{ fontSize: '0.9rem' }}>
          Project "The Good Ultron" - Cinematic AI Systems © {new Date().getFullYear()}
        </p>
      </footer>
    </motion.div>
  );
};

// ── Routing ──────────────────────────────────────────────────────────────────
const AnimatedRoutes = () => {
  const location = useLocation();
  return (
    <AnimatePresence mode="wait">
      <Routes location={location} key={location.pathname}>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/admin/login" element={<AdminLogin />} />
        <Route path="/admin/dashboard" element={<AdminDashboard />} />
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
