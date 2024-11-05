import allure
import pytest
from base.base_test import TestBase


@pytest.mark.TestSelectCategory
@allure.title("Test select category 'Cameras'")
@allure.description("Test for selecting 'Cameras' category")
@pytest.mark.normal
class TestSelectCategory(TestBase):
    """Click on the hamburger menu, select 'Cameras' category"""

    @allure.step("Click on the hamburger menu."
                 "Select 'Cameras' category."
                 )
    @allure.description("Test for selecting 'Cameras' category")
    def test_select_category(self):
        self.home_page.click_hamburger_menu()
        category_name = "Cameras"
        self.home_page.click_cameras_category()

        title = self.home_page.driver.title

        # Assert that the category name is in the title
        assert category_name in title
