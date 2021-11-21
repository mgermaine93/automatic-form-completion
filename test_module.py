from random import randint, choice
from collections.abc import Mapping
from collections import defaultdict
from csv import reader
from constants.us_state_abbreviations import US_STATE_TO_ABBREVIATIONS
from constants.areas_and_cities import AREAS_AND_CITIES
import unittest
import re
from email_validator import validate_email

from person import (
    Person,
    generate_geographic_area,
    generate_city_and_state,
    generate_random_area_code,
    generate_last_seven_digits_of_phone_number,
    get_city_from_city_and_state,
    get_state_from_city_and_state,
    get_full_state_name,
    get_cities_and_area_codes_in_state,
    get_closest_area_code,
    make_group_of_people
)


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.person1 = Person(first_name="Elizabeth", last_name="Lastra", city_and_state={
                              'Pittsburgh': 'PA'})
        self.person2 = Person(
            first_name="David", last_name="Swanson", city_and_state={'Detroit': 'MI'})

    def test_first_name_string(self):
        person1_first_name = self.person1.first_name
        actual = isinstance(person1_first_name, str)
        expected = True
        self.assertEqual(actual, expected,
                         'Expected first_name to be a string.')

    def test_last_name_is_string(self):
        person1_last_name = self.person1.last_name
        actual = isinstance(person1_last_name, str)
        expected = True
        self.assertEqual(actual, expected,
                         'Expected last_name to be a string.')

    def test_geographic_area_is_dict(self):
        person1_city_and_state = self.person1.city_and_state
        actual = isinstance(person1_city_and_state, Mapping)
        expected = True
        self.assertEqual(actual, expected,
                         'Expected city_and_state to be a dict.')

    def test_generate_email_address(self):
        person1_email_address = self.person1.generate_email_address()
        actual = bool(validate_email(person1_email_address))
        expected = True
        self.assertEqual(actual, expected,
                         'Expected generate_email_address() to return a string representing an email address.')

    def test_generate_phone_number(self):
        person1_phone_number = self.person1.generate_phone_number()
        actual = bool(
            re.match("(?:724|412|878)-\d{3}-\d{4}", person1_phone_number))
        expected = True
        self.assertEqual(actual, expected,
                         'Expected generate_phone_number() to return a string representing a Pittsburgh, PA, phone number starting with "724" or "412" or "878".')

    def test_get_geographic_area(self):
        person1_geographic_area = self.person1.get_geographic_area()
        actual = person1_geographic_area
        expected = "Pittsburgh, PA"
        self.assertEqual(actual, expected,
                         'Expected get_geographic_area() to return "Dallas, TX".')

    def test_get_geographic_area_with_unlisted_city(self):
        # https://stackoverflow.com/questions/6103825/how-to-properly-use-unit-testings-assertraises-with-nonetype-objects
        self.assertRaises(KeyError, lambda: self.person2.get_geographic_area())

    def test_generate_geographic_area(self):
        random_geographic_area = generate_geographic_area()
        self.assertIn(random_geographic_area, AREAS_AND_CITIES,
                      'Expected generate_geographic_area() to return an item from the AREAS_AND_CITIES dict.')
        self.assertIn(random_geographic_area, AREAS_AND_CITIES.keys(
        ), 'Expected generate_geographic_area() to return a key from the AREAS_AND_CITIES dict.')

    def test_generate_city_and_state(self):
        # this needs work
        random_geographic_area = generate_geographic_area()
        expected_geographic_area_type = isinstance(random_geographic_area, str)
        expected_geographic_area_names = AREAS_AND_CITIES.keys()
        random_city_and_state = generate_city_and_state(random_geographic_area)
        expected_city_and_state_type = isinstance(
            random_city_and_state, Mapping)
        expected_geographic_area_city_names = AREAS_AND_CITIES[random_geographic_area]
        self.assertEqual(True, expected_geographic_area_type,
                         f'Expected {random_geographic_area} to be a string.')
        self.assertEqual(True, expected_city_and_state_type,
                         f'Expected {random_city_and_state} to be a dict.')
        self.assertIn(random_geographic_area, expected_geographic_area_names,
                      f'Expected {random_geographic_area} to be a key in the AREAS_AND_CITIES dict.')
        self.assertIn(
            list(random_city_and_state.keys())[0], expected_geographic_area_city_names, f'Expected {list(random_city_and_state.keys())[0]} to be drawn from the AREAS_AND_KEYS dict at the {random_geographic_area} key.')
        self.assertEqual(list(random_city_and_state.values())[0], random_geographic_area[-2:],
                         f'Expected {list(random_city_and_state.values())[0]} to be equal to {random_geographic_area[-2:]}, i.e., the state should be the same as the state in which the geographic area is found.')

    def test_get_city_from_city_and_state(self):
        city_and_state_dict = {"McAllen": "TX"}
        city_and_state_string = "McAllen, TX"
        actual = "McAllen"
        expected = get_city_from_city_and_state(city_and_state_dict)
        self.assertEqual(
            actual, expected, 'Expected get_city_from_city_and_state() to retrieve the city from a city/string dict.')
        self.assertRaises(
            TypeError, lambda: get_city_from_city_and_state(city_and_state_string))

    def test_get_state_from_city_and_state(self):
        city_and_state_dict = {"Everett": "WA"}
        city_and_state_string = "Everett, WA"
        actual = "WA"
        expected = get_state_from_city_and_state(city_and_state_dict)
        self.assertEqual(
            actual, expected, 'Expected get_state_from_city_and_state() to retrieve the state value from a city/string dict.')
        self.assertRaises(
            TypeError, lambda: get_state_from_city_and_state(city_and_state_string))

    def test_generate_random_area_code(self):
        random_area_code = generate_random_area_code()
        actual = bool(re.match("[2-9]\d{2}", random_area_code))
        expected = True
        self.assertEqual(
            actual, expected, 'Expected generate_random_area_code() to return a string of three digits with the first digit greater than or equal to 2.')

    def test_generate_last_seven_digits_of_phone_number(self):
        random_last_seven_digits = generate_last_seven_digits_of_phone_number()
        actual = bool(re.match("(\d{3})-(\d{4})", random_last_seven_digits))
        expected = True
        self.assertEqual(
            actual, expected, 'Expected generate_random_last_seven_digits() to return a string of eight characters -- a single hyphen, followed by three digits of any value, followed by a hypen, followed by four digits of any value, e.g., "456-7890".')

    def test_get_full_state_name(self):
        full_state_name = get_full_state_name("WV")
        actual = "West Virginia"
        expected = full_state_name
        self.assertEqual(
            actual, expected, 'Expected get_full_state_name("WV") to return "West Virginia", the full state name corresponding to "WV".')
        self.assertRaises(
            KeyError, lambda: get_full_state_name("VV"))
        self.assertIn(full_state_name, list(US_STATE_TO_ABBREVIATIONS.keys(
        )), 'Expected the full state name of "WV" to be in the US_STATE_TO_ABBREVIATIONS dict.')

    def test_get_cities_and_area_codes_in_state(self):
        state = "Vermont"
        actual = isinstance(get_cities_and_area_codes_in_state(state), Mapping)
        expected = True
        self.assertEqual(
            actual, expected, 'Expected get_cities_and_area_codes_in_state("Vermont") to return a dict.')

    def test_get_closest_area_code(self):
        state = "Michigan"
        city = "Detroit"
        actual = get_closest_area_code(state, city)
        expected = "313"
        self.assertEqual(
            actual, expected, 'Expected get_closest_area_code("Michigan", "Detroit") to return "313".')

    def test_make_group_people(self):
        num_people = 7
        actual_length = len(make_group_of_people(num_people))
        expected_length = num_people
        actual_type = isinstance(make_group_of_people(
            num_people), list)
        expected_type = True
        actual_index_type = isinstance(
            make_group_of_people(num_people)[choice(range(0, num_people))], Person)
        expected_index_type = True
        self.assertEqual(actual_length, expected_length,
                         'Expected make_group_people(7) to return a list of length 7.')
        self.assertEqual(actual_type, expected_type,
                         'Expected make_group_people(7) to produce a list.')
        self.assertEqual(actual_index_type, expected_index_type,
                         'Expected make_group_people(7) to return a list of objects of type Person.')


# if __name__ == "__main__":
#     unittest.main()
