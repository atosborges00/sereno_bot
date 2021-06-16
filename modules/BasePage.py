from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_present(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        return bool(element)

    def is_visible(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_clickable(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)
