import allure
import pytest

from base.base_test import TestBase


@pytest.mark.TestUpdateTheQuantityInTheCart
@allure.title("Test update the quantity of the products")
@allure.description("Test for updating the quantity of the products")
@pytest.mark.normal
class TestUpdateTheQuantityInTheCart(TestBase):
    """Click on the hamburger menu, select 'Cameras' category,
       choose a product from the category,
       open the product's page and add the product to the cart.
       Click on the popup "View Cart" button, go to the Cart page.
       Update the quantity of the product in the input field and click on the update quantity button."""

    @allure.step("Click on the hamburger menu."
                 "Select 'Cameras' category."
                 "Open a product."
                 "Click on 'Add to cart' button."
                 "Click on the 'View Cart' button."
                 "Clear the value in the input."
                 "Send new value."
                 "Click on the update button.")
    @pytest.mark.usefixtures("add_product_to_cart_fixture")
    def test_update_the_product_quantity(self, add_product_to_cart_fixture):
        # Use the fixture for selecting category and clicking on the 'Add to cart' button
        product_page = add_product_to_cart_fixture
        shopping_cart_page = product_page.click_on_view_cart_popup()

        # Get the current quantity
        current_quantity = shopping_cart_page.get_shopping_cart_product_quantity()
        # Update the quantity of the product from 1 to 5
        new_quantity = shopping_cart_page.update_product_quantity(5)

        # Assert that the URL is for the checkout/cart
        assert "https://ecommerce-playground.lambdatest.io/index.php?route=checkout/cart" in self.browser.current_url
        # Assert that the current quantity is 1
        assert current_quantity == '1', "The current product quantity in the cart should be 1."
        # Assert that the new quantity after the update is 5
        assert new_quantity == '5', "The product quantity in the cart should be updated to 5."

