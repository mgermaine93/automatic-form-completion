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
LINK = os.environ.get("FLORIDA_LINK")


def generate_int_between_one_and_three():
    return choice(range(1, 4))


def complete_florida_form(num_times):

    people = make_group_of_floridians(num_times)

    # Thanks to https://python-forum.io/Thread-MaxRetryError-while-scraping-a-website-multiple-times
    driver = webdriver.Chrome(PATH)
    driver.get(LINK)
    seconds = list(range(3, 11))

    for person in people:

        sleep(choice(seconds))

        if driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput.exportInput"):
            # retrieves a list of all available textboxes (should be 7 items with the florida link)
            textboxes = driver.find_elements_by_class_name(
                "quantumWizTextinputPaperinputInput.exportInput")
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
        county = textboxes[4]
        county.send_keys(person.get_county())
        sleep(choice(seconds))

        # sends in the city
        city = textboxes[5]
        city.send_keys(person.get_city())
        sleep(choice(seconds))

        if driver.find_elements_by_class_name(
                "docssharedWizToggleLabeledLabelText.exportLabel.freebirdFormviewerComponentsQuestionCheckboxLabel"):
            # this should be of length 3 with the florida form
            help_checkboxes = driver.find_elements_by_class_name(
                "docssharedWizToggleLabeledLabelText.exportLabel.freebirdFormviewerComponentsQuestionCheckboxLabel")
        else:
            raise NoSuchElementException(
                "Could not find a list of checkboxes.  Something must be different with the form.")

        # checks an option(s) on how to help
        ways_to_help = help_checkboxes

        def check_options(num_options=generate_int_between_one_and_three()):
            if num_options == 3:
                ways_to_help[0].click()
                ways_to_help[1].click()
                ways_to_help[2].click()
            elif num_options == 2:
                first_box = ways_to_help[randint(0, 2)]
                second_box = ways_to_help[randint(0, 2)]
                while second_box == first_box:
                    second_box = ways_to_help[randint(0, 2)]
                first_box.click()
                second_box.click()
            else:
                ways_to_help[randint(0, 2)].click()

        check_options()
        sleep(choice(seconds))

        # sends in the group
        group = textboxes[6]

        # "group" is an optional field in the form, so this is adds the option of randomly including (or not including) the group
        def send_in_group():
            choices = ["yes", "no"]
            action_to_take = choice(choices)
            return action_to_take
        action = send_in_group()
        if action == "yes":
            print("Sending in group.")
            group.send_keys(person.get_group())
            sleep(choice(seconds))
        else:
            print("Not sending in group.")
            sleep(choice(seconds))

        # submits the form
        if driver.find_element_by_class_name(
                "appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel"):
            submit_button = driver.find_element_by_class_name(
                "appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel")
        else:
            raise NoSuchElementException(
                "Could not find a submit button.  Either the class name of the button has changed, or something is different with the form.")

        submit_button.click()
        sleep(choice(seconds))

        print(f"{person.first_name} {person.last_name} from {person.city_and_state} and a member of {person.get_group()} was added to the form.")

        # prevents clicking the "add new response" button if the list of people has been exhausted
        if people.index(person) < len(people) - 1:
            another_response = driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
            another_response.click()
            sleep(choice(seconds))
        else:
            print(f"{person.first_name} {person.last_name} from {person.city_and_state} and a member of {person.get_group()} was the last person.")

    driver.quit()


# complete_florida_form(3)
