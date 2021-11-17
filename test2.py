from person import (
    Person,
    generate_city_and_state,
    generate_geographic_area
)
from names import get_first_name, get_last_name

# newlist = [x for x in fruits if x != "apple"]
# https://stackoverflow.com/questions/30420621/python-creating-object-instances-in-a-loop-with-independent-handling
# https://pypi.org/project/names/


class Person():
    def __init__(self, first_name=get_first_name(), last_name=get_last_name()):
        self.first_name = first_name
        self.last_name = last_name


def make_group_of_people(num_people):
    people = []
    num = 0
    while num < num_people:
        person = Person(
            first_name=get_first_name(),
            last_name=get_last_name(),
        )
        people.append(person)
        num += 1
    return people


group = make_group_of_people(3)

for person in group:
    print(f"***NEW PERSON {group.index(person)}***")
    print(person.first_name)
    print(person.last_name)


def make_group_of_people_2(num_people):
    people = []
    num = 0
    while num < num_people:
        person = Person()
        people.append(person)
        num += 1
    return people


same_named_group = make_group_of_people_2(3)

for person in same_named_group:
    print(f"***NEW PERSON {same_named_group.index(person)}***")
    print(person.first_name)
    print(person.last_name)


# def make_group_of_people(num_people):
#     people = []
#     for num in range(num_people):
#         person = Person(
#             first_name=get_first_name(),
#             last_name=get_last_name(),
#             city_and_state=generate_city_and_state(generate_geographic_area())
#         )
#         people.append(person)
#     return people
