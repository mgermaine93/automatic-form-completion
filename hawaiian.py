# this can be made more object-oriented, particularly with the methods of the Floridian() class.

from random import choice
from constants.areas_and_cities.hawaii_islands_and_cities import HAWAII_ISLANDS_AND_CITIES
from person import Person


def generate_hawaii_island():
    """
    Needs docstring
    """
    island_and_state = choice(list(HAWAII_ISLANDS_AND_CITIES))
    return island_and_state


def generate_hawaii_city_and_state(geographic_area):
    """
    Needs docstring
    """
    if geographic_area in HAWAII_ISLANDS_AND_CITIES.keys():
        city_and_state = {}
        city = choice(HAWAII_ISLANDS_AND_CITIES[geographic_area])
        state = geographic_area[-2:]
        city_and_state[city] = state
        return city_and_state
    else:
        raise KeyError(
            f"{geographic_area} wasn't found in the list of available geographic areas.")


class Hawaiian(Person):

    def __init__(self, first_name=None, last_name=None, city_and_state=None):
        """
        Needs docstring
        """
        super().__init__(first_name=first_name, last_name=last_name)
        self.city_and_state = city_and_state or generate_hawaii_city_and_state(
            generate_hawaii_island())

    def get_geographic_area(self):
        """
        Needs docstring?
        """
        # https://stackoverflow.com/questions/231839/python-inheritance-how-to-disable-a-function
        raise AttributeError(
            "'Hawaiian' object has no attribute 'get_geographic_area().'")

    def get_city(self):
        """
        Needs docstring
        """
        return list(self.city_and_state.keys())[0]

    def get_island(self):
        """
        Needs docstring
        """
        # https://realpython.com/iterate-through-dictionary-python/
        city = list(self.city_and_state.keys())[0]
        for island, cities in HAWAII_ISLANDS_AND_CITIES.items():
            if city in cities:
                return island[:-4]
        raise KeyError(
            f"{city} wasn't found in the list of available geographic areas.")


def make_group_of_hawaiians(num_people):
    # this is likely not necessary in the long run, because make_group_of_people() is so similar.
    """
    Returns a list of Hawaiian objects.

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
        person = Hawaiian()
        people.append(person)
        num += 1
    return people


# Testing
# hawaiian = Hawaiian()
# print(hawaiian.first_name)
# print(hawaiian.last_name)
# print(hawaiian.city_and_state)
# print(hawaiian.get_city())
# print(hawaiian.get_island())
# print(hawaiian.generate_email_address())
# print(hawaiian.generate_phone_number())
