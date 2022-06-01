# https://www.youtube.com/watch?v=_ST_6heCS2I
from dotenv import load_dotenv
from random import choice
import os
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from coloradoan import (
    make_group_of_coloradoans
)

optionsforchrome = Options()
optionsforchrome.add_argument('--no-sandbox')
optionsforchrome.add_argument('--start-maximized')
optionsforchrome.add_argument('--disable-extensions')
optionsforchrome.add_argument('--disable-dev-shm-usage')
optionsforchrome.add_argument('--ignore-certificate-errors')
service = Service(ChromeDriverManager().install())

load_dotenv()

PATH = os.environ.get("CHROMEDRIVER_PATH")
LINK = os.environ.get("COLORADO_LINK")


def complete_colorado_form(num_times):

    coloradoans = make_group_of_coloradoans(num_times)

    # Thanks to https://python-forum.io/Thread-MaxRetryError-while-scraping-a-website-multiple-times
    driver = webdriver.Chrome(PATH)
    driver.get(LINK)
    seconds = list(range(3, 11))

    for person in coloradoans:

        sleep(choice(seconds))

        if driver.find_elements_by_class_name('whsOnd.zHQkBf'):
            # retrieves a list of all available textboxes (should be 6 items with the hawaii link)
            textboxes = driver.find_elements_by_class_name(
                'whsOnd.zHQkBf')
        else:
            raise NoSuchElementException(
                "Could not find a list of textboxes.  Either the class name is incorrect in the script, or something changed with the form.")

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

        # sends in the county
        email_address = textboxes[4]
        email_address.send_keys(person.county)
        sleep(choice(seconds))

        # submits the form
        if driver.find_element_by_xpath(
                "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span"):
            submit_button = driver.find_element_by_xpath(
                "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")
        else:
            raise NoSuchElementException(
                "Could not find a submit button.  Either the class name of the button has changed, or something is different with the form.")

        submit_button.click()
        sleep(choice(seconds))

        print(f"{person.first_name} {person.last_name} from the county of {person.county} was added to the form.")

        # prevents clicking the "add new response" button if the list of people has been exhausted
        if coloradoans.index(person) < len(coloradoans) - 1:
            another_response = driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            another_response.click()
            sleep(choice(seconds))
        else:
            print(
                f"{person.first_name} {person.last_name} from the county of {person.county} was the last person.")

    driver.quit()


complete_colorado_form(100)
