from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config.ConfigSices import ConfigSices
from modules.SicesPlatform import SicesPlatform


def run():
    """ Class for updating the plants on the Sices Platform """

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=SicesPlatform.SICES_OPTIONS)
    sices = SicesPlatform(driver)

    sices.do_login(username=ConfigSices.DEFAULT_EMAIL, password=ConfigSices.DEFAULT_PASSWORD)
    sices.get_ufvs_page()
