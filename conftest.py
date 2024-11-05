import allure
import pytest
from config.driver_manager import DriverManager


@allure.step("Browser setup and teardown")
@pytest.fixture(scope="function")
def browser():
    # Create an instance of DriverManager to manage the WebDriver
    driver_manager = DriverManager()
    driver = driver_manager.start_driver()
    yield driver
    driver_manager.quit_driver()


@pytest.fixture
def add_product_to_cart_fixture(request):
    """ Fixture for steps that are reused in 3 test:
        clicking on the hamburger menu,
        clicking on the 'Cameras' category,
        open a product from the category and
        click on the 'Add to cart' page. """
    request.instance.home_page.click_hamburger_menu()
    category_page = request.instance.home_page.click_cameras_category()
    product_page = category_page.click_on_product()
    product_page.click_add_to_cart()

    yield product_page
