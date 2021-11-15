from random import randint, choice
from names import get_first_name, get_last_name
from constants.areas_and_cities import AREAS_AND_CITIES
from constants.us_state_abbreviations import US_STATE_TO_ABBREVIATIONS
import csv

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def generate_phone_number(self):
        number = ""
        for i in range(12):
            if i == 3 or i == 7:
                number += "-"
            else:
                number += str(randint(0, 9))
        # print(number)
        return number

    def generate_email_address(self):
        first_name_index = randint(1, len(self.first_name))
        last_name_index = randint(1, len(self.last_name))
        first_name_segment = self.first_name.lower()[0:first_name_index]
        last_name_segment = self.last_name.lower()[0:last_name_index]
        random_number = randint(0, 100)
        providers = [
            "gmail.com",
            "outlook.com",
            "yahoo.com",
            "hotmail.com",
            "aol.com",
            "comcast.net"
        ]
        return f"{first_name_segment}{last_name_segment}{random_number}@{choice(providers)}"
    
    def generate_geographic_area(self):
        return choice(list(AREAS_AND_CITIES))

def generate_city_from_geographic_area(geographic_area):
    print(choice(AREAS_AND_CITIES[geographic_area]))
    return choice(AREAS_AND_CITIES[geographic_area])

def get_cities_and_area_codes_in_state(state):
    with open('us-area-code-cities.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        cities = {}
        for row in csv_reader:
            if row[2] == state:
                cities[row[1]] = row[0]
    # print(cities)
    return cities

def get_closest_area_code(state, city):
    available_cities_and_area_codes = get_cities_and_area_codes_in_state(state)
    options = []
    for area_city, area_code in available_cities_and_area_codes.items():
        if area_city == city:
            options.append(area_code)
    if options:
        print(choice(options))
        return choice(options)
    else:
        print(choice(list(available_cities_and_area_codes.values())))
        return choice(list(available_cities_and_area_codes.values()))
    
    # Not sure if this is needed any more?
    #
    # for key, value in available_cities_and_area_codes.items():
    #     options = []
    #     # print(key)
    #     # print(city)
    #     if key == city:
    #         options.append(key[value])
    #         print("Yes")
    #         # print(value)
    #     # else:
    #     #     print("No area codes found.")
    # print(options)


get_cities_and_area_codes_in_state("Michigan")
get_closest_area_code("Michigan", "Detroit")
# get_closest_area_code("Michigan", "Royal Oak")
# person = Person(get_first_name(), get_last_name())

# first_name = person.first_name
# last_name = person.last_name
# email_address = person.generate_email_address()
# geographic_area = person.generate_geographic_area()
# print(geographic_area)

# generate_city_from_geographic_area(geographic_area)