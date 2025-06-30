from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    return driver
