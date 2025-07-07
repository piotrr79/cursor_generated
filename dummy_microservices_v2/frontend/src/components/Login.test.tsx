import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import Login from './Login';
import { AuthService } from './AuthService';

jest.mock('./AuthService');

const mockLogin = jest.fn();
(AuthService.getInstance as jest.Mock).mockReturnValue({ login: mockLogin });

describe('Login component', () => {
  beforeEach(() => {
    mockLogin.mockReset();
  });

  it('renders login form', () => {
    render(<Login />);
    expect(screen.getByPlaceholderText('Email')).toBeInTheDocument();
    expect(screen.getByPlaceholderText('Password')).toBeInTheDocument();
    expect(screen.getByText('Login')).toBeInTheDocument();
  });

  it('shows success message on successful login', async () => {
    mockLogin.mockResolvedValue(true);
    render(<Login />);
    fireEvent.change(screen.getByPlaceholderText('Email'), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'password123' } });
    fireEvent.click(screen.getByText('Login'));
    expect(await screen.findByText('Login successful!')).toBeInTheDocument();
  });

  it('shows error message on failed login', async () => {
    mockLogin.mockResolvedValue(false);
    render(<Login />);
    fireEvent.change(screen.getByPlaceholderText('Email'), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'password123' } });
    fireEvent.click(screen.getByText('Login'));
    expect(await screen.findByText('Invalid email or password')).toBeInTheDocument();
  });

  it('shows error message on network error', async () => {
    mockLogin.mockRejectedValue(new Error('Network error'));
    render(<Login />);
    fireEvent.change(screen.getByPlaceholderText('Email'), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'password123' } });
    fireEvent.click(screen.getByText('Login'));
    expect(await screen.findByText('Login error')).toBeInTheDocument();
  });
}); 