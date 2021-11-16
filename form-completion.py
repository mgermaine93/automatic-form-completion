# https://www.youtube.com/watch?v=_ST_6heCS2I
from dotenv import load_dotenv
import urllib
from random import randint, choice
import os
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from person import Person

# from functions import generate_first_name, generate_last_name

optionsforchrome = Options()
optionsforchrome.add_argument('--no-sandbox')
optionsforchrome.add_argument('--start-maximized')
optionsforchrome.add_argument('--disable-extensions')
optionsforchrome.add_argument('--disable-dev-shm-usage')
optionsforchrome.add_argument('--ignore-certificate-errors')
service = Service(ChromeDriverManager().install())

load_dotenv()

PATH = os.environ.get("CHROMEDRIVER_PATH")
LINK = os.environ.get("LINK")


def complete_form(num_times):

    # https://stackoverflow.com/questions/21598872/how-to-create-multiple-class-objects-with-a-loop-in-python/21598969
    list_of_people = []
    people = [Person() for i in range(0, num_times)]
    for person in people:
        list_of_people.append(person)

    # https://stackoverflow.com/questions/30420621/python-creating-object-instances-in-a-loop-with-independent-handling
    for individual in list_of_people:
        print(individual.first_name)
    # # Thanks to https://python-forum.io/Thread-MaxRetryError-while-scraping-a-website-multiple-times
    # driver = webdriver.Chrome(PATH)
    # driver.get(LINK)
    # seconds = list(range(3, 11))

    # for person in people:

    #     sleep(choice(seconds))

    #     # retrieves a list of all available textboxes (should be 5 items with the current link)
    #     textboxes = driver.find_elements_by_class_name(
    #         "quantumWizTextinputPaperinputInput.exportInput")

    #     # sends in the first name
    #     first_name = textboxes[0]
    #     first_name.send_keys(person.first_name)
    #     sleep(choice(seconds))

    #     # sends in the last name
    #     last_name = textboxes[1]
    #     last_name.send_keys(person.last_name)
    #     sleep(choice(seconds))

    #     # sends in the phone number
    #     phone_number = textboxes[2]
    #     phone_number.send_keys(person.generate_phone_number())
    #     sleep(choice(seconds))

    #     # sends in the email address
    #     email_address = textboxes[3]
    #     email_address.send_keys(person.generate_email_address())
    #     sleep(choice(seconds))

    #     area_checkboxes = driver.find_elements_by_class_name(
    #         "docssharedWizToggleLabeledLabelText.exportLabel.freebirdFormviewerComponentsQuestionCheckboxLabel")

    #     # https://stackoverflow.com/questions/20996392/how-to-get-text-with-selenium-webdriver-in-python
    #     # # creates a list of all locations present on the form (not sure if needed any more)
    #     # area_location_labels = [
    #     #     area.text for area in area_checkboxes if isinstance(area.text, str)]
    #     # print(area_location_labels)
    #     geographic_area = person.get_geographic_area()
    #     # print(geographic_area)
    #     # https://stackoverflow.com/questions/2361426/get-the-first-item-from-an-iterable-that-matches-a-condition
    #     form_geographic_area_index = next((area_index for area_index in range(
    #         0, len(area_checkboxes)) if area_checkboxes[area_index].text == geographic_area), None)

    #     # print(form_geographic_area_index)

    #     # checks the corresponding geographic area checkbox
    #     if form_geographic_area_index:
    #         area_checkboxes[form_geographic_area_index].click()
    #     sleep(choice(seconds))

    #     # sends in the city and state
    #     city = textboxes[4]
    #     city.send_keys(f"{person.city}, {person.state}")
    #     sleep(choice(seconds))

    #     # submits the form
    #     submit_button = driver.find_element_by_class_name(
    #         "appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel")
    #     submit_button.click()
    #     sleep(choice(seconds))

    #     # # avoid infinite loop
    #     # i += 1

    #     # if i >= num_times:
    #     #     driver.close()
    #     # else:
    #     # pass
    #     # need to identify the "submit another response" button here
    #     another_response = driver.find_element_by_xpath(
    #         "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    #     # another_response = driver.find_element_by_class_name(
    #     #     "freebirdFormviewerViewResponseLinksContainer")
    #     another_response.click()
    #     sleep(choice(seconds))

    # driver.quit()


complete_form(3)


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
