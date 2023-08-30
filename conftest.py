import logging

import pytest

from page_object.cart_page.cart_page import CartPage
from page_object.checkout_overview_page.checkout_overview_page import CheckoutOverviewPage
from page_object.checkout_page.checkout_page import CheckoutPage
from page_object.item_preview_page.item_preview_page import ItemPage
from page_object.login_page.login_page import LoginPage
from utilities.driver_factory import DriverFactory
from utilities.read_configs import ReadConfig


@pytest.fixture()
def create_driver():
    chrome_driver = DriverFactory.create_driver(ReadConfig.get_browser_data())
    chrome_driver.get(ReadConfig.get_bas_url())
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def open_car_page(create_driver):
    return CartPage(create_driver)


@pytest.fixture()
def open_checkout_page(create_driver):
    return CheckoutPage(create_driver)


@pytest.fixture()
def open_item_page(create_driver):
    return ItemPage(create_driver)


@pytest.fixture()
def open_checkout_overview_page(create_driver):
    return CheckoutOverviewPage(create_driver)
