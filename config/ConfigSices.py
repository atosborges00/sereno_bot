from os import path
from config.ConfigPaths import ConfigPaths


class ConfigSices:
    
    """ Sices platform useful URLs and constants """

    BASE_URL = 'https://monitoramento.sicessolar.com.br'

    LOGIN_URL = BASE_URL + '/login'
    ANALYTICS_PAGE = BASE_URL + '/analytics?und={code}'
    UFVS_PAGE = BASE_URL + '/ufvs?&p={page}'

    DEFAULT_EMAIL = 'projetos.energiacruze@outlook.com'
    DEFAULT_PASSWORD = 'cruze2113'

    """ Sices platform default directories """

    RAW_DATA_PATH = path.join(ConfigPaths.RAW_DATA_PATH, "sices")

    """ Sices platform options settings """

    PREFERENCES = {
        'download.default_directory': RAW_DATA_PATH,
        'safebrowsing.enabled': 'false'}
