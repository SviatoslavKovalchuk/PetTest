from selenium.webdriver.common.by import By

from utilities.web_ui.locators import Locators


class HomePageLocators:
    def __init__(self):
        """XPath Locators"""
        # self.__add_to_cart = Locators(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
        # self.__logo = Locators(By.XPATH, '//*[@id="header_container"]/div[1]/div[2]/div')
        # self.__burger_btn = Locators(By.XPATH, '//*[@id="react-burger-menu-btn"]')
        # self.__logout_btn = Locators(By.XPATH, '//*[@id="logout_sidebar_link"]')
        # self.__cart_container = Locators(By.XPATH, '//*[@class="shopping_cart_container"]')
        # self.__backpack_item = Locators(By.XPATH, "//*[@id='item_4_title_link']")
        # self.__remove_btn = Locators(By.XPATH, "//*[@id='remove-sauce-labs-backpack']")
        """CSS Locators"""
        self.__add_to_cart = Locators(By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-backpack')
        self.__logo = Locators(By.CSS_SELECTOR, 'div[class^="app"]')
        self.__burger_btn = Locators(By.CSS_SELECTOR, 'div.bm-burger-button[style="z-index: 1000;"]')
        self.__logout_btn = Locators(By.CSS_SELECTOR, 'a#logout_sidebar_link')
        self.__cart_container = Locators(By.CSS_SELECTOR, 'div[class = "shopping_cart_container"]')
        self.__backpack_item = Locators(By.CSS_SELECTOR, 'a#item_4_title_link')
        self.__remove_btn = Locators(By.CSS_SELECTOR, 'button[class="btn btn_secondary btn_small btn_inventory "]')

    @property
    def add_to_cart(self):
        return self.__add_to_cart.find_locator()

    @property
    def logo(self):
        return self.__logo.find_locator()

    @property
    def burger_btn(self):
        return self.__burger_btn.find_locator()

    @property
    def logout_btn(self):
        return self.__logout_btn.find_locator()

    @property
    def cart_container(self):
        return self.__cart_container.find_locator()

    @property
    def backpack_item(self):
        return self.__backpack_item.find_locator()

    @property
    def remove_btn(self):
        return self.__remove_btn.find_locator()


