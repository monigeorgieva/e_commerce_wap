import allure
import pytest

from base.base_test import TestBase


@pytest.mark.TestSearch
@allure.title("Test search a product")
@allure.description("Test for searching a product")
@pytest.mark.normal
class TestSearch(TestBase):
    """Search for example text in the search bar and click on the search button"""

    @allure.step("Fill in the input with 'Iphone' word"
                 "Click on the search button")
    def test_search_functionality(self):
        search_text = "Iphone"
        self.home_page.enter_search_text(search_text)
        self.home_page.click_search_button()

        # Getting the current page title and check if the search text is in the title
        title = self.home_page.driver.title
        assert search_text in title
