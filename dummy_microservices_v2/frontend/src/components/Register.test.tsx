import React from 'react';
import { render, fireEvent, screen } from '@testing-library/react';
import Register from './Register';
import { AuthService } from './AuthService';

jest.mock('./AuthService');

const mockRegister = jest.fn();
(AuthService.getInstance as jest.Mock).mockReturnValue({ register: mockRegister });

describe('Register component', () => {
  beforeEach(() => {
    mockRegister.mockReset();
  });

  it('renders registration form', () => {
    render(<Register />);
    expect(screen.getByPlaceholderText('Email')).toBeInTheDocument();
    expect(screen.getByPlaceholderText('Password')).toBeInTheDocument();
    expect(screen.getByText('Register')).toBeInTheDocument();
  });

  it('shows success message on successful registration', async () => {
    mockRegister.mockResolvedValue({ ok: true });
    render(<Register />);
    fireEvent.change(screen.getByPlaceholderText('Email'), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'password123' } });
    fireEvent.click(screen.getByText('Register'));
    expect(await screen.findByText('Registration successful! You can now log in.')).toBeInTheDocument();
  });

  it('shows error message on failed registration', async () => {
    mockRegister.mockResolvedValue({ ok: false, json: async () => ({ detail: 'Registration failed' }) });
    render(<Register />);
    fireEvent.change(screen.getByPlaceholderText('Email'), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'password123' } });
    fireEvent.click(screen.getByText('Register'));
    expect(await screen.findByText('Registration failed')).toBeInTheDocument();
  });

  it('shows error message on network error', async () => {
    mockRegister.mockRejectedValue(new Error('Network error'));
    render(<Register />);
    fireEvent.change(screen.getByPlaceholderText('Email'), { target: { value: 'test@example.com' } });
    fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'password123' } });
    fireEvent.click(screen.getByText('Register'));
    expect(await screen.findByText('Registration error')).toBeInTheDocument();
  });
}); 