"""
For testing goal you can try to use python package x-dist
pytest -n auto
With this call, pytest will spawn a number of workers processes
equal to the number of available CPUs, and distribute the tests randomly across them.
"""

import pytest


@pytest.mark.regression
def test_valid_login(open_login_page):
    """"
    Verify that user could properly log in to the site
    """
    login_page = open_login_page
    dashboard = login_page.login('standard_user', 'secret_sauce')
    assert dashboard.is_logo_visible() is True


@pytest.mark.regression
@pytest.mark.parametrize("invalid_password", [
    123456,
    'password123',
    'testpass',
])
def test_invalid_login(open_login_page, invalid_password):
    """"
    Verify that user cannot log in to the site
    Error message should display
    """
    login_page = open_login_page
    login_page.enter_email('standard_user')
    login_page.enter_password(invalid_password)
    login_page.press_login_btn()
    assert login_page.error_message_is_visible() is True


@pytest.mark.regression
def test_logout(open_login_page):
    """"
    Verify that user could properly log in and logout
    """
    login_page = open_login_page
    dashboard = login_page.login('standard_user', 'secret_sauce')
    dashboard.click_burger_btn()
    dashboard.click_logout_btn()
    assert login_page.logo_is_visible() is True
