from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from modules.SicesPlatform import SicesPlatform


class SicesController:

    def __init__(self, plants, keys):

        self.LOGINS = keys.logins[plants.sices['starting_index']:plants.sices['ending_index']]
        self.PASSWORDS = keys.passwords[plants.sices['starting_index']:plants.sices['ending_index']]
        self.CODES = plants.codes[plants.sices['starting_index']:plants.sices['ending_index']]

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=SicesPlatform.SICES_OPTIONS)
        sices = SicesPlatform(driver)
