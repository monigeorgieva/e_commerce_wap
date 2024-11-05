import allure
from selenium.common import ElementClickInterceptedException

from pages.base_page import BasePage
from pages.product_page import ProductPage
from locators.category_page_locators import CategoryPageLocators


class CategoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoryPageLocators()

    def click_on_product(self):
        """Click on phone product."""
        try:
            product = self.wait_for_element_to_be_clickable(self.locators.phone_product)
            product.click()
            return ProductPage(self.driver)
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException: The product was not clickable. Retrying...")
            product = self.wait_for_element_to_be_clickable(self.locators.phone_product)
            product.click()
            return ProductPage(self.driver)
        except Exception as e:
            allure.attach(f"An error occurred while clicking the product: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise
