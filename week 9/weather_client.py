import requests

class WeatherClient:
    DEFAULT_TIMEOUT = 10
    BASE_URL = "https://api.open-meteo.com/v1/forecast"
    CITIES = {
        "Johannesburg": (-26.2041, 28.0473),
        "Cape Town":    (-33.9249, 18.4241),
        "Durban":       (-29.8587, 31.0218),
        "Pretoria":     (-25.7479, 28.2293),
        "Port Elizabeth": (-33.9608, 25.6022),
    }
    def __init__(self, timeout=DEFAULT_TIMEOUT):
        """Store timeout as instance attribute."""
        self.timeout = timeout

    def list_CITIES(self):
        """Return a list of supported SA city names."""
        return list(self.CITIES.keys())

    def fetch_current(self, city_name) -> dict:
        """Return weather data dict for a city, or None on failure."""
        if city_name not in self.CITIES:
            return None
        lat, lon = self.CITIES[city_name]
        url = f"{self.BASE_URL}?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code"
        try:
            r = requests.get(url, timeout=self.timeout) 
            r.raise_for_status()
            return r.json()
        except (requests.exceptions.RequestException, ValueError):
            return None

   
if __name__ == "__main__":
    client = WeatherClient()
    print("Supported cities:", client.list_CITIES())
    
    # Extract just the temperature from the response
    data = client.fetch_current("Cape Town")
    if data:
        print(f"Cape Town temperature: {data['current']['temperature_2m']}°C")
    
    print("Unknown city:", client.fetch_current("Atlantis"))

