import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate, Link } from 'react-router-dom';
import Register from './components/Register';
import Login from './components/Login';
import ISSPosition from './components/ISSPosition';
import { AuthService } from './components/AuthService';

/**
 * App component sets up routing, navigation, and authentication state.
 * Protects ISSPosition route and provides navigation links.
 */
const App: React.FC = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(!!AuthService.getInstance().getToken());

  /**
   * Handles user logout and updates authentication state.
   */
  const handleLogout = () => {
    AuthService.getInstance().logout();
    setIsAuthenticated(false);
  };

  /**
   * Handles successful login and updates authentication state.
   */
  const handleLogin = () => {
    setIsAuthenticated(true);
  };

  return (
    <Router>
      <nav>
        <Link to="/">ISS Position</Link> |{' '}
        {!isAuthenticated && <Link to="/login">Login</Link>} |{' '}
        {!isAuthenticated && <Link to="/register">Register</Link>}
        {isAuthenticated && <button onClick={handleLogout}>Logout</button>}
      </nav>
      <Routes>
        <Route
          path="/"
          element={
            isAuthenticated ? <ISSPosition /> : <Navigate to="/login" replace />
          }
        />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login onLogin={handleLogin} />} />
      </Routes>
    </Router>
  );
};

export default App;
