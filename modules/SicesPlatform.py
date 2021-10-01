from modules.BasePage import BasePage
from config.ConfigSices import ConfigSices
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

""" Class dedicated to interact with Sices Platform """


class SicesPlatform(BasePage):
    
    """ By locators for items in the page """
    _EMAIL_LOCATOR = (By.XPATH, "//input[@class='form-control']")
    _PASSWORD_LOCATOR = (By.XPATH, "//input[@class='form-control password']")
    _LOGIN_BUTTON_LOCATOR = (By.XPATH, "//button[@type['submit']]")
    _UNITS_BUTTON_LOCATOR = (By.XPATH, "//a[@id='linkUnidades']")
    _CALENDAR_BUTTON_LOCATOR = (By.XPATH, "//div[@id='calendario']")
    _DOWNLOAD_BUTTON_LOCATOR = (By.XPATH, "//button[@id='botao-download']")
    _DROP_MENU_LOCATOR = (By.XPATH, "//i[@class='fa fa-caret-down']")
    _LOGOUT_BUTTON_LOCATOR = (By.XPATH, "//a[@href='https://monitoramento.sicessolar.com.br/login/sair']")

    """ Platform options configuration """

    SICES_OPTIONS = Options()
    SICES_OPTIONS.add_experimental_option("prefs", ConfigSices.PREFERENCES)

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

    def get_analytics_from(self, selected_period):
        _PERIOD_BUTTON_LOCATOR = (By.XPATH, "//li[@data-range-key='{period}']".format(period=selected_period))

        self._open_calendar()
        period_button_clickable = self.is_clickable(_PERIOD_BUTTON_LOCATOR)

        if not period_button_clickable:
            raise RuntimeError("Unable to interact with the {period} button".format(period=selected_period))

        if period_button_clickable:
            self.do_click(_PERIOD_BUTTON_LOCATOR)

    def do_download(self) -> bool:
        download_button_clickable = self.is_clickable(self._DOWNLOAD_BUTTON_LOCATOR)

        if not download_button_clickable:
            return False

        if download_button_clickable:
            self.do_click(self._DOWNLOAD_BUTTON_LOCATOR)
            _ = self.is_clickable(self._DOWNLOAD_BUTTON_LOCATOR)
            return True

    def _open_drop_menu(self):
        drop_button_clickable = self.is_clickable(self._DROP_MENU_LOCATOR)

        if not drop_button_clickable:
            raise RuntimeError("Unable to interact with the Drop Menu button")

        if drop_button_clickable:
            self.do_click(self._DROP_MENU_LOCATOR)

    def do_logout(self):
        self._open_drop_menu()

        logout_button_clickable = self .is_clickable(self._LOGOUT_BUTTON_LOCATOR)

        if not logout_button_clickable:
            raise RuntimeError("Unable to interact with the Logout button")

        if logout_button_clickable:
            self.do_click(self._LOGOUT_BUTTON_LOCATOR)

    def check_download(self, plant_name) -> bool:
        _ = self.check_downloads_chrome()

        downloaded_files = self.get_files_in(ConfigSices.PREFERENCES['download.default_directory'])
        matches_found = [file for file in downloaded_files if plant_name in file]

        if matches_found:
            return True

        if not matches_found:
            return False
