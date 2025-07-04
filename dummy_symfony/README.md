# Dummy Symfony ISS API

This Symfony application exposes an API endpoint to get the current position of the International Space Station (ISS), including the country or sea/ocean it is currently over.

## Structure
- `src/Service/ISSService.php`: Service for fetching ISS position and reverse geocoding
- `src/Controller/ISSController.php`: API controller for the `/iss` endpoint
- `public/ui.html`: Simple UI to interact with the API

## How to Run

1. Install dependencies:
   ```bash
   composer install
   ```
2. Start the Symfony local server:
   ```bash
   symfony server:start
   ```
   Or with PHP's built-in server:
   ```bash
   php -S localhost:8000 -t public
   ```
3. Access the API at [http://localhost:8000/iss](http://localhost:8000/iss)
4. Open `public/ui.html` in your browser to use the UI.

---

This project is a refactor of the original PHP ISS logic into the Symfony framework. 