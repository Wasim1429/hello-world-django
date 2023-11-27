# Hello World Django App

Simple Django app to display "Hello World!" in JSON and HTML formats.

## Quick Start

1. **Clone Repo**

   ```
   git clone https://github.com/Wasim1429/hello-world-django
   cd helloworld_project
   ```

2. **Install Django**

   ```
   pip install django
   ```

3. **Run Server**

   ```
   python manage.py runserver
   ```

4. **Visit URLs**
   - JSON: `http://localhost:8000/hello/json/`
   - HTML: `http://localhost:8000/hello/html/`

## Structure

- `helloworld_app/`
  - `templates/`: HTML templates.
  - `views.py`: View functions.
- `manage.py`: Django command-line utility.
