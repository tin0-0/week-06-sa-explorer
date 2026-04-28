"""
SA Weather CLI — WeatherClient class.

Build a class that models an API client. Focus on CLASS STRUCTURE:
- Class attribute CITIES (dict of 5+ SA cities with lat/lon tuples)
- Instance attribute timeout (default 10 seconds)
- fetch_current(city_name) validates the city and returns a dict or None
- list_cities() returns a list of city names

The actual HTTP call happens in your local VS Code using requests.
Here we test the logic, structure, and validation.
"""


class WeatherClient:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    # TODO: Add at least 5 SA cities as a class attribute
    # Format: "City Name": (latitude, longitude)
    # Suggested: Johannesburg, Cape Town, Durban, Pretoria, Port Elizabeth
    CITIES = {}

    def __init__(self, timeout=10):
        # TODO: store timeout as instance attribute
        pass

    def list_cities(self):
        """Return a list of supported SA city names."""
        # TODO: return the keys of CITIES as a list
        pass

    def fetch_current(self, city_name):
        """Return weather data dict for a city, or None on failure/unknown city."""
        # TODO:
        # 1. Check if city_name is in self.CITIES — if not, return None
        # 2. For this interactive test, return a stub dict:
        #    {"city": city_name, "temperature_2m": 20.0, "source": "stub"}
        # 3. In your real Thursday build, replace step 2 with requests.get(url)
        pass


# Demo usage (students can test here):
if __name__ == "__main__":
    client = WeatherClient()
    print("Supported cities:", client.list_cities())
    print("Cape Town weather:", client.fetch_current("Cape Town"))
    print("Unknown city:", client.fetch_current("Atlantis"))
