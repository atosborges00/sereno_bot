from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from config.ConfigSices import ConfigSices
from modules.SicesPlatform import SicesPlatform
from controllers import BaseController
from os.path import join


""" Functions to operate the SicesController """


def _get_analytics(sices_driver, plants, current_plant, time_period):
    sices_driver.get_analytics_page(plants.codes[current_plant])
    sices_driver.get_analytics_from(time_period)


def _download_checking(sices_driver, downloaded, plants, plant, download_log, export_log):
    if downloaded:
        checked = sices_driver.check_download(plants.plants_names[plant])

        if checked:
            download_log.append([plants.plants_names[plant], 'OK'])
            print("{plant_name} download confirmed".format(plant_name=plants.plants_names[plant]))

            if export_log:
                BaseController.export_log_file(download_log)

    if not downloaded:
        download_log.append([plants.plants_names[plant], 'SEM DADOS'])
        print("Unable to download {plant_name} data".format(plant_name=plants.plants_names[plant]))

        if export_log:
            BaseController.export_log_file(download_log)


def _final_checking(sices_driver, plants, export_log):
    download_log = []

    for plant in plants.plants_names[plants.sices['starting_index']:plants.sices['ending_index']]:
        checked = sices_driver.check_download(plant)

        if checked:
            download_log.append([plant, 'OK'])

        if not checked:
            download_log.append([plant, 'SEM DADOS'])

    if export_log:
        BaseController.export_log_file(download_log)


def _set_download_path(folder_name):
    ConfigSices.PREFERENCES['download.default_directory'] = join(ConfigSices.RAW_DATA_PATH, folder_name)

    SICES_OPTIONS = Options()
    SICES_OPTIONS.add_experimental_option("prefs", ConfigSices.PREFERENCES)


""" Functions to run all the operations on the SicesPage in the correct order """


def run(plants, keys, time_period, folder_name, exporting_option=True):
    download_log = []
    PLATFORM_INDEX = 0
    PLATFORM_PLANTS_INDICES = [index for index in range(len(plants.login_codes)) if plants.login_codes[index] == 1]
    INDIVIDUAL_PLANTS_INDICES = [index for index in range(len(plants.login_codes))
                                 if plants.login_codes[index] != 1 and plants.platform_names[index] == 'SICES']

    _set_download_path(folder_name)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=SicesPlatform.SICES_OPTIONS)
    sices = SicesPlatform(driver)

    sices.do_login(keys.logins[PLATFORM_INDEX],
                   keys.passwords[PLATFORM_INDEX])

    for current_plant in PLATFORM_PLANTS_INDICES:

        _get_analytics(sices, plants, current_plant, time_period)

        downloaded = sices.do_download(sleep_time=6)

        _download_checking(sices, downloaded, plants, current_plant, download_log, exporting_option)

    sices.do_logout()

    for current_plant in INDIVIDUAL_PLANTS_INDICES:
        sices.do_login(keys.logins[plants.login_codes[current_plant]-1],
                       keys.passwords[plants.login_codes[current_plant]-1])

        _get_analytics(sices, plants, current_plant, time_period)

        downloaded = sices.do_download(sleep_time=6)

        _download_checking(sices, downloaded, plants, current_plant, download_log, exporting_option)

        sices.do_logout()

    _final_checking(sices, plants, exporting_option)
