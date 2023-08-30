from page_object.item_preview_page.item_preview_locators import ItemPageLocators
from utilities.web_ui.base_page import BasePage


class ItemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ItemPageLocators()

    def click_back_to_products_btn(self):
        return self.click(self.locators.back_to_products_btn)

    def click_add_to_cart_button(self):
        return self.click(self.locators.add_to_cart_button)

    def click_remove_btn(self):
        return self.click(self.locators.remove_btn)

    def back_to_products_btn_is_visible(self):
        return self.is_visible(self.locators.back_to_products_btn)