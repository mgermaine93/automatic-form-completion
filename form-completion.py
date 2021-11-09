# https://www.youtube.com/watch?v=_ST_6heCS2I
import urllib
from random import randint, choice
import os
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException, InvalidSelectorException
import requests
from PIL import Image
from urllib import request
import requests
from decouple import config
# from functions import generate_first_name, generate_last_name

optionsforchrome = Options()
optionsforchrome.add_argument('--no-sandbox')
optionsforchrome.add_argument('--start-maximized')
optionsforchrome.add_argument('--disable-extensions')
optionsforchrome.add_argument('--disable-dev-shm-usage')
optionsforchrome.add_argument('--ignore-certificate-errors')
service = Service(ChromeDriverManager().install())

# PATH = config('CHROMEDRIVER_PATH')

PATH = "/Users/mgermaine93/Desktop/CODE/automatic-form-completion/chromedriver"
link = "https://docs.google.com/forms/d/e/1FAIpQLSdPxyzHSveo4UnsRZSdsAWfUvp8abL8X_scMNtZGIBWAHArJA/viewform"


def complete_form(num_times):

    # Thanks to https://python-forum.io/Thread-MaxRetryError-while-scraping-a-website-multiple-times
    driver = webdriver.Chrome(PATH)
    driver.get(link)
    seconds = [3, 4, 5, 6, 7, 8, 9, 10]

    # seconds = [3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(num_times):
        sleep(choice(seconds))

        # quantumWizTextinputPaperinputInput exportInput
        # first name (text)
        textboxes = driver.find_elements_by_class_name(
            "quantumWizTextinputPaperinputInput.exportInput")

        first_name = textboxes[0]
        last_name = textboxes[1]
        phone_number = textboxes[2]
        email_address = textboxes[3]
        city = textboxes[4]

        # It's necessary to distinguish between the check labels and the checkboxes
        checkboxes_boxes = driver.find_elements_by_class_name(
            "quantumWizTogglePapercheckboxInnerBox.exportInnerBox")

        checkboxes_labels = driver.find_elements_by_class_name(
            "docssharedWizToggleLabeledLabelText.exportLabel.freebirdFormviewerComponentsQuestionCheckboxLabel")

        for box in checkboxes_labels:
            print(box.text)
        # random_checkbox = choice(checkboxes)
        # https://stackoverflow.com/questions/20996392/how-to-get-text-with-selenium-webdriver-in-python

        # print(random_checkbox.text)

        submit_button = driver.find_element_by_class_name(
            "appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel")

        # submit_button.click()

        # print(len(textboxes))
        # print(len(checkboxes))

        sleep(choice(seconds))

        # avoid infinite loop
        i += 1


# driver.close()

complete_form(1)

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
