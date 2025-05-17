# Weather Dashboard CLI & Visualization

A simple Python project that fetches weather data using the OpenWeatherMap API and displays it in a command-line interface (CLI) as well as a visual dashboard using Matplotlib.

---

## Features

- **Auto-location detection** (based on IP)  
- Current weather details display: temperature, humidity, weather description  
- Hourly forecast visualization (next 24 hours)  
- 5-day forecast visualization showing high and low temperatures per day as a vertical range chart  
- Clean, organized dashboard layout with Matplotlib's `gridspec`  
- Modular code separated into CLI logic and dashboard visualization  

---

## How to Use

1. Obtain an OpenWeatherMap API key from [https://openweathermap.org/api](https://openweathermap.org/api).  
2. Make sure Python 3.x is installed along with required packages:

   ```bash
   pip install requests matplotlib
   ```
3. Run the CLI app to fetch weather data:
   ```
   python CLIapp.py
   ```
4. Run the Dashboard app to fetch weather data:
   ```
   python Dashboard.py
   ```

---

## Project Structure

- CLIapp.py - Contains functions for fetching location and weather data from the API.
- Dashboard.py - Uses Matplotlib to create a dashboard layout showing current weather, hourly forecast, and 5-day high-low temperature visualization.

---

## Notes

- This dashboard is a practice project to understand API interaction, data processing, and visualization in Python.
- The current visualization can be further improved aesthetically by adding icons, color gradients, interactive plots, and more detailed weather parameters.
- Feel free to fork and customize the project to suit your needs!

---

## ScreenShots
- CLI App
![image](https://github.com/user-attachments/assets/ac7dfc8c-f3c1-463c-8db6-d9356424797d)
- Dashboard App
![weather_dashboard](https://github.com/user-attachments/assets/a6c3e93b-d1a9-445a-97a3-4ed61e3ba069)

