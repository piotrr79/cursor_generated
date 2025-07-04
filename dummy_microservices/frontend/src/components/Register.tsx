import React, { useState } from 'react';
import axios from 'axios';

interface RegisterProps {
  onRegister: () => void;
  onSwitch: () => void;
}

const Register: React.FC<RegisterProps> = ({ onRegister, onSwitch }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setSuccess(false);
    try {
      await axios.post('http://localhost:8001/register', { username, password });
      setSuccess(true);
      setTimeout(() => onRegister(), 1000);
    } catch (err) {
      setError('Registration failed');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Username</label>
        <input value={username} onChange={e => setUsername(e.target.value)} required />
      </div>
      <div>
        <label>Password</label>
        <input type="password" value={password} onChange={e => setPassword(e.target.value)} required />
      </div>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {success && <div style={{ color: 'green' }}>Registered! Redirecting...</div>}
      <button type="submit">Register</button>
      <button type="button" onClick={onSwitch}>Back to Login</button>
    </form>
  );
};

export default Register; 