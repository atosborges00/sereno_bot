from os import path
from config.ConfigPaths import ConfigPaths


class ConfigSices:
    
    """ Sices platform useful URLs and constants """

    LOGIN_URL = 'https://monitoramento.sicessolar.com.br/login'
    ANALYTICS_PAGE = 'https://monitoramento.sicessolar.com.br/analytics?und={code}'
    DEFAULT_EMAIL = 'projetos.energiacruze@outlook.com'
    DEFAULT_PASSWORD = 'cruze2113'

    """ Sices platform default directories """

    RAW_DATA_PATH = path.join(ConfigPaths.RAW_DATA_PATH, "sices")

    """ Sices platform options settings """

    PREFERENCES = {
        'download.default_directory': RAW_DATA_PATH,
        'safebrowsing.enabled': 'false'}
