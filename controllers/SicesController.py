from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from modules.SicesPlatform import SicesPlatform
from controllers import BaseController


def run(plants, keys, export_log=True):
    download_log = []
    PLATFORM_INDEX = 0
    PLATFORM_PLANTS_INDICES = [index for index in range(len(plants.login_codes)) if plants.login_codes[index] == 1]
    INDIVIDUAL_PLANTS_INDICES = [index for index in range(len(plants.login_codes))
                                 if plants.login_codes[index] != 1 and plants.platform_names[index] == 'SICES']

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=SicesPlatform.SICES_OPTIONS)
    sices = SicesPlatform(driver)

    sices.do_login(keys.logins[PLATFORM_INDEX], keys.passwords[PLATFORM_INDEX])

    for plant in PLATFORM_PLANTS_INDICES:

        sices.get_analytics_page(plants.codes[plant])
        sices.get_analytics_from('Mês Passado')

        downloaded = sices.do_download()

        if downloaded:
            checked = sices.check_download(plants.plants_names[plant])

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
