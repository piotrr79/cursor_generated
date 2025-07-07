import { AuthService } from './AuthService';

describe('AuthService', () => {
  let originalFetch: typeof fetch;
  let localStorageMock: any;
  const email = 'test@example.com';
  const password = 'password123';
  const token = 'jwt-token';

  beforeAll(() => {
    originalFetch = global.fetch;
    localStorageMock = (() => {
      let store: Record<string, string> = {};
      return {
        getItem: (key: string) => store[key] || null,
        setItem: (key: string, value: string) => { store[key] = value; },
        removeItem: (key: string) => { delete store[key]; },
        clear: () => { store = {}; },
      };
    })();
    Object.defineProperty(window, 'localStorage', { value: localStorageMock });
  });

  afterAll(() => {
    global.fetch = originalFetch;
  });

  it('registers a user', async () => {
    global.fetch = jest.fn().mockResolvedValue({ ok: true } as any);
    const response = await AuthService.getInstance().register(email, password);
    expect(response.ok).toBe(true);
    expect(global.fetch).toHaveBeenCalledWith('/api/auth/register/', expect.any(Object));
  });

  it('logs in and stores token', async () => {
    global.fetch = jest.fn().mockResolvedValue({
      ok: true,
      json: async () => ({ token }),
    } as any);
    const result = await AuthService.getInstance().login(email, password);
    expect(result).toBe(true);
    expect(localStorage.getItem('jwt_token')).toBe(token);
  });

  it('fails login with wrong credentials', async () => {
    global.fetch = jest.fn().mockResolvedValue({ ok: false } as any);
    const result = await AuthService.getInstance().login(email, password);
    expect(result).toBe(false);
  });

  it('logs out and removes token', () => {
    localStorage.setItem('jwt_token', token);
    AuthService.getInstance().logout();
    expect(localStorage.getItem('jwt_token')).toBeNull();
  });

  it('gets token from storage', () => {
    localStorage.setItem('jwt_token', token);
    expect(AuthService.getInstance().getToken()).toBe(token);
  });
}); 