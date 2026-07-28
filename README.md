# Weather App

A simple Python weather application that retrieves current weather information for a city using the WeatherAPI service. The project includes both a command-line interface and a desktop graphical user interface built with Tkinter.

## Features

- Search weather for any city
- Display current conditions, temperature, feels-like temperature, humidity, wind speed, and chance of rain
- Support for both a terminal-based CLI and a GUI version

## Project Structure

- src/cli.py - Command-line version of the app
- src/gui.py - Tkinter-based graphical interface
- src/weather_api.py - API requests, response handling, and weather data formatting
- requirements.txt - Python dependencies

## Requirements

- Python 3.8+
- A WeatherAPI.com API key

## Installation

1. Clone the repository
2. Create and activate a virtual environment (recommended)
3. Install the dependencies:

```bash
pip install -r requirements.txt
pip install python-dotenv
```

4. Create a .env file in the project root with your WeatherAPI key:

```env
API_KEY=your_weatherapi_key_here
```

## Usage

Run the command-line version:

```bash
python src/cli.py
```

Run the graphical interface:

```bash
python src/gui.py
```

When prompted in the CLI, enter a city name and the app will print the current weather information.

## Notes

- The app uses the WeatherAPI current weather endpoint.
- Invalid city names or missing API keys will produce an error message.
- Make sure your API key is valid and that the .env file is present before running the app.
