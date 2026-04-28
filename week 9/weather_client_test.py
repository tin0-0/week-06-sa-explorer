import weather_client

def test_client_has_cities():
    # Use FileName.ClassName()
    c = weather_client.WeatherClient()
    
    
    assert "Johannesburg" in c.list_CITIES() 
    print("Test 1 Passed!")

def test_unknown_city_returns_none():
    c = weather_client.WeatherClient()
    assert c.fetch_current("Atlantis") is None
    print("Test 2 Passed!")

# Run the tests manually
test_client_has_cities()
test_unknown_city_returns_none()
