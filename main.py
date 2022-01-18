from config.ConfigPaths import ConfigPaths
from util.LoginsLoader import LoginsLoader
from util.PlantsLoader import PlantsLoader
from controllers import SicesController, AuroraController

if __name__ == '__main__':
    """ Main function of the application """

    plants = PlantsLoader(ConfigPaths.PLANTS)
    keys = LoginsLoader(ConfigPaths.LOGINS)

    AuroraController.run(plants, keys, folder_name='dez', sleep_time=4)

    SicesController.run(plants, keys, 'Mês Passado', folder_name='dez', sleep_time=8)
