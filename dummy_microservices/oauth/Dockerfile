FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Install nginx
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# Copy nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Expose ports
EXPOSE 8001 80

# Start both Nginx and Uvicorn
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8001 & nginx -g 'daemon off;'"] 