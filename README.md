# Weather API Fetcher 🌦️

Tiny Python script that pulls **current weather data** for any city using the [OpenWeatherMap API](https://openweathermap.org/api).

## What it does
- Calls OpenWeatherMap REST API
- Parses JSON into readable fields
- Prints results in a nice table

## Example
```bash
python weather_fetcher.py Doha --api-key YOUR_API_KEY
```

Output:
```
Weather in Doha 🌤️
| Metric           | Value |
|------------------|-------|
| Temperature (°C) | 41.2  |
| Feels Like (°C)  | 44.0  |
| Humidity (%)     | 52    |
| Pressure (hPa)   | 1008  |
| Wind Speed (m/s) | 3.5   |
```

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Notes
- You need a free API key from [openweathermap.org](https://home.openweathermap.org/users/sign_up).
- Works on Python 3.8+.

---

MIT License
