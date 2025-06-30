
import pytest
import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from selenium import webdriver
from pageObjects.loginPage import LoginPage

class TestLogin:

    baseURL = "https://www.saucedemo.com/"
    email = "standard_user"
    password = "secret_sauce"

    def test_login_page_title(self,setup):
        self.driver = setup
        assert self.driver.title == "Swag Labs", "Navigation to page failed"
        self.driver.close()

    def test_login_success(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.title = self.lp.login(self.email, self.password)
        time.sleep(5)
        if(self.title == "Swag labs"):
           self.driver.close()
           assert True
        else:
           self.driver.save_screenshot("day17_selenium_practice2\\screenshots\\screenshot.png")
           self.driver.close()
           assert False, "Login failed or title does not match expected value."
        
        
