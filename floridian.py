# this can be made more object-oriented, particularly with the methods of the Floridian() class.

from random import choice
from constants.areas_and_cities.florida_areas_and_cities import FLORIDA_AREAS_AND_CITIES
from constants.party import make_group_name
from person import Person


def generate_florida_county():
    """
    Needs docstring
    """
    county_and_state = choice(list(FLORIDA_AREAS_AND_CITIES))
    return county_and_state


def generate_florida_city_and_state(geographic_area):
    """
    Needs docstring
    """
    if geographic_area in FLORIDA_AREAS_AND_CITIES.keys():
        city_and_state = {}
        city = choice(FLORIDA_AREAS_AND_CITIES[geographic_area])
        state = geographic_area[-2:]
        city_and_state[city] = state
        return city_and_state
    else:
        raise KeyError(
            f"{geographic_area} wasn't found in the list of available geographic areas.")


class Floridian(Person):

    def __init__(self, first_name=None, last_name=None, city_and_state=None):
        """
        Needs docstring
        """
        super().__init__(first_name=first_name, last_name=last_name)
        self.city_and_state = city_and_state or generate_florida_city_and_state(
            generate_florida_county())

    def get_geographic_area(self):
        """
        Needs docstring?
        """
        # https://stackoverflow.com/questions/231839/python-inheritance-how-to-disable-a-function
        raise AttributeError(
            "'Floridian' object has no attribute 'get_geographic_area().'")

    def get_city(self):
        """
        Needs docstring
        """
        return list(self.city_and_state.keys())[0]

    def get_county(self):
        """
        Needs docstring
        """
        counties = FLORIDA_AREAS_AND_CITIES
        city = list(self.city_and_state.keys())[0]
        for county in counties:
            if city in FLORIDA_AREAS_AND_CITIES[county]:
                return county
        raise KeyError(
            f"{city} was not found in the available dictionary of Florida cities and counties.")

    def get_group(self):
        """
        Needs docstring
        """
        counties = FLORIDA_AREAS_AND_CITIES
        city = list(self.city_and_state.keys())[0]
        location = ""
        for county in counties:
            if city in FLORIDA_AREAS_AND_CITIES[county]:
                location = county
                return f'{make_group_name()} of {location[:-4]}'
        raise KeyError(
            f"{city} was not found in the available dictionary of Florida cities and counties.")


def make_group_of_floridians(num_people):
    # this is likely not necessary in the long run, because make_group_of_people() is so similar.
    """
    Returns a list of Floridian objects.

    Parameters
    ----------
        num_people : int
            an integer representing how many Person objects will be created, e.g., '8'

    Returns
    -------
        people : list
            a list of Person objects (see 'Person' object docstring above).
    """
    # https://stackoverflow.com/questions/30420621/python-creating-object-instances-in-a-loop-with-independent-handling
    people = []
    num = 0

    while num < num_people:
        person = Floridian()
        people.append(person)
        num += 1
    return people


# results = make_group_of_floridians(3)

# for floridian in results:
#     print(floridian.first_name)
#     print(floridian.last_name)
#     print(floridian.city_and_state)
#     print(floridian.get_county())
#     print(floridian.generate_phone_number())
#     print(floridian.get_group())
