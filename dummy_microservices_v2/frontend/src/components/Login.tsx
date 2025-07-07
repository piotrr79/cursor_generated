import React, { useState } from 'react';
import { AuthService } from './AuthService';

/**
 * Login component allows users to authenticate and receive a JWT token.
 * Uses AuthService for login logic.
 */
const Login: React.FC<{ onLogin?: () => void }> = ({ onLogin }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  /**
   * Handles form submission for login.
   */
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccess(false);
    try {
      const ok = await AuthService.getInstance().login(email, password);
      if (ok) {
        setSuccess(true);
        if (onLogin) onLogin();
      } else {
        setError('Invalid email or password');
      }
    } catch (err) {
      setError('Login error');
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={e => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          required
        />
        <button type="submit">Login</button>
      </form>
      {error && <div className="error">{error}</div>}
      {success && <div className="success">Login successful!</div>}
    </div>
  );
};

export default Login; 