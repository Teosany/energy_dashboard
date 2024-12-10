# Energy Dashboard

A Django application for analyzing and visualizing energy consumption data across French regions. This project was developed as a technical test demonstrating full-stack development capabilities with Django, Python, and data analysis.

## Features

- CSV data import through web interface
- Interactive visualization:
  - Regional consumption chart
  - Annual consumption chart
- Paginated data table
- Data export API
- Custom data analysis services:
  - Peak consumption detection
  - Custom data type sorting

## Technology Stack

- Django
- Tailwind CSS
- Tailwind UI (license)
- Chart.js
- SQLite3 (default)

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/teosany/energy_dashboard.git
cd energy_dashboard
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Setup Tailwind CSS:
```bash
cd theme/static_src
npm install
cd ../..
python manage.py tailwind start
```

5. Apply migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```
Follow the prompts to create admin user

7. Run development server:
```bash
python manage.py runserver
```

Visit:
- Main application: http://localhost:8000
- Admin interface: http://localhost:8000/admin

## API Usage

Export all data in JSON format:
```bash
curl http://localhost:8000/api/export/
```

Response example:
```json
[
    {
        "date": "2024-01-01",
        "region": "Île-de-France",
        "consumption": 10.5
    }
]
```

## Testing

Run tests:
```bash
python manage.py test
```

## License

MIT