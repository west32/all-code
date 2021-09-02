import geopy
import requests

def run_example():
    address = "ul. Milberta 6, 27-600 Sandomierz"
    geolocator = geopy.Nominatim(user_agent="webinar=agent")
    adress_code= geolocator.geocode(address)

    print(adress_code.latitude)
    print(adress_code.longitude)


if __name__ == "__main__":
    run_example()