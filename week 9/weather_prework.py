import requests

def fetch_weather(lat, lon, timeout=10):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,weather_code"
    )
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.Timeout:
        print(f"Request to {url} timed out")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e.response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None


CITIES = {
    "Johannesburg": (-26.2041, 28.0473),
    "Cape Town":    (-33.9249, 18.4241),
    "Durban":       (-29.8587, 31.0218),
}

for name, (lat, lon) in CITIES.items():
    data = fetch_weather(lat, lon)
    if data and "current" in data:
        temp = data["current"].get("temperature_2m")
        print(f"{name}: {temp}°C")
    else:
        print(f"{name}: weather unavailable")