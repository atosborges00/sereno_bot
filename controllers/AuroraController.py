from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config.ConfigAurora import ConfigAurora
from modules.AuroraPlatform import AuroraPlatform
from controllers import BaseController
from os.path import join


def run(plants, keys):

    PLANTS_INDICES = [index for index in range(len(plants.login_codes)) if plants.platform_names[index] == 'AURORA VISION']

    driver = webdriver.Chrome(ChromeDriverManager().install())
    aurora = AuroraPlatform(driver)

    aurora.do_login(keys.logins[plants.login_codes[PLANTS_INDICES[0]]-1],
                    keys.passwords[plants.login_codes[PLANTS_INDICES[0]]-1])

    aurora.select_month_data()
