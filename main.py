from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config.ConfigPaths import ConfigPaths
from util.LoginsLoader import LoginsLoader
from util.PlantsLoader import PlantsLoader
from modules.SicesPlatform import SicesPlatform

if __name__ == '__main__':
    """ Main function of the application """

    plants = PlantsLoader(ConfigPaths.PLANTS)
    keys = LoginsLoader(ConfigPaths.LOGINS)

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=SicesPlatform.SICES_OPTIONS)

    sices = SicesPlatform(driver)
    plataforma = plants.platform_names.index('SICES')

    sices.do_login(keys.logins[plataforma], keys.passwords[plataforma])

    sices.get_analytics_page(plants.codes[0])

    sices.get_analytics_from('Últimos 7 Dias')

    sices.do_download()

    download_success = sices.check_download(plants.plants_names[0])

    sices.get_analytics_page(plants.codes[0])

    sices.do_logout()
