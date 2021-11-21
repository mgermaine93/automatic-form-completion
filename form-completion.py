# https://www.youtube.com/watch?v=_ST_6heCS2I
from dotenv import load_dotenv
import urllib
from random import choice
import os
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from person import (
    make_group_of_people,
    get_city_from_city_and_state,
    get_state_from_city_and_state
)

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

    people = make_group_of_people(num_times)

    # Thanks to https://python-forum.io/Thread-MaxRetryError-while-scraping-a-website-multiple-times
    driver = webdriver.Chrome(PATH)
    driver.get(LINK)
    seconds = list(range(3, 11))

    for person in people:

        sleep(choice(seconds))

        # retrieves a list of all available textboxes (should be 5 items with the current link)
        textboxes = driver.find_elements_by_class_name(
            "quantumWizTextinputPaperinputInput.exportInput")

        # sends in the first name
        first_name = textboxes[0]
        first_name.send_keys(person.first_name)
        sleep(choice(seconds))

        # sends in the last name
        last_name = textboxes[1]
        last_name.send_keys(person.last_name)
        sleep(choice(seconds))

        # sends in the phone number
        phone_number = textboxes[2]
        phone_number.send_keys(person.generate_phone_number())
        sleep(choice(seconds))

        # sends in the email address
        email_address = textboxes[3]
        email_address.send_keys(person.generate_email_address())
        sleep(choice(seconds))

        area_checkboxes = driver.find_elements_by_class_name(
            "docssharedWizToggleLabeledLabelText.exportLabel.freebirdFormviewerComponentsQuestionCheckboxLabel")

        # https://stackoverflow.com/questions/20996392/how-to-get-text-with-selenium-webdriver-in-python
        # https://stackoverflow.com/questions/2361426/get-the-first-item-from-an-iterable-that-matches-a-condition
        geographic_area = person.get_geographic_area()
        form_geographic_area_index = next((area_index for area_index in range(
            0, len(area_checkboxes)) if area_checkboxes[area_index].text == geographic_area), None)

        # checks the corresponding geographic area checkbox
        if form_geographic_area_index:
            area_checkboxes[form_geographic_area_index].click()
        sleep(choice(seconds))

        # sends in the city and state
        city = textboxes[4]
        city.send_keys(
            f"{get_city_from_city_and_state(person.city_and_state)}, {get_state_from_city_and_state(person.city_and_state)}")
        sleep(choice(seconds))

        # submits the form
        submit_button = driver.find_element_by_class_name(
            "appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel")
        submit_button.click()
        sleep(choice(seconds))

        print(f"{person.first_name} {person.last_name} from {get_city_from_city_and_state(person.city_and_state)}, {get_state_from_city_and_state(person.city_and_state)} was added to the form")

        # prevents clicking the "add new response" button if the list of people has been exhausted
        if people.index(person) < len(people) - 1:
            another_response = driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            another_response.click()
            sleep(choice(seconds))
        else:
            print(f"{person.first_name} {person.last_name} from {get_city_from_city_and_state(person.city_and_state)}, {get_state_from_city_and_state(person.city_and_state)} was the last person.")

    driver.quit()


complete_form(5)
