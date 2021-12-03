from modules.BasePage import BasePage
from config.ConfigAurora import ConfigAurora
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

""" Class dedicated to interact with Aurora Platform """


class AuroraPlatform(BasePage):

    """ By locators for items in the page """
    _EMAIL_LOCATOR = (By.XPATH, "//input[@id='userId']")
    _PASSWORD_LOCATOR = (By.XPATH, "//input[@id='password']")
    _LOGIN_BUTTON_LOCATOR = (By.XPATH, "//button[@name='login-btn']")
    _DATES_NAV_LOCATOR = (By.XPATH, "//div[@class='nav']")

    """ Class constructor extending BasePage """

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver.get(ConfigAurora.LOGIN_URL)

    def do_login(self, username, password):
        self.do_send_keys(self._EMAIL_LOCATOR, username)
        self.do_send_keys(self._PASSWORD_LOCATOR, password)
        self.do_click(self._LOGIN_BUTTON_LOCATOR)
        units_button_located = self.is_present(self._DATES_NAV_LOCATOR)

        if not units_button_located:
            raise RuntimeError("Unable to login")
