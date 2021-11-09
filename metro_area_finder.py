# temporary function to be used to retrieve the surrounding towns and cities of a given larger city

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

# uses the link to the wikipedia page of a given town or city
link = "https://en.wikipedia.org/wiki/Tampa_Bay_area"

# temporary function to be used to retrieve the surrounding towns and cities of a given larger city


def find_metro_area_towns(num_times):

    # Thanks to https://python-forum.io/Thread-MaxRetryError-while-scraping-a-website-multiple-times
    driver = webdriver.Chrome(PATH)
    driver.get(link)
    seconds = [3, 4, 5, 6, 7, 8, 9, 10]

    # seconds = [3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(num_times):
        sleep(choice(seconds))

        towns = driver.find_elements_by_tag_name("a")
        towns_list = []
        for town in towns:
            towns_list.append(town.text)
        print(towns_list)

        sleep(choice(seconds))

        # avoid infinite loop
        i += 1

# driver.close()


find_metro_area_towns(1)
