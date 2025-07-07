import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import ISSPosition from './ISSPosition';
import { ISSService } from './ISSService';
import { AuthService } from './AuthService';

jest.mock('./ISSService');
jest.mock('./AuthService');

const mockGetISSPosition = jest.fn();
const mockGetToken = jest.fn();
(ISSService.getInstance as jest.Mock).mockReturnValue({ getISSPosition: mockGetISSPosition });
(AuthService.getInstance as jest.Mock).mockReturnValue({ getToken: mockGetToken });

describe('ISSPosition component', () => {
  beforeEach(() => {
    mockGetISSPosition.mockReset();
    mockGetToken.mockReset();
  });

  it('shows loading initially', () => {
    mockGetToken.mockReturnValue('token');
    render(<ISSPosition />);
    expect(screen.getByText('Loading ISS position...')).toBeInTheDocument();
  });

  it('shows error if not authenticated', async () => {
    mockGetToken.mockReturnValue(null);
    render(<ISSPosition />);
    expect(await screen.findByText('Not authenticated')).toBeInTheDocument();
  });

  it('shows ISS position data on success', async () => {
    mockGetToken.mockReturnValue('token');
    mockGetISSPosition.mockResolvedValue({
      latitude: '10.0',
      longitude: '20.0',
      location_type: 'country',
      location_name: 'Testland',
    });
    render(<ISSPosition />);
    expect(await screen.findByText('Current ISS Position')).toBeInTheDocument();
    expect(screen.getByText('Latitude: 10.0')).toBeInTheDocument();
    expect(screen.getByText('Longitude: 20.0')).toBeInTheDocument();
    expect(screen.getByText('Location Type: country')).toBeInTheDocument();
    expect(screen.getByText('Location Name: Testland')).toBeInTheDocument();
  });

  it('shows error on fetch failure', async () => {
    mockGetToken.mockReturnValue('token');
    mockGetISSPosition.mockRejectedValue(new Error('Failed to fetch ISS position'));
    render(<ISSPosition />);
    expect(await screen.findByText('Failed to fetch ISS position')).toBeInTheDocument();
  });
}); 