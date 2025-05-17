import requests 
import json

API_KEY = "00c55e7ab4b6229d403afc0149541d9a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# === Getting approx Location via IP Address ===
def getLocation():
    try:
        res = requests.get("http://ip-api.com/json/")
        data = res.json()
        return data.get('city')
    except:
        print("Could not Detect Location Automatically!")
        return None

# === Getting Cordinates from City ===
def getCoordinates(city, api_key):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {'q': city, 'limit': 1, 'appid': api_key}
    res = requests.get(url, params=params).json()
    if res:
        return res[0]['lat'], res[0]['lon']
    else:
        raise Exception("City not found")

# === Getting Forecast of every 3rd Hour ===
def getForecast(city,api_key):
    url = "https://api.openweathermap.org/data/2.5/forecast"
    lat , lon = getCoordinates(city, api_key)
    params = {'lat': lat, 'lon': lon, 'appid': api_key, 'units': 'metric'}
    res = requests.get(url, params=params).json()
    return res['list']  # List of forecasts every 3 hours

# === Getting Weather Data ===
def getWeather(city):
    
    # === Parameters (Defined by OpenWeatherMap API) ===
    params = {
        'q': city,
        'appid': API_KEY,
        'units': "metric"
    }
    
    # === Getting JSON Output and Conversion to Dictionary with Response Handling ===
    response = requests.get(BASE_URL,params=params)

    if response.status_code == 200:
        data = response.json()
        printWeather(data)
    elif response.status_code == 404:
        print("404 Error. City not found!")
    else:
        print("Error fetching data...")


# === Reading and Printing the Weather ===
def printWeather(data):

    # Reading and Storing Weather
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    weather = data['weather'][0]['description'].title()
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    # Printing Weather
    print(f"\n🌤 Weather in {city}, {country}:")
    print(f"🌡 Temperature: {temp}°C (Feels like {feels_like}°C)")
    print(f"☁ Condition: {weather}")
    print(f"💧 Humidity: {humidity}%")
    print(f"💨 Wind Speed: {wind_speed} m/s\n")

# === Main Function ===
def main():
    print("🌍 Welcome to Weather CLI")
    city = getLocation()

    if city:
        print(f"Detected location: {city}")
        user_input = input(f"Press Enter to use this, or type a different city: ")
        if user_input.strip():
            city = user_input.strip()
    else:
        city = input("Enter your city: ")

    getWeather(city)


#main()