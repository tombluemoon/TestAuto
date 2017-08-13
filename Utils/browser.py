import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from Stock.Conf import const


class BrowserUtils:

    def __init__(self):
        os.environ["PATH"] = os.path.dirname(os.getcwd()) + const.CONST_CHROME_PATH + ';' + os.environ["PATH"]
        print(os.environ["PATH"])

    @classmethod
    def open_new_browser_and_maximum(cls):
        driver = cls.__open_browser()
        driver.maximize_window()
        return driver

    @classmethod
    def __open_browser(cls):
        driver = webdriver.Chrome()
        driver.implicitly_wait(const.CONST_DELAY)
        return driver

    @classmethod
    def go_to_url(cls, driver, url, location_xpath):
        driver.get(url)
        WebDriverWait(driver, const.CONST_DELAY).until(ec.presence_of_element_located((By.XPATH, location_xpath)))
        return driver
