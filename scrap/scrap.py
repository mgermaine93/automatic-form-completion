# print(get_closest_area_code('ME', 'Derry'))
# area = generate_geographic_area()
# print(area)
# print(type(area))

# person = Person()
# print(person.first_name)
# print(person.last_name)
# print(person.city_and_state)
# print(person.get_geographic_area())
# print(person.generate_phone_number())
# print(person.generate_email_address())

# area = generate_geographic_area()
# city_and_state = generate_city_and_state(area)

# print(area)
# print(city_and_state)


# def get_city_from_city_and_state(city_and_state):
#     """
#     Needs docstring
#     """
#     if isinstance(city_and_state, Mapping):
#         # city will always be the key
#         return list(city_and_state.keys())[0]
#     else:
#         return f"{city_and_state} is not of type dict."


# def get_state_from_city_and_state(city_and_state):
#     """
#     Needs docstring
#     """
#     if isinstance(city_and_state, Mapping):
#         # city will always be the key
#         return list(city_and_state.values())[0]
#     else:
#         return f"{city_and_state} is not of type dict."


# print(get_city_from_city_and_state({'Waterloo': 'NE'}))
# print(get_state_from_city_and_state({'Waterloo': 'NE'}))


# person = Person()
# print(person.city_and_state)
# print(person.city)
# print(person.state)
# same_named_group = make_group_of_people(3)

# for person in same_named_group:
#     print(f"***NEW PERSON {same_named_group.index(person)}***")
#     print(person.first_name)
#     print(person.last_name)
#     print(person.city_and_state)


# person = Person(first_name="Edwin", last_name="Frazier",
#                 city_and_state={'Houghton', 'MI'})
# print(person.first_name)
# print(person.last_name)
# print(person.generate_email_address())
# print(person.city_and_state)
# print(person.city)
# print(person.state)
# print(person.generate_phone_number())
# print(person.get_geographic_area())
# generate_city_and_state()


### SCRAP STUFF THAT MIGHT BE NEEDED LATER ###


# def generate_city():
#     """
#     Needs docstring
#     """
#     geographic_areas = list(AREAS_AND_CITIES.keys())
#     geographic_area = choice(geographic_areas)
#     return choice(AREAS_AND_CITIES[geographic_area])


# def generate_random_geographic_area():
#     """
#     Needs docstring
#     """
#     random_geographic_area = choice(list(AREAS_AND_CITIES.keys()))
#     return random_geographic_area

# if geographic_area in AREAS_AND_CITIES.keys():
#     city = ""
#     city = choice(AREAS_AND_CITIES[geographic_area])
#     # state = geographic_area[-2:]
#     # city_and_state[city] = state
#     return city
# else:
#     return f"{geographic_area} wasn't found in the list of available areas and cities."


# def generate_phone_number(state, city):
#     first_three = get_closest_area_code(state, city)
#     last_seven = generate_last_seven_digits_of_phone_number()
#     return f"{first_three}{last_seven}"
# print(generate_city())
# print(get_closest_area_code("bloomenthal", "mackinac city"))


# def generate_city_and_state(geographic_area):
#     """
#     Needs docstring
#     """
#     if geographic_area in AREAS_AND_CITIES.keys():
#         city_and_state = {}
#         city = choice(AREAS_AND_CITIES[geographic_area])
#         state = geographic_area[-2:]
#         city_and_state[city] = state
#         return city_and_state
#     else:
#         return f"{geographic_area} wasn't found in the list of available areas and cities."

# def generate_random_location():
#     # This function will likely be very helpful!
#     """
#     Needs docstring
#     """
#     random_geographic_area = choice(list(AREAS_AND_CITIES.keys()))
#     random_city_within_geographic_area = choice(
#         AREAS_AND_CITIES[random_geographic_area])
#     return {random_city_within_geographic_area, random_geographic_area}
# print(get_closest_area_code("mi", "rOyAl oak"))
# print(get_geographic_area("Detroit"))
# print(generate_random_location())

# def generate_phone_number(area_code):
#     city_and_state =
#     print(city_and_state)
#     # full_state_name = get_full_state_name()
#     # print(full_state_name)


# print(get_cities_and_area_codes_in_state("Michigan"))

# person = Person()
# print(person.first_name)
# print(person.last_name)
# print(person.geographic_area)
# print(person.generate_email_address())
# print(person.generate_city())
# print(person.generate_state())


# get_cities_and_area_codes_in_state("Michigan")
# get_closest_area_code("Michigan", "Detroit")
# get_closest_area_code("Michigan", "Royal Oak")
# person = Person(get_first_name(), get_last_name())

# first_name = person.first_name
# last_name = person.last_name
# email_address = person.generate_email_address()
# geographic_area = person.generate_geographic_area()
# print(geographic_area)

# generate_city_from_geographic_area(geographic_area)
