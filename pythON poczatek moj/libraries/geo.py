import geopy
import requests
import black
from dataclasses import dataclass

from geopy import Nominatim
from geopy import distance as geopy_distance

@dataclass(frozen=True)
class StreetLocation:
    latitude: float
    longitude: float

    @property
    def location(self):
        return  self.latitude, self.latitude

class GeoLocator:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="geo=leo-test")

    def street_location_from_address(self,address):
        geocode_location = self.geolocator.geocode(address)
        return StreetLocation(geocode_location.latitude, geocode_location.longitude)

def meter_distance(src,dst):
    return int(geopy_distance.distance(src.location,dst.location).meters)

def walk_time (src,dst):
    meters_per_minute= 80
    distance = meter_distance(src,dst)
    return int(distance/meters_per_minute)



def run_example():

    # src_address = "ul. Milberta 6, 27-600 Sandomierz"
    # dst_address = "ul. Mickiewicza 4, 27-600 Sandomierz "
    # geo_locator = GeoLocator()
    # src_location = geo_locator.street_location_from_address(src_address)
    # dst_location = geo_locator.street_location_from_address(dst_address)
    # src_dst_distance = meter_distance(src_location,dst_location)
    # src_dst_walk_time = walk_time(src_location,dst_location)
    #
    # print(f"Dystans z {src_address} do {dst_address}to {src_dst_distance} metrów")
    # print(f" Czas potrzebny do przebycia pieszo to ok {src_dst_walk_time} minut")
    address = "ul. Mickiewicza 4, 27-600 Sandomierz"
    geolocator = geopy.Nominatim(user_agent="webinar=agent")
    adress_code= geolocator.geocode(address)
#
    print(adress_code.latitude)
    print(adress_code.longitude)
#
#
if __name__ == "__main__":
    run_example()