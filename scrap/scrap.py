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


### SCRAP STUFF THAT MIGHT BE NEEDED LATER ###


# first_name.send_keys(generate_first_name())
# sleep(random.choice(seconds))
# print("First name added.")

# # last name (text)
# last_name = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#     (By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")))
# sleep(random.choice(seconds))
# first_name.send_keys(generate_last_name())
# sleep(random.choice(seconds))
# print("Last name added.")

# cell number (text)
# email address (text)
# area (checkbox)
# city (text)

# try:
#     # This is the name of the google search bar field
#     first_name = driver.find_element(
#         By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
#     print("Success!")
# except NoSuchElementException as e:
#     print(f"No such element found:  {e}")

# # retrieves the google image search results using the phrase provided
# search_bar.send_keys(search_term)
# search_bar.send_keys(Keys.RETURN)
# search_results = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
#     (By.ID, 'islrg')))
# print("Initial image search worked.")

# # waits for the "Tools" button to load and clicks it
# tools_menu = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
#     (By.CSS_SELECTOR, ".PNyWAd.ZXJQ7c")))
# sleep(random.choice(seconds))
# tools_menu.click()
# print("Tool menu was found and clicked.")

# # clicks the "Size" dropdown (revealed by clicking the "Tools" button) once it is clickable
# size_menu = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
#     (By.CSS_SELECTOR, ".xFo9P.r9PaP")))
# sleep(random.choice(seconds))
# size_menu.click()
# print("Size option was found and clicked.")

# # selects the "Large" size option to filter large image sizes only.
# large_option = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
#     (By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[2]/div/span')))
# sleep(random.choice(seconds))
# large_option.click()
# print("Large option was found and clicked.")

# # clicks on the first large image
# large_image = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
#     (By.CSS_SELECTOR, '.rg_i.Q4LuWd')))
# sleep(random.choice(seconds))
# large_image.click()
# print("Large image was found and clicked.")

# # downloads and saves the large image to a local file
# large_image = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
#     (By.CSS_SELECTOR, '.n3VNCb')))
# sleep(random.choice(seconds))
# source = large_image.get_attribute("src")
# # https: // stackoverflow.com/questions/34957748/http-error-403-forbidden-with-urlretrieve
# # https://stackoverflow.com/questions/45358126/http-error-403-forbidden-while-downloading-file-using-urllib

# # Good practice, slows down the WebDriver
# sleep(random.choice(seconds))

# driver.quit()

# return f"{save_folder}/{search_term}_new_artwork.jpeg"
