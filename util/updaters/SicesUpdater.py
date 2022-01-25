from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config.ConfigSices import ConfigSices
from modules.SicesPlatform import SicesPlatform


def run():
    """ Class for updating the plants on the Sices Platform """

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=SicesPlatform.SICES_OPTIONS)
    sices = SicesPlatform(driver)

    sices.do_login(username=ConfigSices.DEFAULT_EMAIL, password=ConfigSices.DEFAULT_PASSWORD)

    names = []
    power = []

    for page in range(1, 5):
        sices.get_ufvs_page(page_number=page)
        names.append(sices.get_plants_names())
        power.append(sices.get_installed_power())

    plants_names = [plant for sublist in names for plant in sublist]
    installed_power = [plant_power for sublist in power for plant_power in sublist]

    plants_names = list(dict.fromkeys(plants_names))
    plants_names.remove('')
