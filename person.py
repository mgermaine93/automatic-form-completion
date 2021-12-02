from collections.abc import Mapping
from collections import defaultdict
from csv import reader
from constants.us_state_abbreviations import US_STATE_TO_ABBREVIATIONS
from random import randint, choice
from names import get_first_name, get_last_name
from constants.areas_and_cities.general_areas_and_cities import GENERAL_AREAS_AND_CITIES


def generate_geographic_area(state_area=None):
    """
    Returns a random US-based geographic area based on a state/region entered by the user.
    If no state/region is entered, the geographic area will be selected at random from a large dictionary of states/regions across the US.

    Parameters
    ----------
        state_area : dict
            a US-based state/region

    Returns
    -------
        geographic_area : str
            a US-based geographic area, e.g. 'Wake County, NC'
    """
    if state_area:
        geographic_area = choice(list(state_area))
    else:
        geographic_area = choice(list(GENERAL_AREAS_AND_CITIES))
    return geographic_area


def generate_city_and_state(geographic_area):
    """
    Returns a random city and state from within a given US-based geographic area, if one is found.

    Parameters
    ----------
        geographic_area : str
            a US-based geographic area, e.g. 'Delaware County, PA'

    Returns
    -------
        city_and_state : dict
            a US-based city and state, e.g., {"Darby": "PA"}
    """
    if geographic_area in GENERAL_AREAS_AND_CITIES.keys():
        city_and_state = {}
        city = choice(GENERAL_AREAS_AND_CITIES[geographic_area])
        state = geographic_area[-2:]
        city_and_state[city] = state
        return city_and_state
    else:
        raise KeyError(
            f"{geographic_area} wasn't found in the list of available geographic areas.")


