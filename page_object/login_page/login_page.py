import logging

from page_object.home_page.home_page import HomePage
from page_object.login_page.login_page_locators import LoginPageLocators
from utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__locators = LoginPageLocators()

    def enter_email(self, user_name):
        self.send_keys(self.__locators.email_input, user_name)
        return self

    def enter_password(self, password):
        self.send_keys(self.__locators.password_field, password)
        return self

    def press_login_btn(self):
        self.click(self.__locators.login_btn)
        return self

    def login(self, user_name, password):
        logging.info(f'entering user name{user_name}, '
                     f'entering password {password}')
        self.enter_email(user_name).enter_password(password).press_login_btn()
        return HomePage(self.driver)

    def error_message_is_visible(self):
        return self.is_visible(self.__locators.error_msg)

    def logo_is_visible(self):
        return self.is_visible(self.__locators.login_logo)
