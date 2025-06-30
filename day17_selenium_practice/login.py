from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # Wait for elements to load
        self.username_txt = (By.ID, "username")
        self.password_txt = (By.ID, "password")
        self.login_btn = (By.XPATH, "//button[contains(text(),'Submit')]")
      
    
    
    def login(self, username, password):
        #scroll until element self.login_btn be clickable
        self.driver.find_element(*self.username_txt).send_keys(username)
        self.driver.find_element(*self.password_txt).send_keys(password)
        self.driver.find_element(*self.login_btn).click()
        return self.driver


    
