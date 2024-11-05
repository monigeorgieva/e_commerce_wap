from selenium.webdriver.common.by import By


# Cart Side Menu Locators
class CartSideMenuLocators:
    cart_product = (By.XPATH, "//*[@id='entry_217847']/div/table/tbody/tr/td[2]/a")
    cart_product_quantity = (By.XPATH, "//*[@id='entry_217847']/div/table/tbody/tr/td[3]")


# Shopping Cart Page Locators
class ShoppingCartPageLocators:
    product_name = (By.XPATH, "//*[@id='content']/form/div/table/tbody/tr/td[2]/a")
    quantity_input_field = (By.XPATH, "//*[@id='content']/form/div/table/tbody/tr/td[4]/div/input")
    update_quantity_button = (By.XPATH, "//*[@id='content']//button[@title='Update']")
    remove_items_button = (By.XPATH, "//*[@id='content']//button[@title='Remove']")
    updating_quantity_success_message = (By.XPATH, "//*[@id='checkout-cart']/div[1]")


# Empty Cart Page Locators
class EmptyCartPageLocators:
    empty_cart_message = (By.XPATH, "//*[@id='content']/p")
