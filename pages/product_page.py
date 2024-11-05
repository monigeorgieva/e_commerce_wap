import allure
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.common import TimeoutException

from pages.base_page import BasePage
from pages.shopping_cart_page import ShoppingCartPage
from locators.product_page_locators import ProductPageLocators


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductPageLocators()

    def click_add_to_cart(self):
        """Wait Add to cart button to be clickable and click it.
        Wait for the popup to appear."""
        try:
            add_to_cart_button = self.wait_for_element_to_be_clickable(self.locators.add_to_cart_button)
            add_to_cart_button.click()
            self.wait_for_popup_to_appear()
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException: Retrying click on add to cart button.")
            add_to_cart_button = self.wait_for_element_to_be_clickable(self.locators.add_to_cart_button)
            add_to_cart_button.click()
            self.wait_for_popup_to_appear()
        except TimeoutException as e:
            allure.attach(f"Timeout: Add to cart button did not become clickable: {e}", name="Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except NoSuchElementException as e:
            allure.attach(f"No such element: Add to cart button not found: {e}", name="Button not found",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except Exception as e:
            allure.attach(f"An error occurred while trying to add to cart: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def wait_for_popup_to_appear(self):
        """Waits for the popup to appear after adding a product to the cart."""
        try:
            self.wait_for_element_to_be_clickable(self.locators.popup_close_button)
            return True
        except TimeoutException as e:
            allure.attach(f"Timeout: Popup did not appear after adding to cart: {e}", name="Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except NoSuchElementException as e:
            allure.attach(f"No such element: Popup close button element not found: {e}", name="Button not found",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except Exception as e:
            allure.attach(f"An unexpected error occurred: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def close_popup_if_present(self):
        """Closes the popup if it appears after adding a product to the cart."""
        try:
            popup_close_button = self.wait_for_element_to_be_clickable(self.locators.popup_close_button)
            popup_close_button.click()
            return True
        except TimeoutException as e:
            allure.attach(f"Timeout: Popup close button did not appear: {e}", name="Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except NoSuchElementException as e:
            allure.attach(f"No such element: Popup close button not found: {e}", name="Button not found",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except Exception as e:
            allure.attach(f"An error occurred while trying to add to cart: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def click_on_view_cart_popup(self):
        """When the popup is present and button View cart, click on it."""
        try:
            pop_up_view_cart_button = self.find(*self.locators.popup_view_cart_button)
            if pop_up_view_cart_button.is_displayed():
                pop_up_view_cart_button.click()
                return ShoppingCartPage(self.driver)
            else:
                allure.attach("View Cart popup button is not displayed.", name="Button Not Displayed",
                              attachment_type=allure.attachment_type.TEXT)
                raise Exception("View Cart popup button is not displayed.")
        except TimeoutException as e:
            allure.attach(f"Timeout: View Cart popup button did not appear: {e}", name="Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise

        except NoSuchElementException as e:
            allure.attach(f"No such element: View Cart popup button not found: {e}", name="Button Not Found",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except Exception as e:
            allure.attach(f"An unexpected error occurred: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise
