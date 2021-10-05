from os import path
from config.ConfigPaths import ConfigPaths


class ConfigSices:
    
    """ Sices platform useful URLs """

    LOGIN_URL = 'https://monitoramento.sicessolar.com.br/login'
    ANALYTICS_PAGE = 'https://monitoramento.sicessolar.com.br/analytics?und={code}'

    """ Sices platform default directories """

    RAW_DATA_PATH = path.join(ConfigPaths.RAW_DATA_PATH, "sices")

    """ Sices platform options settings """

    PREFERENCES = {
        'download.default_directory': RAW_DATA_PATH,
        'safebrowsing.enabled': 'false'}
