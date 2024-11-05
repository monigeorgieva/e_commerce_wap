import allure
import pytest

from base.base_test import TestBase


@pytest.mark.TestRemoveProductsFromTheCart
@allure.title("Test remove products from the cart")
@allure.description("Test for removing products from the cart")
@pytest.mark.normal
class TestRemoveProductsFromTheCart(TestBase):
    """Click on the hamburger menu, select 'Cameras' category,
       choose a product from the category,
       open the product's page and add the product to the cart.
       Click on the popup "View Cart" button, go to the Cart page.
       Click on the remove products button.
       Wait for the empty cart message."""

    @allure.step("Click on the hamburger menu."
                 "Select 'Cameras' category."
                 "Open a product."
                 "Click on 'Add to cart' button."
                 "Click on the 'View Cart' button."
                 "Click on the remove products button."
                 "Wait for the empty cart message.")
    @pytest.mark.usefixtures("add_product_to_cart_fixture")
    def test_remove_products_from_cart(self, add_product_to_cart_fixture):
        # Use the fixture for selecting category and clicking on the 'Add to cart' button
        product_page = add_product_to_cart_fixture

        # When the popup appears click on the 'View cart' button
        shopping_cart_page = product_page.click_on_view_cart_popup()

        # Remove the product from the cart
        empty_cart = shopping_cart_page.remove_product()
        # Wait for the empty cart message
        message = empty_cart.get_empty_cart_message()

        # Assert that the message is for the empty cart
        assert message == "Your shopping cart is empty!"
