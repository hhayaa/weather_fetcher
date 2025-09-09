#!/usr/bin/env python3
"""
Weather API Fetcher
-------------------

Fetch current weather data from OpenWeatherMap API
and print it in a clean table.
"""

import requests
from tabulate import tabulate

API_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city: str, api_key: str):
    params = {"q": city, "appid": api_key, "units": "metric"}
    r = requests.get(API_URL, params=params)
    r.raise_for_status()
    return r.json()

def format_weather(data):
    main = data["main"]
    wind = data["wind"]
    rows = [
        ["Temperature (°C)", main["temp"]],
        ["Feels Like (°C)", main["feels_like"]],
        ["Humidity (%)", main["humidity"]],
        ["Pressure (hPa)", main["pressure"]],
        ["Wind Speed (m/s)", wind["speed"]],
    ]
    return tabulate(rows, headers=["Metric", "Value"], tablefmt="github")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Fetch weather for a city")
    parser.add_argument("city", help="City name (e.g. Doha)")
    parser.add_argument("--api-key", required=True, help="OpenWeatherMap API key")
    args = parser.parse_args()

    try:
        data = fetch_weather(args.city, args.api_key)
        print(f"Weather in {args.city} 🌤️")
        print(format_weather(data))
    except Exception as e:
        print("Error fetching weather:", e)
