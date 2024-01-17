from selenium.webdriver.common.by import By

from utilities.web_ui.locators import Locators


class CheckoutOverviewPageLocators:
    def __init__(self):
        self.__finish_btn = Locators(By.XPATH, "//*[@id='finish']")
        self.__cancel_co_btn = Locators(By.XPATH, "//*[@id='cancel']")
        self.__back_home_btn = Locators(By.XPATH,
                                        "//*[@id='back-to-products']")

    @property
    def finish_btn(self):
        return self.__finish_btn.find_locator()

    @property
    def cancel_checkout_overview_btn(self):
        return self.__cancel_co_btn.find_locator()

    @property
    def back_home_btn(self):
        return self.__back_home_btn.find_locator()
