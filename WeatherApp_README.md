
# WeatherApp

The WeatherApp is a Python application built with Tkinter for GUI. It allows users to view the current weather of pre-selected cities, manage preferences like temperature units, severe weather notifications, and background colors, and even update the API key via a management console.

## Features

- Displays the current temperature for five cities (Paris, Rome, Lagos, Tokyo, New York).
- Allows users to toggle between Fahrenheit and Celsius for temperature display.
- Supports enabling/disabling severe weather notifications.
- Provides an option to customize the background color.
- Includes a management console for updating the API key.
- Alerts feature for displaying severe weather notifications (if available for a city).

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3.x installed on your system.
3. Install the required libraries:
   ```bash
   pip install requests
   ```
4. Place the required image files (e.g., `weatherBackground.png`, `notification.png`, and city-specific images like `paris.png`) in the same directory as the code.

## Usage

1. Run the application:
   ```bash
   python weatherApp.py
   ```
2. Use the "Preferences" button to:
   - Change the temperature unit (Fahrenheit or Celsius).
   - Enable or disable severe weather notifications.
   - Customize the background color.
3. To manage the API key, open the management console from the application and enter the new API key. This ensures the app continues to fetch weather data seamlessly.
4. Click on city icons to view the temperature and weather alerts (if any).

## Management Console for API Key

The application includes a management console that allows you to update the API key without modifying the source code. Simply access the console, input the new API key, and save it. The application will use the updated key for all subsequent weather data requests.

## Notes

- The application uses the OpenWeatherMap API to fetch weather data. Ensure you have a valid API key.
- If you encounter any issues, double-check the API key and ensure you have a stable internet connection.

## Future Improvements

- Add the ability to dynamically add or remove cities.
- Enhance the user interface with additional themes.
- Add localization for supporting multiple languages.
