from config.ConfigPaths import ConfigPaths
from util.LoginsLoader import LoginsLoader
from util.PlantsLoader import PlantsLoader
from controllers import SicesController

if __name__ == '__main__':
    """ Main function of the application """

    plants = PlantsLoader(ConfigPaths.PLANTS)
    keys = LoginsLoader(ConfigPaths.LOGINS)

    SicesController.run(plants, keys, 'Mês Passado', folder_name='nov', sleep_time=8)
