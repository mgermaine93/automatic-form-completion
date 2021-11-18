from random import randint, choice
from collections.abc import Mapping
from collections import defaultdict
from csv import reader
from constants.us_state_abbreviations import US_STATE_TO_ABBREVIATIONS
from constants.areas_and_cities import AREAS_AND_CITIES
import unittest
import re

from person import (
    Person,
    generate_geographic_area,
    generate_city_and_state,
    generate_random_area_code,
    generate_last_seven_digits_of_phone_number,
    get_full_state_name,
    get_cities_and_area_codes_in_state,
    get_closest_area_code
)


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.person1 = Person(first_name="Elizabeth", last_name="Lastra", city_and_state={
                              'Arlington Park': 'TX'})
        self.person2 = Person(
            first_name="David", last_name="Swanson", city_and_state={'Detroit': 'MI'})

    def test_first_name_string(self):
        person1_first_name = self.person1.first_name
        actual = isinstance(person1_first_name, str)
        expected = True
        self.assertEqual(actual, expected,
                         'Expected `first_name` to be a string.')

    def test_last_name_is_string(self):
        person1_last_name = self.person1.last_name
        actual = isinstance(person1_last_name, str)
        expected = True
        self.assertEqual(actual, expected,
                         'Expected `last_name` to be a string.')

    def test_geographic_area_is_dict(self):
        person1_city_and_state = self.person1.city_and_state
        actual = isinstance(person1_city_and_state, Mapping)
        expected = True
        self.assertEqual(actual, expected,
                         'Expected `city_and_state` to be a dict.')

    def test_generate_email_address(self):
        person1_email_address = self.person1.generate_email_address()
        # this needs work
        actual = re.match("\d[@]\D[.com]", person1_email_address)
        expected = True
        self.assertEqual(actual, expected,
                         'Expected `generate_email_address()` to return a string representing an email address.')

    def test_generate_phone_number(self):
        # this needs work, too
        person1_phone_number = self.person1.generate_phone_number()
        actual = re.match("\817-\d{3}-\d{4}", person1_phone_number)
        expected = True
        self.assertEqual(actual, expected,
                         'Expected `generate_phone_number()` to return a string representing an Arlington, TX, phone number starting with "817" or "469".')

    def test_get_geographic_area(self):
        person1_geographic_area = self.person1.get_geographic_area()
        actual = person1_geographic_area
        expected = "Dallas, TX"
        self.assertEqual(actual, expected,
                         'Expected `get_geographic_area()` to return "Dallas, TX".')

    # METHODS

    # test first name is string
    # test last name is string
    # test geographic area is dict
    # test generate_email_address
    # test generate_phone_number
    # test get_geographic_area

    # FUNCTIONS

    # test generate_geographic_area
    # test generate city and state
    # test get city from city and state
    # test get state from city and state
    # generate_random_area_code,
    # generate_last_seven_digits_of_phone_number,
    # get_full_state_name,
    # get_cities_and_area_codes_in_state,
    # get_closest_area_code
    # make_group_people


#     def test_deposit(self):  # good
#         self.food.deposit(900, "deposit")
#         actual = self.food.ledger[0]
#         expected = {"amount": 900, "description": "deposit"}
#         self.assertEqual(
#             actual, expected, 'Expected `deposit` method to create a specific object in the ledger instance variable.')

#     def test_deposit_no_description(self):  # good
#         self.food.deposit(45.56)
#         actual = self.food.ledger[0]
#         expected = {"amount": 45.56, "description": ""}
#         self.assertEqual(
#             actual, expected, 'Expected calling `deposit` method with no description to create a blank description.')

#     def test_withdraw(self):  # good
#         self.food.deposit(900, "deposit")
#         self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
#         actual = self.food.ledger[1]
#         expected = {"amount": -45.67,
#                     "description": "milk, cereal, eggs, bacon, bread"}
#         self.assertEqual(
#             actual, expected, 'Expected `withdraw` method to create a specific object in the ledger instance variable.')

#     def test_withdraw_no_description(self):  # good
#         self.food.deposit(900, "deposit")
#         good_withdraw = self.food.withdraw(45.67)
#         actual = self.food.ledger[1]
#         expected = {"amount": -45.67, "description": ""}
#         self.assertEqual(
#             actual, expected, 'Expected `withdraw` method with no description to create a blank description.')
#         self.assertEqual(good_withdraw, True,
#                          'Expected `transfer` method to return `True`.')

#     def test_get_balance(self):  # good
#         self.food.deposit(900, "deposit")
#         self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
#         actual = self.food.get_balance()
#         expected = 854.33
#         self.assertEqual(actual, expected, 'Expected balance to be 854.33')

#     def test_transfer(self):  # all good
#         self.food.deposit(900, "deposit")
#         self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
#         good_transfer = self.food.transfer(20, self.entertainment)
#         actual = self.food.ledger[2]
#         expected = {"amount": -20, "description": "Transfer to Entertainment"}
#         self.assertEqual(
#             actual, expected, 'Expected `transfer` method to create a specific ledger item in food object.')
#         self.assertEqual(good_transfer, True,
#                          'Expected `transfer` method to return `True`.')
#         actual = self.entertainment.ledger[0]
#         expected = {"amount": 20, "description": "Transfer from Food"}
#         self.assertEqual(
#             actual, expected, 'Expected `transfer` method to create a specific ledger item in entertainment object.')

#     def test_check_funds(self):  # all good
#         self.food.deposit(10, "deposit")
#         actual = self.food.check_funds(20)
#         expected = False
#         self.assertEqual(actual, expected,
#                          'Expected `check_funds` method to be False')
#         actual = self.food.check_funds(10)
#         expected = True
#         self.assertEqual(actual, expected,
#                          'Expected `check_funds` method to be True')

#     def test_withdraw_no_funds(self):  # good
#         self.food.deposit(100, "deposit")
#         good_withdraw = self.food.withdraw(100.10)
#         self.assertEqual(good_withdraw, False,
#                          'Expected `withdraw` method to return `False`.')

#     def test_transfer_no_funds(self):  # good
#         self.food.deposit(100, "deposit")
#         good_transfer = self.food.transfer(200, self.entertainment)
#         self.assertEqual(good_transfer, False,
#                          'Expected `transfer` method to return `False`.')

#     def test_to_string(self):  # not good
#         self.food.deposit(900, "deposit")
#         self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
#         self.food.transfer(20, self.entertainment)
#         actual = str(self.food)
#         expected = f"*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"
#         self.assertEqual(actual, expected,
#                          'Expected different string representation of object.')

#     def test_create_spend_chart(self):  # definitely not good
#         self.food.deposit(900, "deposit")
#         self.entertainment.deposit(900, "deposit")
#         self.business.deposit(900, "deposit")
#         self.food.withdraw(105.55)
#         self.entertainment.withdraw(33.40)
#         self.business.withdraw(10.99)
#         actual = create_spend_chart(
#             [self.business, self.food, self.entertainment])
#         expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
#         self.assertEqual(
#             actual, expected, 'Expected different chart representation. Check that all spacing is exact.')


# if __name__ == "__main__":
#     unittest.main()
