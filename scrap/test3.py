# task = randomly return a number between 1 and 3, inclusive.
# then return indices at which to check, exclusive
from random import choice, randint


def generate_int_between_one_and_three():
    return choice(range(1, 4))


# checks an option(s) on how to help
ways_to_help = [0, 1, 2]


def check_options(num_options=generate_int_between_one_and_three()):
    if num_options == 3:
        return "Checked all three boxes."
    elif num_options == 2:
        first_box = ways_to_help[randint(0, 2)]
        second_box = ways_to_help[randint(0, 2)]
        while second_box == first_box:
            second_box = ways_to_help[randint(0, 2)]
        return f"Checked box {first_box} and box {second_box}."
    else:
        return "Checked one box."


print(check_options())
