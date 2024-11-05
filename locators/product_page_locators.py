from selenium.webdriver.common.by import By


class ProductPageLocators:
    add_to_cart_button = (By.XPATH, "//*[@id='entry_216868']/button")
    popup_close_button = (By.XPATH, "//*[@id='notification-box-top']/div[1]/div[1]/button/span")
    popup_view_cart_button = (By.XPATH, "// *[ @ id = 'notification-box-top'] / div / div[2] / div[2] / div[1] / a")