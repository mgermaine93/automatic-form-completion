from random import randint, choice
from names import get_first_name, get_last_name
from constants.areas_and_cities import AREAS_AND_CITIES

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def generate_phone_number(self):
        number = ""
        for i in range(12):
            if i == 3 or i == 7:
                number += "-"
            else:
                number += str(randint(0, 9))
        # print(number)
        return number

    def generate_email_address(self):
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
            "comcast.net"
        ]
        return f"{first_name_segment}{last_name_segment}{random_number}@{choice(providers)}"
    
    def generate_geographic_area(self):
        return choice(list(AREAS_AND_CITIES))

def generate_city_from_geographic_area(geographic_area):
    print(choice(AREAS_AND_CITIES[geographic_area]))
    return choice(AREAS_AND_CITIES[geographic_area])

person = Person(get_first_name(), get_last_name())

first_name = person.first_name
last_name = person.last_name
email_address = person.generate_email_address()
geographic_area = person.generate_geographic_area()
print(geographic_area)

generate_city_from_geographic_area(geographic_area)