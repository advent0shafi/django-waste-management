# Django Scrap Collection App

## Overview

This Django application is designed to manage scrap collection requests, orders, and collections. It provides a RESTful API for interacting with scraps, scrap orders, and collected scraps. Users can submit scrap collection requests, track their orders, and workers can fulfill these orders and record the collections.

## Features

- CRUD operations for scraps, scrap orders, and collected scraps
- User authentication and authorization
- Image uploads for scrap items
- Automatic timestamp recording for order creation and collection

## Setup

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- Pillow (for handling image uploads)

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <project-directory>

2. Create a virtual environment:

   ```bash
   python3 -m venv env

3. Activate the virtual environment:

   ```bash
   \env\Scripts\activate

4. Install dependencies:
   
   ```bash
   pip install -r requirements.txt


5. Run database migrations:
   
   ```bash
   python manage.py migrate

6. Start the development server:
   
   ```bash 
   python manage.py runserver

License
This project is licensed under the MIT License.

javascript
Copy code

You can use this content as your `README.md` file.

