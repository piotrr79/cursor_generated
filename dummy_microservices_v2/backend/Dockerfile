FROM python:3.11-slim AS base

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Install system dependencies with security updates
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    nginx \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY --chown=appuser:appuser app ./app
COPY --chown=appuser:appuser start.sh .
COPY nginx.conf /etc/nginx/nginx.conf

# Set proper permissions
RUN chmod +x start.sh \
    && chown -R appuser:appuser /app \
    && mkdir -p /var/log/nginx /var/lib/nginx \
    && chown -R appuser:appuser /var/log/nginx /var/lib/nginx

# Expose ports
EXPOSE 80
EXPOSE 8000

# Switch to non-root user
USER appuser

CMD ["./start.sh"]