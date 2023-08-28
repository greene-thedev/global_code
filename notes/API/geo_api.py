from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="CG Test")
newYorkCity = geolocator.geocode(input("Enter first location: "))
washingtonDc = geolocator.geocode(input("Enter second location: "))

x = (newYorkCity.latitude, newYorkCity.longitude)
y = (washingtonDc.latitude, washingtonDc.longitude)

print(geodesic(x, y).miles)
