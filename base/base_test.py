import pytest
from pages.home_page import HomePage
from config.configuration import Configuration


@pytest.mark.TestBase
@pytest.mark.critical
class TestBase:
    @pytest.fixture(autouse=True)
    def test_setup_home_page(self, browser):
        """Fixture to set up the browser with the home page loaded."""
        self.browser = browser
        self.config = Configuration()

        self.home_page = HomePage(browser)
        home_url = self.config.get_e_commerce_base_url()
        self.home_page.load()

        # Assert that the current URL matches the expected home URL
        assert browser.current_url == home_url, f"Unexpected URL: {browser.current_url}"
        # Assert that the main icon with the logo is displayed
        assert self.home_page.is_main_icon_displayed(), "Main icon is not displayed on the home page."
