import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function", autouse=True)
def get_driver(request):

    if os.environ["BROWSER"] == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        request.cls.driver = driver
        yield
        driver.quit()

    elif os.environ["BROWSER"] == "firefox":
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        request.cls.driver = driver
        yield
        driver.quit()