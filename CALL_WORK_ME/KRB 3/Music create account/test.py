# Importing required module
from geopy.geocoders import Nominatim

# Using Nominatim Api
geolocator = Nominatim(user_agent="geoapiExercises")
from faker import Faker

f = Faker(["fr_FR"])
print(f.name() + "\n***********")
address, ZipCodeAndCity = str(f.address()).split("\n")
ZipCode = ZipCodeAndCity.split(" ", 1)[0]
# Zipcode input
# zipcode = "800011"

# Using geocode()
location = geolocator.geocode(ZipCode)

# Displaying address details
print("Zipcode:", ZipCode)
print("Details of the Zipcode:")
print(location)