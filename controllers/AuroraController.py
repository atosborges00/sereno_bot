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


def _download_checking(aurora_driver, downloaded, plants, current_plant, download_number, download_log, export_log):
    if not downloaded:
        download_log.append([plants.plants_names[current_plant], 'SEM DADOS'])

    if downloaded:
        downloaded += 1
        aurora_driver.check_download(str(download_number))
        download_log.append([plants.plants_names[current_plant], 'OK'])

        if export_log:
            BaseController.export_log_file(download_log, ConfigAurora.PREFERENCES['download.default_directory'])


def run(plants, keys, folder_name, sleep_time=2, export_log=True):
    download_log = []
    download_number = 0
    PLANTS_INDICES = range(plants.auroravision['starting_index'], plants.auroravision['ending_index']+1)

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=_set_download_path(folder_name))
    aurora = AuroraPlatform(driver)

    for current_plant in PLANTS_INDICES:

        try:
            aurora.do_login(keys.logins[plants.login_codes[current_plant]-1],
                            keys.passwords[plants.login_codes[current_plant]-1])
        except RuntimeError:
            aurora.return_to_login()
            continue

        aurora.select_month_data(sleep_time)

        aurora.select_previous(sleep_time)

        downloaded = aurora.do_download(sleep_time)
        _download_checking(aurora, downloaded, plants, current_plant, download_number, download_log, export_log)

        aurora.do_logout()
        aurora.return_to_login()
