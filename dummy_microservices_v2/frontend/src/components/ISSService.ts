/**
 * ISSService handles fetching the current ISS position and geolocation from the backend API.
 * Follows OOP and SOLID principles for modularity and testability.
 */
export class ISSService {
  private static instance: ISSService;

  private constructor() {}

  /**
   * Singleton instance accessor.
   */
  public static getInstance(): ISSService {
    if (!ISSService.instance) {
      ISSService.instance = new ISSService();
    }
    return ISSService.instance;
  }

  /**
   * Fetches the current ISS position and geolocation from the backend API.
   * Requires a valid JWT token for authentication.
   */
  async getISSPosition(token: string): Promise<any> {
    const response = await fetch('/api/backend/iss', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    if (!response.ok) {
      throw new Error('Failed to fetch ISS position');
    }
    return response.json();
  }
} 