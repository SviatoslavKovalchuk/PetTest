from selenium.webdriver.common.by import By

from utilities.web_ui.locators import Locators


class CheckoutPageLocators:
    def __init__(self):
        self.__first_name = Locators(By.XPATH, "//*[@id='first-name']")
        self.__last_name = Locators(By.XPATH, "//*[@id='last-name']")
        self.__postal_code = Locators(By.XPATH, "//*[@id='postal-code']")
        self.__cancel_btn = Locators(By.XPATH, "//*[@id='cancel']")
        self.__continue_btn = Locators(By.XPATH, "//*[@id='continue']")

    @property
    def first_name(self):
        return self.__first_name.find_locator()

    @property
    def last_name(self):
        return self.__last_name.find_locator()

    @property
    def postal_code(self):
        return self.__postal_code.find_locator()

    @property
    def cancel_btn(self):
        return self.__cancel_btn.find_locator()

    @property
    def continue_btn(self):
        return self.__continue_btn.find_locator()

