import { ISSService } from './ISSService';

describe('ISSService', () => {
  const token = 'test-token';
  let originalFetch: typeof fetch;

  beforeAll(() => {
    originalFetch = global.fetch;
  });

  afterAll(() => {
    global.fetch = originalFetch;
  });

  it('fetches ISS position successfully', async () => {
    const mockResponse = {
      latitude: '10.0',
      longitude: '20.0',
      location_type: 'country',
      location_name: 'Testland',
    };
    global.fetch = jest.fn().mockResolvedValue({
      ok: true,
      json: async () => mockResponse,
    } as any);
    const result = await ISSService.getInstance().getISSPosition(token);
    expect(result).toEqual(mockResponse);
    expect(global.fetch).toHaveBeenCalledWith('/api/backend/iss', {
      headers: { Authorization: `Bearer ${token}` },
    });
  });

  it('throws error on failed fetch', async () => {
    global.fetch = jest.fn().mockResolvedValue({ ok: false } as any);
    await expect(ISSService.getInstance().getISSPosition(token)).rejects.toThrow('Failed to fetch ISS position');
  });
}); 