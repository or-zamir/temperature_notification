# Temperature Notification
This project is a simple Python script that monitors the current weather in a specified location and notifies the user when the temperature exceeds a defined threshold (default: 25°C). If the user is idle for more than 10 seconds, it will continue to monitor the weather and send desktop notifications when it is too hot or cold.

![Weather Notification Image](https://github.com/user-attachments/assets/9130a86d-e99e-4b2f-b589-2034720c1294)

## Features

- Fetches the current temperature using the Python Weather API.
- Sends a desktop notification when the temperature exceeds or drops below a set value.
- Detects user inactivity and only checks the temperature when the user is not idle.
- Provides alerts when the weather becomes too hot and informs you when it cools down.

## How to Use

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/or-zamir/temperature_notification.git
   ```

2. **Install dependencies**:  
   You will need Python 3.x installed. Run the following command to install the necessary packages:  
   ```bash
   pip install python-weather desktop-notifier
   ```

3. **Run the script**:  
   Execute the script using Python:
   ```bash
   python hotdetector.py
   ```

   The script will check the temperature for the specified location and notify you if it exceeds the predefined threshold of 25°C.

## Configuration

- You can change the `MAX_TEMP` variable in the script to set the temperature threshold you want to receive notifications for:
  ```python
  MAX_TEMP = 30
  ```

- The location is controlled by the `CITY_NAME` variable. You can set this to any city of your choice:
  ```python
  CITY_NAME = 'New York'
  ```

## Dependencies

- `python-weather` for fetching the weather data.
- `desktop-notifier` for sending desktop notifications.
- The script is designed to work on Windows due to the use of the Windows API for idle detection.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