class Person(object):
    """
    A class to represent a person.
    ...

    Attributes
    ----------
        first_name : str
            first name of the person, e.g. 'Mario'
        last_name : str
            last name of the person, e.g. 'Lemieux'
        city_and_state : dict
            the city and state in which the person resides, e.g. {'Pittsburgh': 'PA}

    Methods
    -------
        generate_email_address():
            Returns an email address that was constructed from the person's first name and last name.
        generate_phone_number():
            Returns a phone number that was constructed using the closest area code to the person's geographic area and/or city and state
        get_geographic_area():
            Returns the geographic area in which the person resides, based on their city and state.
    """

    def __init__(self, first_name=None, last_name=None, city_and_state=None):
        """
        Constructs all the necessary attributes for the person object.

        If no attributes are supplied to the person object, random values for the first_name, last_name, and city_and_state attributes will be generated automatically.

        Parameters
        ----------
            first_name : str
                first name of the person
            last_name : str
                last name of the person
            city_and_state : dict
                the city and state in which the person resides, e.g., {'Fort Smith':'AR'}
        """
        self.first_name = first_name or get_first_name()
        self.last_name = last_name or get_last_name()
        self.city_and_state = city_and_state or generate_city_and_state(
            generate_geographic_area())

    def generate_email_address(self):
        """
        Returns an email address that was generated using the person's first name and last name.

        Parameters
        ----------
            None needed

        Returns
        -------
            email_address : str 
                a string representing the person's email address, e.g., 'tony.delvecchio2006@outlook.com'
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
        email_address = f"{first_name_segment}{last_name_segment}{random_number}@{choice(providers)}"
        return email_address

    def generate_phone_number(self):
        """
        Returns a phone number that was generated using the person's city and state.

        Parameters
        ----------
            None needed

        Returns
        -------
            phone_number : (str) 
                a string representing the person's phone number, e.g., '800-588-2300'
        """
        first_three = get_closest_area_code(get_state_from_city_and_state(
            self.city_and_state), get_city_from_city_and_state(self.city_and_state))
        last_seven = generate_last_seven_digits_of_phone_number()
        phone_number = f"{first_three}-{last_seven}"
        return phone_number

    def get_geographic_area(self):
        """
        Returns a geographic area that was generated using the person's city and state.

        Parameters
        ----------
            None needed

        Returns
        -------
            area : str
                a string representing the person's geographic area of residence, e.g., 'McAllen, TX'
        """
        for area, cities in GENERAL_AREAS_AND_CITIES.items():
            if get_city_from_city_and_state(self.city_and_state) in cities:
                # in case there are cities of the same name in different states
                if get_state_from_city_and_state(self.city_and_state) in area:
                    return area
        else:
            raise KeyError(
                f"City {get_city_from_city_and_state(self.city_and_state)} not found in the dictionary of available cities.")


# from constants.florida_areas_and_cities import FLORIDA_AREAS_AND_CITIES
# https://stackoverflow.com/questions/395735/how-to-check-whether-a-variable-is-a-class-or-not


def get_city_from_city_and_state(city_and_state):
    """
    Returns the city of a provided US-based location.

    Parameters
    ----------
        city_and_state : dict
            a US city- and state-based location, e.g., {'Taos': 'NM'}

    Returns
    -------
        city : str
            a US-based city, e.g., 'Taos'
    """
    # https://stackoverflow.com/questions/25231989/how-to-check-if-a-variable-is-a-dictionary-in-python

    if isinstance(city_and_state, Mapping):
        # city will always be the key
        city = list(city_and_state.keys())[0]
        return city
    else:
        raise TypeError(f"{city_and_state} is not of type dict.")


def get_state_from_city_and_state(city_and_state):
    """
    Returns the ISO-3166 two-character state abbreviation from a provided US-based location.

    Parameters
    ----------
        city_and_state : dict
            a US city- and state-based location, e.g. {'Mackinac City': 'MI'}

    Returns
    -------
        state : str
            the ISO-3166 two-character abbreviation of a US-based state, e.g., 'MI'
    """
    if isinstance(city_and_state, Mapping):
        # state will always be the value
        state = list(city_and_state.values())[0]
        return state
    else:
        raise TypeError(f"{city_and_state} is not of type dict.")


def generate_random_area_code():
    """
    Returns a random three-digit phone number area code, e.g. "313".

    Parameters
    ----------
        None needed

    Returns
    -------
        area_code : str
            a random three-digit phone number area code, e.g. "313"
    """
    area_code = ""
    i = 0
    while i < 3:
        area_code += str(choice(range(2, 9)))
        i += 1
    return area_code


def generate_last_seven_digits_of_phone_number():
    """
    Returns a random string of eight characters representing the hyphenated last seven digits of a US-based phone number.

    Parameters
    ----------
        None needed

    Returns
    -------
        digits : str
            a random string of eight characters and a hyphen, e.g. "888-8888"
    """
    digits = ""
    for i in range(8):
        if i == 3:
            digits += "-"
        else:
            digits += str(randint(0, 9))
    return digits


def get_full_state_name(state_abbreviation):
    """
    Returns the full name of a US-based state.

    Parameters
    ----------
        state_abbreviation : str
            the ISO-3166 two-character abbreviation of a US-based state, e.g. 'VT'

    Returns
    -------
        full_name : str
            the full name of a US-based state, e.g. 'Vermont'
    """
    for full_name, abbreviation in US_STATE_TO_ABBREVIATIONS.items():
        if state_abbreviation.lower() == abbreviation.lower():
            return full_name
        elif state_abbreviation.lower() == full_name.lower():
            return state_abbreviation
    else:
        raise KeyError(
            f"{state_abbreviation} is not a valid ISO-3166 two-character US state abbreviation, nor the full name of a US state.")


def get_cities_and_area_codes_in_state(state):
    """
    Returns a dictionary of US-based cities (keys) and their associated three-digits area codes (values) within a provided US state.

    Parameters
    ----------
        state : str
            a US-based state, represented by either its full name or its the ISO-3166 two-character abbreviation, e.g., 'New Hampshire' or 'NH'

    Returns
    -------
        cities_and_area_codes : dict
            a dictionary of US-based cities (keys) and their associated three-digits area codes (values) from within a US-based state, e.g.,
                {
                    'East Concord': ['603'], 
                    'Derry': ['603'], 
                    'Dover': ['603'], 
                    'Keene': ['603'], 
                    'Manchester': ['603'], 
                    'Nashua': ['603'], 
                    'Portsmouth': ['603'], 
                    'Rochester': ['603']
                }
    """
    # https://www.kite.com/python/answers/how-to-append-an-element-to-a-key-in-a-dictionary-with-python
    state_name = get_full_state_name(state)
    with open('constants/us-area-code-cities.csv') as csv_file:
        csv_reader = reader(csv_file, delimiter=",")
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
    Returns a three-digit area code that most closely matches up with the user-input state and city, if one is found.  If no matching state and city is found, a random three-digit area code will be returned instead.

    Parameters
    ----------
        state : str
            a US-based state, represented by either its full name or its the ISO-3166 two-character abbreviation, e.g., 'Maine' or 'ME'
        city : str
            a US-based city, e.g., 'Portland'

    Returns
    -------
        area_code : str
            a three-digit phone number area code, e.g., '207'
    """
    available_cities_and_area_codes = get_cities_and_area_codes_in_state(state)
    # the default is a random area code
    area_code = generate_random_area_code()
    for area_city, area_codes in available_cities_and_area_codes.items():
        # for if there's an exact match between the provided state/city and what's in the csv file
        if area_city.lower() == city.lower():
            area_code = choice(area_codes)
            return area_code
    # for if no area code was found for a given city, but there are area codes for the city's state
    if available_cities_and_area_codes:
        area_code = choice(
            choice(list(available_cities_and_area_codes.values())))
        return area_code
    # for all other cases
    else:
        return area_code


def make_group_of_people(num_people):
    # this might need to be refactored to take in a certain type of person (Floridian, etc.) rather than a Person() object be default.
    """
    Returns a list of Person objects.

    Parameters
    ----------
        num_people : int
            an integer representing how many Person objects will be created, e.g., '8'
        type_person : Person() / class
            a class or subclass of type Person()

    Returns
    -------
        people : list
            a list of Person objects (see 'Person' object docstring above).
    """
    # https://stackoverflow.com/questions/30420621/python-creating-object-instances-in-a-loop-with-independent-handling
    people = []
    num = 0

    while num < num_people:
        person = Person()
        people.append(person)
        num += 1
    return people


# person = Person()
# print(person.first_name)
# print(person.last_name)
# print(person.city_and_state)
# print(person.generate_email_address())
# print(person.generate_phone_number())
