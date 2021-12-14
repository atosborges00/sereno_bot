from modules.BasePage import BasePage
from config.ConfigAurora import ConfigAurora
from selenium.webdriver.common.by import By
from time import sleep

""" Class dedicated to interact with Aurora Platform """


class AuroraPlatform(BasePage):

    """ By locators for items in the page """
    _EMAIL_LOCATOR = (By.XPATH, "//input[@id='userId']")
    _PASSWORD_LOCATOR = (By.XPATH, "//input[@id='password']")
    _LOGIN_BUTTON_LOCATOR = (By.XPATH, "//button[@name='login-btn']")
    _DATES_NAV_LOCATOR = (By.XPATH, "//div[@class='nav']")
    _MTD_BUTTON_LOCATOR = (By.XPATH, "//li[@duration='MTD']")
    _PREVIOUS_BUTTON_LOCATOR = (By.XPATH, "//a[@class='prev']")
    _NO_DATA_MESSAGE_LOCATOR = (By.XPATH, "//div[@class='alert alert-info noChartData hideOnLoad']")
    _DOWNLOAD_BUTTON_LOCATOR = (By.XPATH, "//a[@class='btn btn-secondary download']")
    _MENU_BUTTON_LOCATOR = (By.XPATH, '//a[@id="user_menu"]')
    _LOGOUT_BUTTON_LOCATOR = (By.XPATH, '//a[@id="logout"]')

    """ Class constructor extending BasePage """

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver.get(ConfigAurora.LOGIN_URL)

    def do_login(self, username, password, sleep_time=5):
        self.do_send_keys(self._EMAIL_LOCATOR, username)
        self.do_send_keys(self._PASSWORD_LOCATOR, password)
        self.do_click(self._LOGIN_BUTTON_LOCATOR)
        period_nav_located = self.is_present(self._DATES_NAV_LOCATOR)

        if not period_nav_located:
            sleep(sleep_time)
            if not self.is_present(self._DATES_NAV_LOCATOR):
                return False

        if period_nav_located:
            return True

    def select_month_data(self, sleep_time):
        month_button_clickable = self.is_clickable(self._DATES_NAV_LOCATOR)

        if not month_button_clickable:
            raise RuntimeError("Unable to interact with the MTD button")

        if month_button_clickable:
            self.do_click(self._MTD_BUTTON_LOCATOR)
            sleep(sleep_time)

    def select_previous(self, sleep_time):
        previous_button_clickable = self.is_clickable(self._PREVIOUS_BUTTON_LOCATOR)

        if not previous_button_clickable:
            raise RuntimeError("Unable to interact with the Previous button")

        if previous_button_clickable:
            self.do_click(self._PREVIOUS_BUTTON_LOCATOR)
            sleep(sleep_time)

    def do_download(self, sleep_time):
        download_button_clickable = self.is_clickable(self._DOWNLOAD_BUTTON_LOCATOR)

        if not download_button_clickable:
            no_data_message_visible = self.is_visible(self._NO_DATA_MESSAGE_LOCATOR)

            if not no_data_message_visible:
                raise RuntimeError("Unable to interact with the Download button")
            if no_data_message_visible:
                return False

        if download_button_clickable:
            self.do_click(self._DOWNLOAD_BUTTON_LOCATOR)
            sleep(sleep_time)
            return True

    def do_logout(self):
        self.open_drop_menu(self._MENU_BUTTON_LOCATOR)

        logout_button_clickable = self .is_clickable(self._LOGOUT_BUTTON_LOCATOR)

        if not logout_button_clickable:
            raise RuntimeError("Unable to interact with the Logout button")

        if logout_button_clickable:
            self.do_click(self._LOGOUT_BUTTON_LOCATOR)

    def check_download(self, download_number) -> bool:

        downloaded_files = self.get_files_in(ConfigAurora.PREFERENCES['download.default_directory'])
        matches_found = [file for file in downloaded_files if download_number in file]

        if matches_found:
            return True

        if not matches_found:
            return False

    def return_to_login(self):
        self.driver.get(ConfigAurora.LOGIN_URL)
