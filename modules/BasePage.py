from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from os.path import isfile, join
from os import listdir

""" This class is the parent class for all page classes. It contains all common methods an utilities for all pages """


class BasePage:

    """ Superclass constructor  """
    def __init__(self, driver) -> None:
        self.driver = driver

    """ Common methods for all Pages """

    def do_click(self, by_locator) -> None:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, content) -> None:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(content)

    def get_element_text(self, by_locator) -> str:
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return element.text
        except TimeoutException:
            return 'Text not found'

    def is_present(self, by_locator) -> bool:
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            return bool(element)
        except TimeoutException:
            return False

    def is_visible(self, by_locator) -> bool:
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except TimeoutException:
            return False

    def is_clickable(self, by_locator) -> bool:
        try:
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator))
            return bool(element)
        except TimeoutException:
            return False

    @staticmethod
    def get_files_in(directory_path) -> list:
        return [file for file in listdir(directory_path) if isfile(join(directory_path, file))]
