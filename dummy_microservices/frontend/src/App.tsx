import React, { useState } from 'react';
import Login from './components/Login';
import Register from './components/Register';
import ISSPosition from './components/ISSPosition';

const App: React.FC = () => {
  const [token, setToken] = useState<string | null>(null);
  const [view, setView] = useState<'login' | 'register' | 'iss'>('login');

  const handleLogin = (token: string) => {
    setToken(token);
    setView('iss');
  };

  const handleLogout = () => {
    setToken(null);
    setView('login');
  };

  return (
    <div style={{ maxWidth: 400, margin: '2em auto', fontFamily: 'Arial, sans-serif' }}>
      <h1>ISS Position Tracker</h1>
      {token ? (
        <>
          <button onClick={handleLogout} style={{ float: 'right' }}>Logout</button>
          <ISSPosition token={token} />
        </>
      ) : view === 'login' ? (
        <>
          <Login onLogin={handleLogin} onSwitch={() => setView('register')} />
        </>
      ) : (
        <Register onRegister={() => setView('login')} onSwitch={() => setView('login')} />
      )}
    </div>
  );
};

export default App; 