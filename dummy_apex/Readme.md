# Dummy Apex ISS API

This project provides a simple Salesforce Apex REST API:
- `/services/apexrest/hello` — returns "Hello World"
- `/services/apexrest/iss` — returns the current ISS position and the country over which it is located (using external APIs)

## Files
- `IssService.cls` — Apex class for ISS logic and country lookup
- `IssApi.cls` — Apex REST API for `/iss` endpoint
- `HelloApi.cls` — Apex REST API for `/hello` endpoint
- `IssServiceTest.cls` — Apex test class with HTTP callout mocks

## Deployment
1. Deploy all `.cls` files to your Salesforce org (use SFDX, Workbench, or Developer Console).
2. Ensure "Apex REST Services" is enabled in your org.

## Usage
- **Hello World:**
  - `GET /services/apexrest/hello`
- **ISS Info:**
  - `GET /services/apexrest/iss`
  - Returns JSON: `{ "latitude": "...", "longitude": "...", "country": "..." }`

## Testing
- Run all tests in `IssServiceTest.cls` via Salesforce Setup > Apex Test Execution, or using SFDX:
  ```bash
  sfdx force:apex:test:run -c -r human -t IssServiceTest
  ```
- The test class mocks all HTTP callouts and does not perform real API requests.

## Notes
- The `/iss` endpoint depends on external APIs and may be rate-limited in production.
- For production use, consider error handling and governor limits for HTTP callouts. 