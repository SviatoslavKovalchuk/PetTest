from selenium.webdriver.common.by import By

from utilities.web_ui.locators import Locators


class ItemPageLocators:
    def __init__(self):
        self.__back_to_products_btn = Locators(By.XPATH,
                                               "//*[@id='back-to-products']")
        self.__add_to_cart_button = Locators(
            By.XPATH,
            "//*[@class='btn btn_primary btn_small btn_inventory']")
        self.__remove_btn = Locators(
            By.XPATH,
            "//*[@class='btn btn_secondary btn_small btn_inventory']")

    @property
    def back_to_products_btn(self):
        return self.__back_to_products_btn.find_locator()

    @property
    def add_to_cart_button(self):
        return self.__add_to_cart_button.find_locator()

    @property
    def remove_btn(self):
        return self.__remove_btn.find_locator()
