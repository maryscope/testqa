import allure

from data.data import Data
from data.links import Links
from libs.helper import Helper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.links = Links()
        self.data = Data()
        self.helper = Helper(driver)
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)

    def open(self):
        with allure.step(f"Открыть страницу {self.PAGE_URL}"):
            self.driver.get(self.PAGE_URL)

    @allure.step("Страница открыта")
    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))
        self.helper.make_screenshot("Page is opened")

