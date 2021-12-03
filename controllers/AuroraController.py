from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config.ConfigAurora import ConfigAurora
from modules.AuroraPlatform import AuroraPlatform
from controllers import BaseController
from os.path import join


def _set_download_path(folder_name):
    ConfigAurora.PREFERENCES['download.default_directory'] = join(ConfigAurora.RAW_DATA_PATH, folder_name)

    AURORA_OPTIONS = Options()
    AURORA_OPTIONS.add_experimental_option("prefs", ConfigAurora.PREFERENCES)

    return AURORA_OPTIONS


def run(plants, keys, folder_name, sleep_time=2):

    PLANTS_INDICES = [index for index in range(len(plants.login_codes)) if plants.platform_names[index] == 'AURORA VISION']

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=_set_download_path(folder_name))
    aurora = AuroraPlatform(driver)

    aurora.do_login(keys.logins[plants.login_codes[PLANTS_INDICES[0]]-1],
                    keys.passwords[plants.login_codes[PLANTS_INDICES[0]]-1])

    aurora.select_month_data()
    aurora.select_previous(sleep_time)
    aurora.do_download(sleep_time)
