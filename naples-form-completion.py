# https://www.youtube.com/watch?v=_ST_6heCS2I
from dotenv import load_dotenv
from random import choice, randint
import os
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from floridian import (
    make_group_of_floridians
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
LINK = os.environ.get("NAPLES_LINK")


def complete_naples_form(num_times):

    people = make_group_of_floridians(num_times)

    # Thanks to https://python-forum.io/Thread-MaxRetryError-while-scraping-a-website-multiple-times
    driver = webdriver.Chrome(PATH)
    driver.get(LINK)
    seconds = list(range(3, 11))

    for person in people:

        sleep(choice(seconds))

        # if driver.find_elements_by_class_name("dmforminput.small-12.dmRespDesignCol.medium-12.large-12.input"):
        #     # retrieves a list of all available textboxes (should be 7 items with the florida link)
        #     text_fields = driver.find_elements_by_class_name(
        #         "dmforminput.small-12.dmRespDesignCol.medium-12.large-12.input")
        # else:
        #     raise NoSuchElementException(
        #         "Could not find a list of textboxes.  Either the class name is incorrect in the script, or something changed with the form.")

        name_field = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[4]/div/div/div/div[9]/div/div/div[3]/div[1]/form/div[1]/input[1]")
        full_name = f"{person.first_name} {person.last_name}"
        name_field.send_keys(full_name)
        sleep(choice(seconds))

        email_field = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[4]/div/div/div/div[9]/div/div/div[3]/div[1]/form/div[2]/input[1]")
        email_field.send_keys(person.generate_email_address())
        sleep(choice(seconds))

        phone_number_field = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[4]/div/div/div/div[9]/div/div/div[3]/div[1]/form/div[3]/input[1]")
        phone_number_field.send_keys(person.generate_phone_number())
        sleep(choice(seconds))

        # # sends in the first name
        # # name = text_fields[0]
        # full_name = f"{person.first_name} {person.last_name}"
        # name.send_keys(full_name)
        # sleep(choice(seconds))

        # # sends in the email address
        # email_address = text_fields[2]
        # email_address.send_keys(person.generate_email_address())
        # sleep(choice(seconds))

        # # sends in the phone number
        # phone_number = text_fields[3]
        # phone_number.send_keys(person.generate_phone_number())
        # sleep(choice(seconds))

        # submits the form
        if driver.find_element_by_xpath(
                "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[4]/div/div/div/div[9]/div/div/div[3]/div[1]/form/div[4]/input"):
            submit_button = driver.find_element_by_xpath(
                "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[2]/div[4]/div/div/div/div[9]/div/div/div[3]/div[1]/form/div[4]/input")
        else:
            raise NoSuchElementException(
                "Could not find a submit button.  Either the class name of the button has changed, or something is different with the form.")

        submit_button.click()
        sleep(choice(seconds))

        print(f"{person.first_name} {person.last_name} from {person.get_city()}, {person.get_county()}, FL, was added to the form.")

        # prevents clicking the "add new response" button if the list of people has been exhausted
        if people.index(person) < len(people) - 1:
            another_response = driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            another_response.click()
            sleep(choice(seconds))
        else:
            print(f"{person.first_name} {person.last_name} from {person.get_city()}, {person.get_county()}, FL, was the last person.")

    driver.quit()


complete_naples_form(1)
