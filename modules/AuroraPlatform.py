from modules.BasePage import BasePage
from config.ConfigAurora import ConfigAurora
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

""" Class dedicated to interact with Aurora Platform """


class AuroraPlatform(BasePage):

    """ Class constructor extending BasePage """

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver.get(ConfigAurora.LOGIN_URL)
