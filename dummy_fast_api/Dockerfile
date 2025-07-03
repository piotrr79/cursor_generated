FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install nginx and openssl
RUN apt-get update && \
    apt-get install -y nginx openssl && \
    rm -rf /var/lib/apt/lists/*

# Generate self-signed SSL certificate
RUN mkdir -p /etc/ssl/certs /etc/ssl/private && \
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/fastapi.key \
    -out /etc/ssl/certs/fastapi.crt \
    -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=localhost"

# Copy Nginx config
COPY nginx.conf /etc/nginx/nginx.conf

COPY . .

# Entrypoint script to run both Nginx and Uvicorn
COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"] 