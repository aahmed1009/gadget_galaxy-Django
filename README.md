# Gadget Galaxy

Gadget Galaxy is a Django-based web application that provides complete CRUD functionality for product and category management, along with user authentication and email verification using Celery and Redis.

---

## Features

* User registration with email verification
* User login and logout
* Password validation
* Category CRUD using Django class-based generic views
* Product listing, creation, and soft delete
* Celery and Redis for asynchronous email sending
* Responsive Bootstrap design

---

## Screenshots

### Register Page

![Register](screenshots/register.png)

### Email Verification

![Email](screenshots/activation_email.png)
![Email](screenshots/activation_email2.png)
![Email](screenshots/activation_email3.png)

### Login Page

![Login](screenshots/login.png)
![Login](screenshots/login2.png)

### Product List

![Products](screenshots/product_list.png)

### Category List

![Categories](screenshots/category_list.png)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/gadget_galaxy.git
cd gadget_galaxy
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your `.env` or `settings.py`

Update email backend and credentials for Gmail or SMTP service.

### 5. Setup Redis (required for Celery)

```bash
sudo apt update && sudo apt install redis-server
sudo service redis-server start
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Start Celery worker

```bash
celery -A gadget_galaxy worker -l info
```

### 8. Run the development server

```bash
python manage.py runserver
```

---

## Project Structure

```
gadget_galaxy/
├── gadget_galaxy/       # Project settings
├── product/             # Product app
├── category/            # Category app
├── user/                # User registration/login
├── templates/           # HTML templates
├── static/              # CSS and JS files
└── README.md            # Project documentation
```

---

## Author

Developed by Alaa - [3la2.a7med60@gmail.com](mailto:3la2.a7med60@gmail.com)

---

## License

MIT License
