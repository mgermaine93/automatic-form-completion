from random import randint, choice
from names import get_first_name, get_last_name
from constants.areas_and_cities import AREAS_AND_CITIES
from constants.us_state_abbreviations import US_STATE_TO_ABBREVIATIONS
import csv
from collections import defaultdict


def generate_geographic_area():
    """
    Needs docstring
    """
    return choice(list(AREAS_AND_CITIES))


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


class Person(object):
    def __init__(self, first_name=get_first_name(), last_name=get_last_name(), city_and_state=generate_city_and_state(generate_geographic_area())):
        """
        Needs docstring
        """
        self.first_name = first_name
        self.last_name = last_name
        self.city_and_state = city_and_state
        self.city = list(city_and_state.keys())[0]
        self.state = list(city_and_state.values())[0]

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

    def generate_phone_number(self):
        first_three = get_closest_area_code(self.state, self.city)
        last_seven = generate_last_seven_digits_of_phone_number()
        return f"{first_three}{last_seven}"

    def get_geographic_area(self):
        """
        Needs docstring
        """
        for area, cities in AREAS_AND_CITIES.items():
            if self.city in cities:
                # in case there are cities of the same name in different states
                if self.state in area:
                    return area
        else:
            return f"City {self.city} not found in the dictionary of available cities."


def generate_random_area_code():
    """
    Needs docstring
    """
    area_code = ""
    for i in range(3):
        area_code += str(choice(range(2, 9)))
    return area_code


def generate_last_seven_digits_of_phone_number():
    """
    Needs docstring
    """
    number = ""
    for i in range(9):
        if i == 0 or i == 4:
            number += "-"
        else:
            number += str(randint(0, 9))
    return number


def get_full_state_name(state_abbreviation):
    """
    Needs docstring
    """
    for full_name, abbreviation in US_STATE_TO_ABBREVIATIONS.items():
        if state_abbreviation.lower() == abbreviation.lower():
            return full_name
        elif state_abbreviation.lower() == full_name.lower():
            return state_abbreviation
    else:
        return f"{state_abbreviation} is not a valid two-character US state abbreviation, nor the name of a US state."


def get_cities_and_area_codes_in_state(state):
    # https://www.kite.com/python/answers/how-to-append-an-element-to-a-key-in-a-dictionary-with-python
    """
    Needs docstring
    """
    state_name = get_full_state_name(state)
    with open('us-area-code-cities.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        # if the city is already in the dict, add another area code as a
        # value to the city key (defaultdict takes care of this automatically)
        cities_and_area_codes = defaultdict(list)
        for row in csv_reader:
            csv_area_code = row[0]
            csv_city = row[1]
            csv_state = row[2]
            if csv_state == state_name:
                cities_and_area_codes[csv_city].append(csv_area_code)
    return cities_and_area_codes


def get_closest_area_code(state, city):
    """
    Needs docstring
    """
    available_cities_and_area_codes = get_cities_and_area_codes_in_state(state)

    for area_city, area_codes in available_cities_and_area_codes.items():
        if area_city.lower() == city.lower():
            return choice(area_codes)
    # for if no area code was found for a given city, but there are area codes for the city's state
    if available_cities_and_area_codes:
        return choice(choice(list(available_cities_and_area_codes.values())))
    # for all other cases
    else:
        return generate_random_area_code()


person = Person()
print(person.city_and_state)
print(person.city)
print(person.state)
print(person.generate_phone_number())
print(person.get_geographic_area())


### SCRAP STUFF THAT MIGHT BE NEEDED LATER ###


# def generate_city():
#     """
#     Needs docstring
#     """
#     geographic_areas = list(AREAS_AND_CITIES.keys())
#     geographic_area = choice(geographic_areas)
#     return choice(AREAS_AND_CITIES[geographic_area])


# def generate_random_geographic_area():
#     """
#     Needs docstring
#     """
#     random_geographic_area = choice(list(AREAS_AND_CITIES.keys()))
#     return random_geographic_area

# if geographic_area in AREAS_AND_CITIES.keys():
#     city = ""
#     city = choice(AREAS_AND_CITIES[geographic_area])
#     # state = geographic_area[-2:]
#     # city_and_state[city] = state
#     return city
# else:
#     return f"{geographic_area} wasn't found in the list of available areas and cities."


# def generate_phone_number(state, city):
#     first_three = get_closest_area_code(state, city)
#     last_seven = generate_last_seven_digits_of_phone_number()
#     return f"{first_three}{last_seven}"
# print(generate_city())
# print(get_closest_area_code("bloomenthal", "mackinac city"))


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

# def generate_random_location():
#     # This function will likely be very helpful!
#     """
#     Needs docstring
#     """
#     random_geographic_area = choice(list(AREAS_AND_CITIES.keys()))
#     random_city_within_geographic_area = choice(
#         AREAS_AND_CITIES[random_geographic_area])
#     return {random_city_within_geographic_area, random_geographic_area}
# print(get_closest_area_code("mi", "rOyAl oak"))
# print(get_geographic_area("Detroit"))
# print(generate_random_location())

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
