from page_object.checkout_overview_page.checkout_overview_locators import CheckoutOverviewPageLocators
from utilities.web_ui.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CheckoutOverviewPageLocators()

    def click_finish_btn(self):
        self.click(self.locators.finish_btn)

    def click_cancel_co_btn(self):
        """
        test for  docstring (missing-function-docstring)

        """
        self.click(self.locators.cancel_checkout_overview_btn)

    def click_back_home_btn(self):
        """
        test for  docstring (missing-function-docstring)

        """
        self.click(self.locators.back_home_btn)

