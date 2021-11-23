from random import randint, choice
from names import get_first_name, get_last_name
from constants.areas_and_cities.general_areas_and_cities import GENERAL_AREAS_AND_CITIES
from functions import (
    generate_geographic_area,
    generate_city_and_state,
    get_city_from_city_and_state,
    get_state_from_city_and_state,
    generate_last_seven_digits_of_phone_number,
    get_closest_area_code,
)


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

    # need to work on this ... Person is different from Person()
    # if not inspect.isclass(type_person):
    #     raise TypeError(
    #         f"{type_person} is neither a class nor subclass of type Person().")

    while num < num_people:
        person = Person()
        people.append(person)
        num += 1
    return people
