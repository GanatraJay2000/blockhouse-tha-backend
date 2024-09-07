# Django API Backend

This is a simple Django REST API that provides hardcoded data for Candlestick, Line, Bar, and Pie charts. The API is integrated with a Next.js frontend for dynamic chart rendering.

## Requirements

- Python 3.x
- Django 4.x
- Django REST Framework

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/GanatraJay2000/blockhouse-tha-backend.git
   cd blockhouse-tha-backend
   ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv env
   source env/bin/activate  # Linux/MacOS
   env\Scripts\activate  # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Django server**:

   ```bash
   python manage.py runserver
   ```

   The server will start on `http://127.0.0.1:8000`.

## API Endpoints

The following API endpoints are available:

- **Candlestick Data**: `/api/candlestick-data/`
- **Line Chart Data**: `/api/line-chart-data/`
- **Bar Chart Data**: `/api/bar-chart-data/`
- **Pie Chart Data**: `/api/pie-chart-data/`

All data is hardcoded and follows the structure expected by charting libraries.

### Example Response

- **Candlestick Data**:
  ```json
  {
    "data": [
      { "x": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35 },
      { "x": "2023-01-02", "open": 35, "high": 45, "low": 30, "close": 40 }
    ]
  }
  ```

## Tools and Libraries Used

- **Django**: Web framework for building the backend.
- **Django REST Framework**: Toolkit for building Web APIs.

## Thought Process

This backend was built with simplicity in mind. The data for the charts is hardcoded to keep the focus on API integration with the Next.js frontend. The Django REST framework was used for API management because it provides quick and easy-to-use tools for serializing data and responding to client requests.
