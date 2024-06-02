# Weather App

This is a simple weather application built using Python's `tkinter` for the GUI and OpenWeatherMap API for fetching weather data.

## Files

- `weather.py`: Contains the logic for fetching latitude/longitude and weather data.
- `weather_app.py`: The main GUI application using `tkinter`.
- `README.md`: This documentation file.
- `requirements.txt`: List of required Python packages.

## Setup and Installation

### Prerequisites

- Python 3.x installed on your system.
- `tkinter` (comes pre-installed with Python on most systems).

### Installation Steps

1. **Clone the Repository**:
    ```sh
    git clone <repository_url>
    cd weather_app
    ```

2. **Install Required Packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Replace API Key**:
    - Open `weather.py` and replace `"Your API"` with your actual OpenWeatherMap API key.

### Running the Application

Run the following command to start the GUI application:
```sh
python weather_app.py
