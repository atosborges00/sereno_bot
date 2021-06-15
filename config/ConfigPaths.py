from os import path

""" Storage class for the application's useful paths """


class ConfigPaths:
    
    """ Root path for the application """
    _ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
    
    """ Path for chrome webdriver """
    CHROME_PATH = path.join(_ROOT_DIR, "chromedriver.exe")

    """ Path for project folders """
    
    _DATABASE_PATH = path.join(_ROOT_DIR, "database")

    UTIL_PATH = path.join(_ROOT_DIR, "util")

    """ Path for database tables """

    PLANTS = path.join(_DATABASE_PATH, "plants.csv")

    LOGINS = path.join(_DATABASE_PATH, "logins.csv")
