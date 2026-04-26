import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { Shield, Trash2, LogOut, Users } from 'lucide-react';
import { useContext } from 'react';
import { LogoutContext } from '../contexts';

const AdminDashboard = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMsg, setErrorMsg] = useState('');
  
  const navigate = useNavigate();
  const { handleLogout: triggerLogout } = useContext(LogoutContext);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const token = localStorage.getItem('adminToken');
      if (!token) {
        navigate('/admin/login');
        return;
      }

      const BACKEND_SERVER = import.meta.env.VITE_BACKEND_SERVER || 'http://localhost:4000';
      const res = await fetch(`${BACKEND_SERVER}/api/admin/users`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      
      const data = await res.json();
      
      if (!res.ok) {
        throw new Error(data.message || 'Failed to fetch users');
      }
      
      setUsers(data.users);
      setLoading(false);
    } catch (error) {
      setErrorMsg(error.message);
      setLoading(false);
      if (error.message.includes('Access denied') || error.message.includes('Invalid or expired')) {
        navigate('/admin/login');
      }
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm("Are you sure you want to delete this user? This cannot be undone.")) return;

    try {
      const token = localStorage.getItem('adminToken');
      const BACKEND_SERVER = import.meta.env.VITE_BACKEND_SERVER || 'http://localhost:4000';
      const res = await fetch(`${BACKEND_SERVER}/api/admin/users/${id}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.message || 'Failed to delete user');
      }

      // Update state to remove deleted user
      setUsers(users.filter(user => user._id !== id));
      alert("User deleted successfully.");
    } catch (error) {
      alert("Error: " + error.message);
    }
  };

  const handleLogout = () => {
    triggerLogout('/admin/login');
  };

  return (
    <div style={{
      minHeight: '100vh',
      background: 'var(--bg-gradient)',
      padding: '4rem 2rem',
      color: 'var(--text-main)'
    }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto' }}>
        <header style={{
          display: 'flex', justifyContent: 'space-between', alignItems: 'center',
          marginBottom: '3rem', paddingBottom: '1rem', borderBottom: '1px solid var(--glass-border)'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
            <Shield size={36} color="#FFA500" />
            <h1 style={{ color: '#FFA500', fontSize: '2rem' }}>Admin Dashboard</h1>
          </div>
          <button 
            onClick={handleLogout}
            style={{
              display: 'flex', alignItems: 'center', gap: '8px',
              background: 'transparent', border: '1px solid var(--neon-error)',
              color: 'var(--neon-error)', padding: '10px 20px', borderRadius: '8px',
              cursor: 'pointer', transition: 'all 0.3s'
            }}
            onMouseOver={(e) => e.currentTarget.style.background = 'rgba(255, 68, 68, 0.1)'}
            onMouseOut={(e) => e.currentTarget.style.background = 'transparent'}
          >
            <LogOut size={18} /> Logout
          </button>
        </header>

        <section className="glass-panel" style={{ padding: '2rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '2rem' }}>
            <Users size={24} color="var(--neon-cyan)" />
            <h2 style={{ fontSize: '1.5rem' }}>Registered Students</h2>
          </div>

          {loading ? (
            <p style={{ textAlign: 'center', padding: '2rem' }}>Loading users...</p>
          ) : errorMsg ? (
            <p style={{ textAlign: 'center', color: 'var(--neon-error)' }}>{errorMsg}</p>
          ) : users.length === 0 ? (
            <p style={{ textAlign: 'center', color: 'var(--text-muted)' }}>No users found in the system.</p>
          ) : (
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                <thead>
                  <tr style={{ background: 'rgba(255, 255, 255, 0.05)' }}>
                    <th style={{ padding: '15px', borderBottom: '1px solid var(--glass-border)' }}>Name</th>
                    <th style={{ padding: '15px', borderBottom: '1px solid var(--glass-border)' }}>Email</th>
                    <th style={{ padding: '15px', borderBottom: '1px solid var(--glass-border)' }}>Institute</th>
                    <th style={{ padding: '15px', borderBottom: '1px solid var(--glass-border)' }}>Date Joined</th>
                    <th style={{ padding: '15px', borderBottom: '1px solid var(--glass-border)', textAlign: 'right' }}>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {users.map((user) => (
                    <motion.tr 
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      key={user._id}
                      style={{ borderBottom: '1px solid rgba(255, 255, 255, 0.05)', transition: 'background 0.3s' }}
                      onMouseOver={(e) => e.currentTarget.style.background = 'rgba(255, 255, 255, 0.02)'}
                      onMouseOut={(e) => e.currentTarget.style.background = 'transparent'}
                    >
                      <td style={{ padding: '15px' }}>{user.name}</td>
                      <td style={{ padding: '15px', color: 'var(--neon-cyan)' }}>{user.email}</td>
                      <td style={{ padding: '15px' }}>{user.institute_name}</td>
                      <td style={{ padding: '15px', color: 'var(--text-muted)' }}>
                        {new Date(user.created_at).toLocaleDateString()}
                      </td>
                      <td style={{ padding: '15px', textAlign: 'right' }}>
                        <button 
                          onClick={() => handleDelete(user._id)}
                          style={{
                            background: 'transparent', border: 'none', color: 'var(--neon-error)',
                            cursor: 'pointer', padding: '8px', borderRadius: '4px',
                            transition: 'all 0.3s'
                          }}
                          onMouseOver={(e) => e.currentTarget.style.background = 'rgba(255, 68, 68, 0.1)'}
                          onMouseOut={(e) => e.currentTarget.style.background = 'transparent'}
                          title="Delete User"
                        >
                          <Trash2 size={20} />
                        </button>
                      </td>
                    </motion.tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </section>
      </div>
    </div>
  );
};

export default AdminDashboard;
