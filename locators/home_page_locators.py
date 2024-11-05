from selenium.webdriver.common.by import By


class HomePageLocators:
    hamburger_menu = (By.XPATH, "//*[@id='entry_217827']/a")
    cameras_category = (By.XPATH, "//*[@id='widget-navbar-217841']/ul/li[2]/a")
    my_account_menu = (By.XPATH, "//*[@id='entry_217829']/a")
    cart_view = (By.XPATH, "//*[@id='entry_217830']/a")
    search_bar_input = (By.XPATH, "//input[@name='search' and not(@data-autocomplete)]")
    search_button = (By.XPATH, "//*[@id='search']/div[2]/button/i")
    cart = (By.XPATH, "//*[@id='cart-total-drawer']/h5")
    main_icon = (By.CSS_SELECTOR, "img[alt='Poco Theme']")