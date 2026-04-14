coordinates = ("joburg",-26.2041, 28.0473)
college = ("college",-26.1109365, 27.8023829)
print(coordinates)
city, lat, lon = coordinates
print(lat,lon)
# coordinates[0] = 0  # This would cause an error since tuples are immutable

lat=0
print(city, lat, lon) # The original coordinates remain unchanged since tuples are immutable