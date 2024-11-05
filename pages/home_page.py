import allure
from selenium.common import WebDriverException, NoSuchElementException, TimeoutException, \
    ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.configuration import Configuration
from pages.base_page import BasePage
from pages.cart_side_menu_page import CartSideMenuPage
from pages.category_page import CategoryPage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        """Set up the base URLs and retrieve the URL for the Home Page."""
        try:
            self.base_url = Configuration().get_e_commerce_base_url()
        except FileNotFoundError as e:
            allure.attach(f"File not found: Error loading base URL from config: {e}", name="Config load error",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        self.locators = HomePageLocators()

    def load(self):
        """Loads the Home Page by navigating to the base URL."""
        try:
            self.driver.get(self.base_url)
        except WebDriverException as e:
            allure.attach(f"Failed to load the page: {e}", name="Page Load Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def is_main_icon_displayed(self):
        """Check if the main icon with the logo is displayed on the home page."""
        try:
            icon = self.find(*self.locators.main_icon)
            return icon.is_displayed()
        except NoSuchElementException as e:
            allure.attach(f"No such element: The icon not found: {e}", name="Element not found",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def enter_search_text(self, text):
        """Locate the search input, clear the field, send text to be searched using the set method."""
        try:
            self.set(locator=self.locators.search_bar_input, value=text)

        except NoSuchElementException as e:
            allure.attach(f"No such element: Search bar input not found: {e}", name="Element not found",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except ElementNotInteractableException as e:
            allure.attach(f"Search bar is not interactable: {e}", name="Element not interactable",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except TimeoutException as e:
            allure.attach(f"Timeout: Timed out while waiting for the search bar: {e}", name="Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except Exception as e:
            allure.attach(f"An unexpected error occurred: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def click_search_button(self):
        """Wait for the search button to be clickable and click it,
        if ElementClickInterceptedException occurs, retry the click after pause."""
        try:
            search_button = self.wait_for_element_to_be_clickable(self.locators.search_button)
            search_button.click()
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException: The search button was not clickable. Retrying...")
            search_button = self.wait_for_element_to_be_clickable(self.locators.search_button)
            search_button.click()
        except Exception as e:
            allure.attach(f"An error occurred while clicking the search button: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def click_hamburger_menu(self):
        """Wait for the hamburger menu to be clickable and click it,
           if ElementClickInterceptedException occurs, retry the click after pause."""
        try:
            hamburger_menu = self.wait_for_element_to_be_clickable(self.locators.hamburger_menu)
            hamburger_menu.click()
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException: The hamburger menu was not clickable. Retrying...")
            hamburger_menu = self.wait_for_element_to_be_clickable(self.locators.hamburger_menu)
            hamburger_menu.click()
        except Exception as e:
            allure.attach(f"An error occurred while clicking the hamburger menu: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def click_cameras_category(self):
        """Wait for the Cameras category to be clickable and click it,
           if ElementClickInterceptedException occurs, retry the click after pause."""
        try:
            cameras_category = self.wait_for_element_to_be_clickable(self.locators.cameras_category)
            cameras_category.click()
            return CategoryPage(self.driver)
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException: The Cameras category was not clickable. Retrying...")
            cameras_category = self.wait_for_element_to_be_clickable(self.locators.cameras_category)
            cameras_category.click()
            return CategoryPage(self.driver)
        except Exception as e:
            allure.attach(f"An error occurred while clicking the Cameras category: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise

    def click_cart(self):
        """Wait for the Cart menu to be clickable and click it,
           if ElementClickInterceptedException occurs, retry the click after pause."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators.cart_view)
            )
            self.click(*self.locators.cart_view)
            return CartSideMenuPage(self.driver)
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException: The Cart side menu was not clickable. Retrying...")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.cart_view)
            ).click()
            return CartSideMenuPage(self.driver)
        except TimeoutException as e:
            allure.attach(f"Timeout: Cart view button did not become clickable: {e}", name="Timeout",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except NoSuchElementException as e:
            allure.attach(f"No such element: Cart view button not found: {e}", name="Element not found",
                          attachment_type=allure.attachment_type.TEXT)
            raise
        except Exception as e:
            allure.attach(f"An error occurred while trying to click the cart button: {e}", name="Error",
                          attachment_type=allure.attachment_type.TEXT)
            raise
