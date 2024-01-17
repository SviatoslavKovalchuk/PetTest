from selenium.webdriver.common.by import By

from utilities.web_ui.locators import Locators


class CartPageLocators:
    def __init__(self):
        self.__continue_shopping_btn = Locators(By.XPATH,
                                                '//*[@id="continue-shopping"]')
        self.__remove_btn = Locators(By.XPATH,
                                     '//*[@id="remove-sauce-labs-backpack"]')
        self.__checkout_btn = Locators(By.XPATH,
                                       '//*[@id="checkout"]')
        self.__test_locator = Locators(By.XPATH,
                                       "//*[@class='inventory_item_name']")

    @property
    def continue_shopping_btn(self):
        return self.__continue_shopping_btn.find_locator()

    @property
    def remove_btn(self):
        return self.__remove_btn.find_locator()

    @property
    def checkout_btn(self):
        return self.__checkout_btn.find_locator()

    @property
    def test_locator(self):
        return self.__test_locator.find_locator()
