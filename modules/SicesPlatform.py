from modules.BasePage import BasePage
from config.ConfigSices import ConfigSices
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

""" Class dedicated to interact with Sices Platform """


class SicesPlatform(BasePage):
    
    """ By locators for items in the page """
    _EMAIL_LOCATOR = (By.XPATH, "//input[@class='form-control']")
    _PASSWORD_LOCATOR = (By.XPATH, "//input[@class='form-control password']")
    _LOGIN_BUTTON_LOCATOR = (By.XPATH, "//button[@type['submit']]")
    _UNITS_BUTTON_LOCATOR = (By.XPATH, "//a[@id='linkUnidades']")
    _CALENDAR_BUTTON_LOCATOR = (By.XPATH, "//div[@id='calendario']")
    _DOWNLOAD_BUTTON_LOCATOR = (By.XPATH, "//button[@id='botao-download']")
    _MESSAGE_LOCATOR = (By.XPATH, "//span[@id='mensagem-info-text']")
    _DROP_MENU_LOCATOR = (By.XPATH, "//i[@class='fa fa-caret-down']")
    _LOGOUT_BUTTON_LOCATOR = (By.XPATH, "//a[@href='https://monitoramento.sicessolar.com.br/login/sair']")
    _TABLE_LOCATOR = (By.XPATH, "//tbody")
    _PLANTS_NAMES_LOCATOR = (By.XPATH, "//a[@class='btn btn-xs']")
    _INSTALLED_POWER_LOCATOR = (By.XPATH, "//td[@id='unidadePotencia']")

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

    def get_ufvs_page(self, page_number):
        self.driver.get(ConfigSices.UFVS_PAGE.format(page=page_number))
        table_body_located = self.is_present(self._TABLE_LOCATOR)

        if not table_body_located:
            raise RuntimeError("Unable to open the UFVS page on the platform")

    def get_installed_power(self):
        installed_power_list = self.get_list_of_elements(self._INSTALLED_POWER_LOCATOR)

        return [power.text.replace(',', '.') for power in installed_power_list]

    def get_plants_names(self):
        plants_list = self.get_list_of_elements(self._PLANTS_NAMES_LOCATOR)

        return [plant.text for plant in plants_list]

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
            sleep(5)
            period_button_clickable = self.is_clickable(_PERIOD_BUTTON_LOCATOR)

        if period_button_clickable:
            self.do_click(_PERIOD_BUTTON_LOCATOR)

    def _check_message(self):
        message = self.get_element_text(self._MESSAGE_LOCATOR).split(' ')[0]

        if message == 'Sucesso':
            return True

        if message != 'Sucesso':
            return False

    def do_download(self, sleep_time=6) -> bool:
        download_button_clickable = self.is_clickable(self._DOWNLOAD_BUTTON_LOCATOR)

        if not download_button_clickable:
            return False

        if download_button_clickable:
            self.do_click(self._DOWNLOAD_BUTTON_LOCATOR)
            _ = self.is_clickable(self._DOWNLOAD_BUTTON_LOCATOR)

            success = self._check_message()

            if success:
                sleep(sleep_time)
                return True

            if not success:
                sleep(sleep_time)
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

        downloaded_files = self.get_files_in(ConfigSices.PREFERENCES['download.default_directory'])
        matches_found = [file for file in downloaded_files if plant_name in file]

        if matches_found:
            return True

        if not matches_found:
            return False
