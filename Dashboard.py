import CLIapp
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from collections import defaultdict

# === Dashboard ===
fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(3, 1, height_ratios=[1, 2, 2])

info_ax = fig.add_subplot(gs[0])
hourly_ax = fig.add_subplot(gs[1])
daily_ax = fig.add_subplot(gs[2])

if __name__ == '__main__':
    city = CLIapp.getLocation()
    if city == None:
        print("City Not Found!")
        exit()
    else:
        forecast_data = CLIapp.getForecast(city, CLIapp.API_KEY)
        forecast_list = forecast_data

        # === Formatting info_ax ===
        current = forecast_list[0]['main']
        weather = forecast_list[0]['weather'][0]
        info_ax.axis("off")
        info_ax.text(0.01, 0.7, f"📍 City: {city}", fontsize=14)
        info_ax.text(0.01, 0.4, f"🌡 Temp: {current['temp']}°C", fontsize=14)
        info_ax.text(0.4, 0.4, f"💧 Humidity: {current['humidity']}%", fontsize=14)
        info_ax.text(0.7, 0.4, f"☁️ {weather['description'].capitalize()}", fontsize=14)

        # === Formatting hourly_ax ===
        times = [item['dt_txt'][11:16] for item in forecast_list[:8]]
        temps = [item['main']['temp'] for item in forecast_list[:8]]

        hourly_ax.plot(times, temps, marker='o', color='tomato')
        hourly_ax.set_title("Hourly Forecast")
        hourly_ax.set_ylabel("Temp (°C)")

        # === Formatting daily_ax ===
        day_temps = defaultdict(list)
        for item in forecast_list:
            date = item['dt_txt'].split()[0]
            day_temps[date].append(item['main']['temp'])

        dates = list(day_temps.keys())[:5]
        highs = [max(day_temps[d]) for d in dates]
        lows = [min(day_temps[d]) for d in dates]

        daily_ax.clear()
        for i, (date, high, low) in enumerate(zip(dates, highs, lows)):
            daily_ax.plot([i, i], [low, high], color='royalblue', linewidth=4)
            daily_ax.plot(i, high, 'o', color='red')   # Max temp
            daily_ax.plot(i, low, 'o', color='blue')   # Min temp

        daily_ax.set_xticks(range(len(dates)))
        daily_ax.set_xticklabels(dates, rotation=45)
        daily_ax.set_title("5-Day Forecast (High/Low Temps)")
        daily_ax.set_ylabel("Temp (°C)")

        # === Showing Plot ===
        plt.tight_layout()
        plt.savefig("weather_dashboard.png")
        plt.show()
