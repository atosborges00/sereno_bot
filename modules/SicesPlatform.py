from modules.BasePage import BasePage
from config.ConfigSices import ConfigSices
from selenium.webdriver.common.by import By

""" Class dedicated to interact with Sices Platform """


class SicesPlatform(BasePage):
    
    """ By locators for items in the page """
    _EMAIL_LOCATOR = (By.XPATH, "//input[@class='form-control']")
    _PASSWORD_LOCATOR = (By.XPATH, "//input[@class='form-control password']")
    _LOGIN_BUTTON_LOCATOR = (By.XPATH, "//button[@type['submit']]")
    _UNITS_BUTTON_LOCATOR = (By.XPATH, "//a[@id='linkUnidades']")

    """ Class constructor extending BasePage """

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver.get(ConfigSices.LOGIN_URL)

    """ Page Actions """
    
    def do_login(self, username, password):
        self.do_send_keys(self._EMAIL_LOCATOR, username)
        self.do_send_keys(self._PASSWORD_LOCATOR, password)
        self.do_click(self._LOGIN_BUTTON_LOCATOR)
        units_button_located = self.is_present(self._UNITS_BUTTON_LOCATOR)

        if not units_button_located:
            raise RuntimeError("Incapable of doing login")

    def get_analytics_page(self, plant_code):
        self.driver.get(ConfigSices.ANALYTICS_PAGE.format(code=plant_code))
