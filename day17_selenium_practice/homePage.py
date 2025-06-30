from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.welcome_message = (By.CSS_SELECTOR, "h1.post-title")
       
    def get_welcome_message(self):
        return self.driver.find_element(*self.welcome_message).text


