from random import randint, choice
from names import get_first_name, get_last_name
from constants.areas_and_cities import AREAS_AND_CITIES
from constants.us_state_abbreviations import US_STATE_TO_ABBREVIATIONS
import csv


def generate_geographic_area():
    """
    Needs docstring
    """
    return choice(list(AREAS_AND_CITIES))


def generate_random_geographic_area():
    """
    Needs docstring
    """
    random_geographic_area = choice(list(AREAS_AND_CITIES.keys()))
    return random_geographic_area


class Person(object):
    def __init__(self, first_name=get_first_name(), last_name=get_last_name(), geographic_area=generate_random_geographic_area()):
        """
        Needs docstring
        """
        self.first_name = first_name
        self.last_name = last_name
        # self.geographic_area = geographic_area

    # def generate_phone_number(self):
    #     """
    #     Needs docstring
    #     """
    #     pass

    def generate_email_address(self):
        """
        Needs docstring
        """
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
            "comcast.net",
            "verizon.net",
            "comcast.net"
        ]
        return f"{first_name_segment}{last_name_segment}{random_number}@{choice(providers)}"


def get_geographic_area(city):
    for area, cities in AREAS_AND_CITIES.items():
        if city in cities:
            return area
    else:
        return f"City {city} not found."


# def generate_random_location():
#     # This function will likely be very helpful!
#     """
#     Needs docstring
#     """
#     random_geographic_area = choice(list(AREAS_AND_CITIES.keys()))
#     random_city_within_geographic_area = choice(
#         AREAS_AND_CITIES[random_geographic_area])
#     return {random_city_within_geographic_area, random_geographic_area}


def generate_city_and_state(geographic_area):
    """
    Needs docstring
    """
    if geographic_area in AREAS_AND_CITIES.keys():
        city_and_state = {}
        city = choice(AREAS_AND_CITIES[geographic_area])
        state = geographic_area[-2:]
        city_and_state[city] = state
        return city_and_state
    else:
        return f"{geographic_area} wasn't found in the list of available areas and cities."

# def generate_city_and_state(geographic_area):
#     """
#     Needs docstring
#     """
#     if geographic_area in AREAS_AND_CITIES.keys():
#         city_and_state = {}
#         city = choice(AREAS_AND_CITIES[geographic_area])
#         state = geographic_area[-2:]
#         city_and_state[city] = state
#         return city_and_state
#     else:
#         return f"{geographic_area} wasn't found in the list of available areas and cities."


def generate_random_phone_number():
    """
    Needs docstring
    """
    number = ""
    for i in range(12):
        if i == 3 or i == 7:
            number += "-"
        else:
            number += str(randint(0, 9))
    return number


def generate_last_seven_digits_of_phone_number(area_code):
    """
    Needs docstring
    """
    number = f"{area_code}"
    for i in range(9):
        if i == 0 or i == 4:
            number += "-"
        else:
            number += str(randint(0, 9))
    return number


def get_cities_and_area_codes_in_state(state):
    """
    Needs docstring
    """
    with open('us-area-code-cities.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        cities_and_area_codes = {}
        for row in csv_reader:
            if row[2] == state:
                cities_and_area_codes[row[1]] = row[0]
    return cities_and_area_codes


def get_closest_area_code(state, city):
    """
    Needs docstring
    """
    available_cities_and_area_codes = get_cities_and_area_codes_in_state(state)
    options = []
    for area_city, area_code in available_cities_and_area_codes.items():
        if area_city == city:
            options.append(area_code)
    if options:
        return choice(options)
    elif available_cities_and_area_codes:
        return choice(list(available_cities_and_area_codes.values()))
    else:
        return generate_random_phone_number()


def get_full_state_name(state_abbreviation):
    """
    Needs docstring
    """
    if len(state_abbreviation) == 2:
        for full_name, abbreviation in US_STATE_TO_ABBREVIATIONS.items():
            if state_abbreviation.upper() == abbreviation:
                return full_name
        else:
            return f"{state_abbreviation} was not found in the list of valid states and abbreviations."
    return f"{state_abbreviation} is not a valid two-character US state abbreviation."


# print(get_geographic_area("Detroit"))
print(generate_random_location())

# def generate_phone_number(area_code):
#     city_and_state =
#     print(city_and_state)
#     # full_state_name = get_full_state_name()
#     # print(full_state_name)


# print(get_cities_and_area_codes_in_state("Michigan"))

# person = Person()
# print(person.first_name)
# print(person.last_name)
# print(person.geographic_area)
# print(person.generate_email_address())
# print(person.generate_city())
# print(person.generate_state())


# get_cities_and_area_codes_in_state("Michigan")
# get_closest_area_code("Michigan", "Detroit")
# get_closest_area_code("Michigan", "Royal Oak")
# person = Person(get_first_name(), get_last_name())

# first_name = person.first_name
# last_name = person.last_name
# email_address = person.generate_email_address()
# geographic_area = person.generate_geographic_area()
# print(geographic_area)

# generate_city_from_geographic_area(geographic_area)
