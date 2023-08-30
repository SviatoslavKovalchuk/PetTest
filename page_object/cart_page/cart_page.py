from page_object.cart_page.cart_page_locators import CartPageLocators
from utilities.web_ui.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartPageLocators()

    def click_continue_shopping_btn(self):
        return self.click(self.locators.continue_shopping_btn)

    def click_remove_btn(self):
        return self.click(self.locators.remove_btn)

    def click_checkout_btn(self):
        return self.click(self.locators.checkout_btn)

    def added_item_is_visible(self):
        return self.is_visible(self.locators.test_locator)
