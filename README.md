# Django E-Commerce Platform

## Overview

This project is a fully functional e-commerce web application built using Django and PostgreSQL. It features user authentication, product listings, and a custom shopping cart system. The architecture is designed for scalability and ease of future integration with features such as checkout, orders, and payment gateways.

---

## Features

### User Authentication
- Secure user signup, login, and logout
- Session-based authentication to maintain user sessions
- Role-based access control to manage feature access for different user types (e.g., regular users vs. admins)

### Product Management
- Product listing pages rendered using Django Templates
- Display of images, descriptions, and pricing
- Backend controlled by Django ORM models for clean, scalable schema design

### Shopping Cart
- Custom `CartItem` model linked to each user session
- Add, update, and remove items with quantity support
- Robust session-aware logic for managing cart state across requests
- Clean database handling for future integration with order and payment systems

### Frontend
- Fully responsive layout using Django Templates, HTML, and CSS
- Dynamic rendering of user-specific content
- Mobile-friendly design with consistent UX

---

## Tech Stack

| Layer        | Technology                                |
|--------------|--------------------------------------------|
| Backend      | Django                                     |
| Frontend     | Django Templates, HTML, CSS                |
| Database     | PostgreSQL                                 |
| Auth System  | Session-based Authentication               |
| Cart Logic   | Custom CartItem model + session state      |

---

## Project Structure

'''ecommerce/
├── accounts/ # User registration and authentication
├── cart/ # Cart management logic
├── panther_store/ # Product listing and detail views
├── templates/ # HTML templates (Django Template Engine)
├── static/ # Static assets (CSS, images)
├── manage.py # Django entry point
├── requirements.txt # Python dependencies'''

# Setup Instructions

Follow these steps to set up and run the Django E-Commerce platform locally.

---

## 1. Clone the Repository

```bash
git clone https://github.com/Thamil2725/DjangoEcommerce.git
cd DjangoEcommerce
```

---

## 2. Create and Activate a Virtual Environment

### On macOS/Linux:
```bash
python3 -m venv myVenv
source myVenv/bin/activate
```

### On Windows:
```bash
python -m venv myVenv
myVenv\Scripts\activate
```

---

## 3. Install Project Dependencies

```bash
pip install -r requirements.txt
```

> Make sure you have `pip` and Python 3.8+ installed.

---

## 4. Set Up the Database

### PostgreSQL Configuration:
Ensure PostgreSQL is installed and running. Then create a database and update the database configuration in `settings.py`:

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

> Alternatively, you can use SQLite during development by reverting to the default SQLite settings in `settings.py`.

---

## 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 6. Create a Superuser (for admin access)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin credentials.

---

## 7. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the app running.

---

## 8. Access the Admin Panel

Visit `http://127.0.0.1:8000/admin/` and log in using the superuser credentials.

---

## Optional: Collect Static Files (for production)

```bash
python manage.py collectstatic
```

---

## Troubleshooting

- Make sure PostgreSQL service is running
- Check your environment variables and database credentials
- If using `.env`, make sure it's loaded in `settings.py`

---


