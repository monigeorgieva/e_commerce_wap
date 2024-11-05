import allure

from pages.base_page import BasePage
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.shopping_cart_locators import CartSideMenuLocators


class CartSideMenuPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CartSideMenuLocators()

    def get_cart_product_name(self):
        """Return the name of the product in the cart."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.cart_product)
            )
            return self.driver.find_element(*self.locators.cart_product).text
        except TimeoutException as e:
            allure.attach(f"Timeout: Cart product name did not become visible: {e}", name="Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except NoSuchElementException as e:
            allure.attach(f"No such element: Cart product name not found: {e}", name="Element not found",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except Exception as e:
            allure.attach(f"An error occurred while retrieving cart product name: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def get_cart_product_quantity(self):
        """Return the quantity of the product in the cart."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.cart_product_quantity)
            )
            return self.driver.find_element(*self.locators.cart_product_quantity).text
        except TimeoutException as e:
            allure.attach(f"Timeout: Cart product quantity did not become visible: {e}", name="Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except NoSuchElementException as e:
            allure.attach(f"No such element: Cart product quantity element not found: {e}", name="Element not found",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except Exception as e:
            allure.attach(f"An error occurred while retrieving cart product quantity: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise