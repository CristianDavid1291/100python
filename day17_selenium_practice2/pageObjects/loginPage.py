from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_txt = (By.ID,"user-name")
        self.password_txt = (By.ID,"password")
        self.login_btn = (By.ID,"login-button")
    
    def login(self, email, password):
        self.driver.find_element(*self.email_txt).send_keys(email)
        self.driver.find_element(*self.password_txt).send_keys(password)
        self.driver.find_element(*self.login_btn).click()
        return self.driver.title

