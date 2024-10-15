#### Ecommerce API

## Table of Contents
- Overview
- Features
- Requirements
- Installation
- API Endpoints
- Models
- Serializers
- Admin Interface

## Overview
This is an ecommerce API built using Django and Django Rest Framework. The API provides endpoints for managing products, users, and categories.

## Features
- Product management: create, read, update, and delete products
- User management: create, read, update, and delete users
- Category management: create, read, update, and delete categories
- Authentication and authorization using Django's built-in auth system

## Requirements
- Python 3.8+
- Django 5.0.7
- Django Rest Framework 3.15.2
- Django-filter 24.3
- Django-taggit 6.0.0
- PyJWT 2.9.0

## Installation
- Clone the repository: git clone https://github.com/your-username/ecommerce-api.git
- Install the requirements: pip install -r requirements.txt
- Run the migrations: python manage.py migrate
- Create a superuser: python manage.py createsuperuser

## API Endpoints
# Products
- GET /products/: List all products
- POST /products/: Create a new product
- GET /products/{id}/: Retrieve a product by ID
- PUT /products/{id}/: Update a product by ID
- DELETE /products/{id}/: Delete a product by ID

# Users
- GET /users/: List all users
- POST /users/: Create a new user
- GET /users/{id}/: Retrieve a user by ID
- PUT /users/{id}/: Update a user by ID
- DELETE /users/{id}/: Delete a user by ID

# Categories
- GET /categories/: List all categories
- POST /categories/: Create a new category
- GET /categories/{id}/: Retrieve a category by ID
- PUT /categories/{id}/: Update a category by ID
- DELETE /categories/{id}/: Delete a category by ID

## Models
The API uses the following models:

- Product: represents a product with attributes such as name, description, price, and category
- User: represents a user with attributes such as username, email, and password
- Category: represents a category with attributes such as name

## Serializers
The API uses the following serializers:

- ProductSerializer: serializes a product instance
- UserSerializer: serializes a user instance
- CategorySerializer: serializes a category instance

## Admin Interface
The API provides an admin interface for managing products, users, and categories. To access the admin interface, navigate to http://localhost:8000/admin/ and log in with the superuser credentials.

