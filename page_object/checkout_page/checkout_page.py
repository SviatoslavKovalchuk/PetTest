from page_object.checkout_page.checkout_page_locators import CheckoutPageLocators
from utilities.web_ui.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CheckoutPageLocators()

    def enter_first_name(self, first_name: str):
        self.send_keys(self.locators.first_name, first_name)

    def enter_last_name(self, last_name: str):
        self.send_keys(self.locators.last_name, last_name)

    def enter_zip_code(self, postal_code: int):
        self.send_keys(self.locators.postal_code, postal_code)

    def click_continue_btn(self):
        self.click(self.locators.continue_btn)

    def confirm_order(self, first_name: str, last_name: str, postal_code: int):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_zip_code(postal_code)
        self.click_continue_btn()
