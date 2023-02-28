import allure
import pytest
import os
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
from allure_commons.types import AttachmentType


class Helper:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

    def accept_alert(self):
        '''
        Данный метод принимает алерт
        '''
        your_alert = self.driver.switch_to.alert
        your_alert.accept()

    def dismiss_alert(self):
        your_alert = self.driver.switch_to.alert
        your_alert.dismiss()

    def find(self, locator):
        '''
        Данный метод ищет элемент на странице
        :param locator: Картеж
        :return: Веб-элемент
        '''
        self.wait.until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        return self.driver.find_elements(*locator)

    def click_on(self, locator, assertion_message):
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            self.find(locator).click()
        except:
            raise AssertionError(assertion_message)

    def enter_text(self, locator, text, check_value=False):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.find(locator).send_keys(text)
        if check_value is True:
            assert self.find(locator).get_attribute("value") == text, "Текст не совпадает"

    def upload_file(self, locator, source):
        self.find(locator).send_keys(source)

    def download_file(self, locator):
        self.find(locator).click()

    def save_cookies(self):
        pickle.dump(self.driver.get_cookies(), open(os.getcwd() + "/data/temp/cookies.pkl", "wb"))

    def load_cookies(self):
        cookies = pickle.load(open(os.getcwd()+"/data/temp/cookies.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def select_by_value(self, locator, value):
        dropdown = Select(self.find(locator))
        dropdown.select_by_value(value)

    def select(self, locator, value):
        self.find(locator).send_keys(value, Keys.ENTER)

    def make_screenshot(self, name):
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)