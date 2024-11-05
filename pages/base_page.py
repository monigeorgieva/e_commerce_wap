from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Common methods to all page objects"""

    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.find(*locator).click()

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        # Waits for an element to be clickable
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
