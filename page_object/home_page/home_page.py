from page_object.cart_page.cart_page import CartPage
from page_object.home_page.home_page_locators import HomePageLocators
from utilities.web_ui.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators()

    def is_logo_visible(self):
        return self.is_visible(self.locators.logo)

    def click_burger_btn(self):
        return self.click(self.locators.burger_btn)

    def click_logout_btn(self):
        return self.click(self.locators.logout_btn)

    def click_add_to_cart_btn(self):
        return self.click(self.locators.add_to_cart)

    def click_cart_container(self):
        self.click(self.locators.cart_container)
        return CartPage(self.driver)

    def click_item(self):
        self.click(self.locators.backpack_item)

    def click_remove_btn(self):
        self.click(self.locators.remove_btn)
