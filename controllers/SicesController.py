from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from modules.SicesPlatform import SicesPlatform


def run(plants, keys):
    PLATFORM_INDEX = 0
    PLATFORM_PLANTS_INDICES = [index for index in range(len(plants.login_codes)) if plants.login_codes[index] == 1]
    INDIVIDUAL_PLANTS_INDICES = [index for index in range(len(plants.login_codes))
                                 if plants.login_codes[index] != 1 and plants.platform_names[index] == 'SICES']

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=SicesPlatform.SICES_OPTIONS)
    sices = SicesPlatform(driver)

    sices.do_login(keys.logins[PLATFORM_INDEX], keys.passwords[PLATFORM_INDEX])
