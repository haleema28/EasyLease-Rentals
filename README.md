# EasyLease & Rentals

A Django-based property rental and leasing platform that allows users to browse, book, and manage properties.

## Features

- Browse properties (1BHK to 3BHK)
- Filter properties by type (Rental/Lease) and price range
- View detailed property information with images
- Add properties to wishlist
- Book properties with security deposit
- View booking history
- Admin panel for property management

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/easyleaseandrentals.git
cd easyleaseandrentals
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Access the website at `http://localhost:8000`

## Usage

1. Access the admin panel at `http://localhost:8000/admin` and log in with your superuser credentials
2. Add properties through the admin panel
3. Browse properties at `http://localhost:8000`
4. Register an account to book properties and manage your wishlist

## Demo Credentials

-username: root
-password: root123456789

## Project Structure

- `properties/` - Main app directory
  - `models.py` - Database models
  - `views.py` - View functions
  - `urls.py` - URL patterns
  - `forms.py` - Form classes
  - `admin.py` - Admin interface
- `templates/` - HTML templates
  - `base.html` - Base template
  - `properties/` - Property-related templates
  - `registration/` - Authentication templates
- `static/` - Static files (CSS, JS, images)
- `media/` - User-uploaded files

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
