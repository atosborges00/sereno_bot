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
    _CALENDAR_BUTTON_LOCATOR = (By.XPATH, "//div[@id='calendario']")
    _YESTERDAY_BUTTON_LOCATOR = (By.XPATH, "//li[@data-range-key='Ontem']")
    _WEEK_BUTTON_LOCATOR = (By.XPATH, "//li[@data-range-key='Últimos 7 Dias']")

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
            raise RuntimeError("Unable to login")

    def get_analytics_page(self, plant_code):
        self.driver.get(ConfigSices.ANALYTICS_PAGE.format(code=plant_code))
        calendar_button_located = self.is_present(self._CALENDAR_BUTTON_LOCATOR)

        if not calendar_button_located:
            raise RuntimeError("Unable to open the Analytics page on the platform")

    def _open_calendar(self):
        calendar_button_clickable = self.is_clickable(self._CALENDAR_BUTTON_LOCATOR)

        if not calendar_button_clickable:
            raise RuntimeError("Unable to interact with the calendar button")

        if calendar_button_clickable:
            self.do_click(self._CALENDAR_BUTTON_LOCATOR)

    def get_yesterday_analytics(self):
        self._open_calendar()
        yesterday_button_clickable = self.is_clickable(self._YESTERDAY_BUTTON_LOCATOR)

        if not yesterday_button_clickable:
            raise RuntimeError("Unable to interact with the 'Ontem' button")

        if yesterday_button_clickable:
            self.do_click(self._YESTERDAY_BUTTON_LOCATOR)

    def get_week_analytics(self):
        self._open_calendar()
        week_button_clickable = self.is_clickable(self._WEEK_BUTTON_LOCATOR)

        if not week_button_clickable:
            raise RuntimeError("Unable to interact with the 'Últimos 7 dias' button")

        if week_button_clickable:
            self.do_click(self._WEEK_BUTTON_LOCATOR)
