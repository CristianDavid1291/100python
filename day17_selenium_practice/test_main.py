from selenium import webdriver
from selenium.webdriver.common.by import By
from login import LoginPage
from homePage import HomePage


def test_login():
    driver = webdriver.Chrome()
    loginPage = LoginPage(driver)
    homePage = HomePage(loginPage.login("student", "Password123"))
    assert "Logged In Successfully" in homePage.get_welcome_message(), "Login failed or welcome message not found"






