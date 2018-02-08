import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyBuUF2LTfdHTmbxmoVRRnYYFlyR-jCCgyQ')

# Geocoding an address
geocode_result = gmaps.geocode('NSIT Dwarka Sector 3 , New Delhi')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="driving",
                                     departure_time=now)
print directions_result
