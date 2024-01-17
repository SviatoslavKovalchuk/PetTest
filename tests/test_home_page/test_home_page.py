import pytest


def test_preview_item(open_login_page, open_item_page):
    """"
    Verify that user could open selected item
    Verify that the user redirected to item preview page
    Verify that the user can back to dashboard page
    """
    login_page = open_login_page
    dashboard = login_page.login('standard_user', 'secret_sauce')
    dashboard.click_item()
    item = open_item_page
    assert item.back_to_products_btn_is_visible()
    item.click_back_to_products_btn()
    assert dashboard.is_logo_visible()


def test_add_item_to_the_cart_and_continue(
        open_login_page, open_item_page, open_car_page):
    """"
        Verify that user can add selected item to the cart
        Verify that the user redirected to cart page
        Verify that the user can leave cart page via clicking continue btn

    """
    login_page = open_login_page
    dashboard = login_page.login('standard_user', 'secret_sauce')
    dashboard.click_add_to_cart_btn()
    dashboard.click_cart_container()
    cart = open_car_page
    cart.click_continue_shopping_btn()
    assert dashboard.is_logo_visible()


@pytest.mark.smoke
def test_user_can_remove_item_from_dashboard(
        open_login_page, open_item_page, open_car_page):
    """"
        Verify that the user can remove item from cart on dashboard page

    """
    login_page = open_login_page
    dashboard = login_page.login('standard_user', 'secret_sauce')
    dashboard.click_add_to_cart_btn()
    dashboard.click_cart_container()
    cart = open_car_page
    cart.click_continue_shopping_btn()
    dashboard.click_remove_btn()
    dashboard.click_cart_container()
    assert cart.added_item_is_visible() is False


@pytest.mark.smoke
def test_full_order(
        open_login_page, open_item_page,
        open_car_page, open_checkout_page,
        open_checkout_overview_page):
    """"
    Verify that user could add item to the cart
    Verify that the user could create the order
    Verify that the user can switch back to dashboard page
    """
    login_page = open_login_page
    dashboard = login_page.login('standard_user', 'secret_sauce')
    dashboard.click_add_to_cart_btn()
    dashboard.click_cart_container()
    cart = open_car_page
    cart.click_checkout_btn()
    checkout = open_checkout_page
    checkout.confirm_order('user_1', 'test_1', 76000)
    overview = open_checkout_overview_page
    overview.click_finish_btn()
    overview.click_back_home_btn()
    assert dashboard.is_logo_visible() is True
