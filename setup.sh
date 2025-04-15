#!/bin/bash

# Create directories
mkdir -p customer_app/app/templates

# Create empty Python files
touch customer_app/app/__init__.py
touch customer_app/app/routes.py
touch customer_app/app/models.py
touch customer_app/run.py

# Create template HTML files
touch customer_app/app/templates/login.html
touch customer_app/app/templates/signup.html
touch customer_app/app/templates/dashboard.html

# Create config and environment files
touch customer_app/.env
touch customer_app/config.py
touch customer_app/requirements.txt

# Create Docker-related files
touch customer_app/Dockerfile
touch customer_app/docker-compose.yml

echo "Project structure created successfully!"

