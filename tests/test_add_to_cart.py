import allure
import pytest

from base.base_test import TestBase


@pytest.mark.TestAddProductToCart
@allure.title("Test add product to cart")
@allure.description("Test for adding product to cart")
@pytest.mark.normal
class TestAddProductToCart(TestBase):
    """Click on the hamburger menu, select 'Cameras' category,
    choose a product from the category,
    open the product's page and add the product to the cart.
    Close the popup.
    Click on the cart and check if the product has been added and the quantity of the product."""

    @allure.step("Click on the hamburger menu."
                 "Select 'Cameras' category."
                 "Open a product."
                 "Click on 'Add to cart' button."
                 "Close the popup."
                 "Click on the cart.")
    @pytest.mark.usefixtures("add_product_to_cart_fixture")
    def test_add_product_to_cart(self, add_product_to_cart_fixture):
        # Use the fixture for selecting category and clicking on the 'Add to cart' button
        product_page = add_product_to_cart_fixture
        product_title = "HTC Touch HD"

        # Close the popup
        product_page.close_popup_if_present()

        # Open the cart side menu
        cart_side_menu_page = self.home_page.click_cart()

        # Get the product name and quantity from the cart
        cart_product_name = cart_side_menu_page.get_cart_product_name()
        cart_product_quantity = cart_side_menu_page.get_cart_product_quantity()

        # Assert that the product name and quantity in the cart match expectations
        assert cart_product_name == product_title, (
            f"Expected product '{product_title}' not found in the cart, "
            f"found '{cart_product_name}' instead."
        )
        assert cart_product_quantity == "x1", (
            f"Expected quantity 'x1' for product '{product_title}', "
            f"but found '{cart_product_quantity}'"
        )
