from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.configuration import Configuration


class DriverManager:
    def __init__(self):
        self.driver = None

    def start_driver(self):
        chrome_options = webdriver.ChromeOptions()

        # Set up mobile emulation based on the specified device name
        device = Configuration().get_device_name()
        mobile_emulation = {"deviceName": device}

        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        chrome_options.add_argument("--no-default-browser-check")

        # Launch Chrome WebDriver with the configured options
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.maximize_window()
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
