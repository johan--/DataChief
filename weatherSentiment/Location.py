import urllib2
import json
import time
import pandas as pd

class Location:
    twitterLocationData = {}
    weatherLocationData = {}

    def get_corodinates_for_geo_box(latitide, longitude):
        geo_box_coordinates = []
        geo_box_coordinates.append(longitude - .5)
        geo_box_coordinates.append(latitide - .5)
        geo_box_coordinates.append(longitude + .5)
        geo_box_coordinates.append(latitide + .5)
        return geo_box_coordinates

    def get_location_data_with_city_state(city, state):
        location_data = []
        location_data.append(city)
        location_data.append(state)
        return location_data

    def import_cities_data_from_file(file_name):
        file = open(file_name, 'r')
        data_frame = pd.read_csv(file)
        return data_frame

    def set_coordinates_for_data_frame(data_frame):
        for x in range(0, int(data_frame['city'].count())):
            latitude = data_frame['lat'][x]
            longitude = data_frame['lng'][x]
            state_name = data_frame['state'][x]
            city_name = data_frame['city'][x]
            geo_box = Location.get_corodinates_for_geo_box(latitude, longitude)
            Location.twitterLocationData[city_name] = geo_box
            Location.weatherLocationData[city_name] = state_name