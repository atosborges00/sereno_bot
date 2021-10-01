from config.ConfigPaths import ConfigPaths
from util.LoginsLoader import LoginsLoader
from util.PlantsLoader import PlantsLoader
from controllers.SicesController import SicesController

if __name__ == '__main__':
    """ Main function of the application """

    plants = PlantsLoader(ConfigPaths.PLANTS)
    keys = LoginsLoader(ConfigPaths.LOGINS)

    sices_bot = SicesController(plants, keys)
