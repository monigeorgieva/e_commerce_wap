import allure

from pages.base_page import BasePage
from locators.shopping_cart_locators import EmptyCartPageLocators
from selenium.common import NoSuchElementException, TimeoutException


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmptyCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = EmptyCartPageLocators

    def get_empty_cart_message(self):
        """Wait for the empty cart message element to be present, then get its text."""
        try:
            empty_cart_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.empty_cart_message)
            ).text
            return empty_cart_message
        except TimeoutException as e:
            allure.attach(f"Timeout: Empty cart message did not appear in the expected time: {e}", name="Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except NoSuchElementException as e:
            allure.attach(f"No such element: Empty cart message element not found: {e}", name="Element not found",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except Exception as e:
            allure.attach(f"An unexpected error occurred: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise

