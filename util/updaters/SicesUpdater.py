from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config.ConfigSices import ConfigSices
from modules.SicesPlatform import SicesPlatform
import csv


def _clean_list(list_to_clean):
    cleaner = list(dict.fromkeys(list_to_clean))
    cleaner.remove('')

    return cleaner


def run():
    """ Funcion for updating the plants on the Sices Platform """

    _DATABASE_FILE_PATH = ConfigSices.DATABASE_PATH + "/sices_plants.csv"

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=SicesPlatform.SICES_OPTIONS)
    sices = SicesPlatform(driver)

    sices.do_login(username=ConfigSices.DEFAULT_EMAIL, password=ConfigSices.DEFAULT_PASSWORD)

    names = []
    codes = []
    power = []

    for page in range(1, 5):
        sices.get_ufvs_page(page_number=page)
        plants = sices.get_plants_info()

        names.append(plants['names'])
        codes.append(plants['codes'])
        power.append(sices.get_installed_power())

    plants_names = [plant_name for sublist in names for plant_name in sublist]
    plants_codes = [plant_code for sublist in codes for plant_code in sublist]
    plants_power = [plant_power for sublist in power for plant_power in sublist]

    plants_names = _clean_list(plants_names)
    plants_codes = _clean_list(plants_codes)
    plants_codes.remove('https://monitoramento.sicessolar.com.br/boxes')

    sices_logins = []

    with open(_DATABASE_FILE_PATH, 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=';')
        saved_plants = [plant[0] for plant in file_reader]

    for plant in plants_names:
        if plant not in saved_plants:
            print("New plant on the platform: {new_plant}".format(new_plant=plant))
            raise RuntimeError

    print("The plant list is up to date")
