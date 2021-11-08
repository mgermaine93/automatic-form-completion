from random import randint
from names import get_first_name, get_last_name


class Person:
    def __init__(self):
        self.first_name = get_first_name
        self.last_name = get_last_name

    def first_name(self):
        return self.first_name

    def second_name(self):
        return self.last_name

    def get_email_provider(self):
        providers = [
            "gmail.com",
            "outlook.com",
            "yahoo.com",
            "hotmail.com",
            "aol.com",
            "comcast.net"
        ]
        # print(providers[randint(0, len(providers))])
        return providers[randint(0, len(providers))]

    def generate_email_address(self):
        pass
        # first_name_segment = self.first_name()[0, randint(first_name_length)]
        # last_name_length = len(self.last_name())
        # last_name_segment = self.last_name()[0, randint(last_name_length)]
        # provider = self.get_email_provider()
        # print(f"{first_name_segment}{last_name_segment}{provider}")
        # return f"{first_name_segment}{last_name_segment}{provider}"

    def generate_phone_number(self):
        number = ""
        for i in range(12):
            if i == 3 or i == 7:
                number += "-"
            else:
                number += str(randint(0, 9))
        # print(number)
        return number


def generate_first_name():
    # print(get_first_name())
    return get_first_name()


def generate_last_name():
    # print(get_last_name())
    return get_last_name()


# generate_first_name()
# generate_last_name()
# generate_phone_number()

person = Person()
print(person.first_name())
print(person.last_name())
print(person.generate_phone_number())
print(person.generate_email_address())
