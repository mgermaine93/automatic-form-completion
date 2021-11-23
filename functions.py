from random import randint, choice
from constants.areas_and_cities.general_areas_and_cities import GENERAL_AREAS_AND_CITIES
# from constants.florida_areas_and_cities import FLORIDA_AREAS_AND_CITIES
from constants.us_state_abbreviations import US_STATE_TO_ABBREVIATIONS
from csv import reader
from collections import defaultdict
from collections.abc import Mapping
import inspect
# https://stackoverflow.com/questions/395735/how-to-check-whether-a-variable-is-a-class-or-not


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
            a US-based city and state, e.g., 'PA'
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


def get_county(city_and_state):
    # still need to figure this out for the Floridian() class.
    pass
