import React, { useState } from 'react';
import axios from 'axios';

interface LoginProps {
  onLogin: (token: string) => void;
  onSwitch: () => void;
}

const Login: React.FC<LoginProps> = ({ onLogin, onSwitch }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    try {
      const resp = await axios.post('http://localhost:8001/token', new URLSearchParams({
        username,
        password,
        grant_type: 'password',
      }), {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      });
      onLogin(resp.data.access_token);
    } catch (err) {
      setError('Login failed');
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
      <button type="submit">Login</button>
      <button type="button" onClick={onSwitch}>Register</button>
    </form>
  );
};

export default Login; 