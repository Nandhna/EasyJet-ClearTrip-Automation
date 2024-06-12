from selenium import webdriver
import time
import pytest



@pytest.fixture(scope="class")
def setup(request):

    driver = webdriver.Chrome()
    driver.get("https://www.cleartrip.ae/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()