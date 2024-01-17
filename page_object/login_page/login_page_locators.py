from selenium.webdriver.common.by import By

from utilities.web_ui.locators import Locators


class LoginPageLocators:
    def __init__(self):
        """XPATH Locators:"""
        # self.__email_input = Locators(By.XPATH, '//*[@id="user-name"]')
        # self.__password_field = Locators(By.XPATH, '//*[@id="password"]')
        # self.__login_btn = Locators(By.XPATH, '//*[@id="login-button"]')
        # self.__error_msg = Locators(
        #     By.XPATH,
        #     '//*[contains(text(), "Epic sadface: Username and password do not match any user in this service")]')
        # self.__login_logo = Locators(By.XPATH, '//*[@class="login_logo"]')

        """CSS Locators:"""
        self.__email_input = Locators(By.CSS_SELECTOR, "input.input_error[name='user-name']")
        self.__password_field = Locators(By.CSS_SELECTOR, "input#password")
        self.__login_btn = Locators(By.CSS_SELECTOR, "input[id ='login-button']")
        self.__error_msg = Locators(
             By.CSS_SELECTOR, "button[class='error-button']")
        self.__login_logo = Locators(By.CSS_SELECTOR, "[class='login_logo']")

    @property
    def email_input(self):
        return self.__email_input.find_locator()

    @property
    def password_field(self):
        return self.__password_field.find_locator()

    @property
    def login_btn(self):
        return self.__login_btn.find_locator()

    @property
    def error_msg(self):
        return self.__error_msg.find_locator()

    @property
    def login_logo(self):
        return self.__login_logo.find_locator()
