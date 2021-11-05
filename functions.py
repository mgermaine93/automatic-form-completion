from random import randint
from names import get_first_name, get_last_name


def generate_first_name():
    # print(get_first_name())
    return get_first_name()


def generate_last_name():
    # print(get_last_name())
    return get_last_name()


def get_email_provider():
    providers = [
        "gmail.com",
        "outlook.com",
        "yahoo.com",
        "hotmail.com",
        "aol.com"
    ]
    # print(providers[randint(0, len(providers))])
    return providers[randint(0, len(providers))]


def generate_email_address():
    pass


def generate_phone_number():
    number = ""
    for i in range(12):
        if i == 3 or i == 7:
            number += "-"
        else:
            number += str(randint(0, 9))
    # print(number)
    return number


# generate_first_name()
# generate_last_name()
# generate_phone_number()
