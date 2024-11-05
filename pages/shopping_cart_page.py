import allure
from selenium.common import NoSuchElementException, ElementNotInteractableException, TimeoutException

from pages.base_page import BasePage
from pages.empty_cart_page import EmptyCartPage
from locators.shopping_cart_locators import ShoppingCartPageLocators


class ShoppingCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ShoppingCartPageLocators()

    def get_shopping_cart_product_name(self):
        """Return the name of the product in the cart."""
        try:
            product_name_element = self.driver.find_element(*self.locators.product_name)
            return product_name_element.text
        except NoSuchElementException as e:
            allure.attach(f"No such element: Product name not found in cart: {e}", name="Product Not Found",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except TimeoutException as e:
            allure.attach(f"Timeout: Failed to locate product name in cart within the allotted time: {e}",
                          name="Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except Exception as e:
            allure.attach(f"An error occurred while trying to get the product name in the cart: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def get_shopping_cart_product_quantity(self):
        """Return the quantity of the product in the cart."""
        try:
            input_field = self.driver.find_element(*self.locators.quantity_input_field)
            current_value = input_field.get_attribute("value")
            return current_value
        except NoSuchElementException as e:
            allure.attach(f"No such element: Product quantity not found in cart: {e}",
                          name="Product Quantity not found",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except TimeoutException as e:
            allure.attach(f"Timeout: Failed to locate product quantity in cart within the allotted time: {e}",
                          name="Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except Exception as e:
            allure.attach(f"An error occurred while trying to get the product quantity in the cart: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def update_product_quantity(self, value):
        """Clear the value, update the input value and click the button to update the quantity of the product."""
        try:
            self.set(locator=self.locators.quantity_input_field, value=value)
            self.find(*self.locators.update_quantity_button).click()
            new_quantity = self.get_shopping_cart_product_quantity()
            return new_quantity

        except NoSuchElementException as e:
            allure.attach(f"No such element: Update button or quantity input field is not found: {e}",
                          name="Update button/Quantity not found",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except ElementNotInteractableException as e:
            allure.attach(f"Element is not interactable: {e}",
                          name="Element not interactable",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except TimeoutException as e:
            allure.attach(f"Timeout: Timed out while waiting for the update button or quantity input: {e}",
                          name="Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except Exception as e:
            allure.attach(f"An unexpected error occurred: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def remove_product(self):
        """Click the button to remove the product from the cart."""
        try:
            self.driver.find_element(*self.locators.remove_items_button).click()
            return EmptyCartPage(self.driver)
        except NoSuchElementException as e:
            allure.attach(f"No such element: Remove items button not found on the Cart page: {e}",
                          name="Button not found",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except Exception as e:
            allure.attach(f"An unexpected error occurred: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise
