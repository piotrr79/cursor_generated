FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Install nginx
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# Copy nginx config
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 8002 80

CMD ["sh", "-c", "gunicorn auth_service.wsgi:application --bind 0.0.0.0:8002 & nginx -g 'daemon off;'"] 