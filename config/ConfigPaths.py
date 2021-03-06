from os import path

""" Storage class for the application's useful paths """


class ConfigPaths:
    
    """ Root path for the application """
    _ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
    
    """ Path for chrome webdriver """
    CHROME_PATH = path.join(_ROOT_DIR, "chromedriver.exe")

    """ Path for project folders """
    
    DATABASE_PATH = path.join(_ROOT_DIR, "database")

    UTIL_PATH = path.join(_ROOT_DIR, "util")
    MODULES_PATH = path.join(_ROOT_DIR, "modules")
    RAW_DATA_PATH = path.join(_ROOT_DIR, "raw_data")

    """ Path for database tables """

    PLANTS = path.join(DATABASE_PATH, "plants.csv")

    LOGINS = path.join(DATABASE_PATH, "logins.csv")
