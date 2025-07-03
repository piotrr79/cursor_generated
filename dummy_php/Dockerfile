FROM php:8.2-fpm

# Install Nginx and supervisor
RUN apt-get update && \
    apt-get install -y nginx supervisor && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Composer
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

# Set up document root
WORKDIR /var/www/html
COPY . /var/www/html

# Copy nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Configure supervisor to run both Nginx and PHP-FPM
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80
CMD ["/usr/bin/supervisord"] 