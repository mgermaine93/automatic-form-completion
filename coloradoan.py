import csv

from random import choice
from constants.states.colorado import COLORADO_COUNTIES
from functions import generate_last_seven_digits_of_phone_number
from person import Person


def generate_colorado_county():
    """
    Needs docstring
    """
    county = choice(list(COLORADO_COUNTIES))
    return county


def get_colorado_cities_and_states():
    """
    Need docstring
    """
    with open('constants/colorado-cities-and-states.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        colorado_cities_and_states = []
        for row in csv_reader:
            if row[1] == "CO":
                new_dict = {row[4]: row[1]}
                colorado_cities_and_states.append(new_dict)
        return colorado_cities_and_states


def generate_colorado_city_and_state():
    """
    Need docstring
    """
    city_and_state = choice(get_colorado_cities_and_states())
    return city_and_state


class Coloradoan(Person):

    def __init__(self, first_name=None, last_name=None, city_and_state=None):
        """
        Needs docstring
        """
        super().__init__(first_name=first_name, last_name=last_name)
        self.city_and_state = city_and_state or generate_colorado_city_and_state()
        self.county = generate_colorado_county()

    def generate_colorado_phone_number(self):
        """
        Needs docstring
        """
        first_three = choice(["303", "719", "720", "970", "983"])
        last_seven = generate_last_seven_digits_of_phone_number()
        phone_number = f"{first_three}-{last_seven}"
        return phone_number


def make_group_of_coloradoans(num_people):
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
        person = Coloradoan()
        people.append(person)
        num += 1
    return people


# # Testing
# coloradoan = Coloradoan()
# print(coloradoan.first_name)
# print(coloradoan.last_name)
# print(coloradoan.generate_email_address())
# print(coloradoan.generate_phone_number())
# print(coloradoan.county)

# # generate_colorado_county()
# # generate_colorado_city_and_state()
# # get_colorado_cities_and_states()
