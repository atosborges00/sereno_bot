from os import path
from config.ConfigPaths import ConfigPaths


class ConfigAurora:
    
    """ Aurora login page URL """
    LOGIN_URL = "https://www.auroravision.net/ums/v1/loginPage?redirectUrl=http:%2F%2Fwww.auroravision.net%2Fdash%2Fhome.jsf&cause=MISSING_TOKEN"

    """ Aurora platform default directories """

    RAW_DATA_PATH = path.join(ConfigPaths.RAW_DATA_PATH, "aurora")

    """ Aurora platform options settings """

    PREFERENCES = {
        'download.default_directory': RAW_DATA_PATH,
        'safebrowsing.enabled': 'false'}
