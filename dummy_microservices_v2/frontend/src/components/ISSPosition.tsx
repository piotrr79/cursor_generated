import React, { useEffect, useState } from 'react';
import { ISSService } from './ISSService';
import { AuthService } from './AuthService';

/**
 * ISSPosition component fetches and displays the current ISS position and geolocation.
 * Uses ISSService for data and AuthService for JWT token.
 */
const ISSPosition: React.FC = () => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      setError(null);
      try {
        const token = AuthService.getInstance().getToken();
        if (!token) {
          setError('Not authenticated');
          setLoading(false);
          return;
        }
        const result = await ISSService.getInstance().getISSPosition(token);
        setData(result);
      } catch (err: any) {
        setError(err.message || 'Failed to fetch ISS position');
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  if (loading) return <div>Loading ISS position...</div>;
  if (error) return <div className="error">{error}</div>;
  if (!data) return null;

  return (
    <div className="iss-position-container">
      <h2>Current ISS Position</h2>
      <ul>
        <li>Latitude: {data.latitude}</li>
        <li>Longitude: {data.longitude}</li>
        <li>Location Type: {data.location_type}</li>
        <li>Location Name: {data.location_name}</li>
      </ul>
    </div>
  );
};

export default ISSPosition; 