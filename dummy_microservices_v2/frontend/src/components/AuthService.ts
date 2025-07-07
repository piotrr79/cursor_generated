/**
 * AuthService handles user authentication logic: registration, login, logout, and JWT storage.
 * Follows OOP and SOLID principles for modularity and testability.
 */
export class AuthService {
  private static instance: AuthService;
  private tokenKey = 'jwt_token';

  private constructor() {}

  /**
   * Singleton instance accessor.
   */
  public static getInstance(): AuthService {
    if (!AuthService.instance) {
      AuthService.instance = new AuthService();
    }
    return AuthService.instance;
  }

  /**
   * Registers a new user via the auth microservice.
   */
  async register(email: string, password: string): Promise<Response> {
    return fetch('/api/auth/register/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
  }

  /**
   * Logs in a user and stores the JWT token.
   */
  async login(email: string, password: string): Promise<boolean> {
    const response = await fetch('/api/auth/login/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    if (response.ok) {
      const data = await response.json();
      this.setToken(data.token);
      return true;
    }
    return false;
  }

  /**
   * Logs out the user by removing the JWT token.
   */
  logout(): void {
    localStorage.removeItem(this.tokenKey);
  }

  /**
   * Returns the stored JWT token, if any.
   */
  getToken(): string | null {
    return localStorage.getItem(this.tokenKey);
  }

  /**
   * Stores the JWT token securely.
   */
  private setToken(token: string): void {
    localStorage.setItem(this.tokenKey, token);
  }
} 