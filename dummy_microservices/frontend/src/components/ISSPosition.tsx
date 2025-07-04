import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface ISSPositionProps {
  token: string;
}

const ISSPosition: React.FC<ISSPositionProps> = ({ token }) => {
  const [data, setData] = useState<any>(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchISS = async () => {
      try {
        const resp = await axios.get('http://localhost:8000/iss', {
          headers: { Authorization: `Bearer ${token}` },
        });
        setData(resp.data);
      } catch (err) {
        setError('Failed to fetch ISS position');
      }
    };
    fetchISS();
  }, [token]);

  if (error) return <div style={{ color: 'red' }}>{error}</div>;
  if (!data) return <div>Loading...</div>;

  let locationText = '';
  if (data.location_type === 'country') {
    locationText = `over ${data.location_name}`;
  } else if (data.location_type === 'sea') {
    locationText = `over the ${data.location_name}`;
  } else {
    locationText = 'over an unknown area';
  }

  return (
    <div>
      <div>Latitude: <b>{data.latitude}</b></div>
      <div>Longitude: <b>{data.longitude}</b></div>
      <div>The ISS is currently {locationText}.</div>
    </div>
  );
};

export default ISSPosition; 