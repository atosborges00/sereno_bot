from config.ConfigPaths import ConfigPaths
from util.loaders.LoginsLoader import LoginsLoader
from util.loaders.PlantsLoader import PlantsLoader
from util.updaters import SicesUpdater
from controllers import SicesController, AuroraController

if __name__ == '__main__':
    """ Main function of the application """

    SicesUpdater.run()

    plants = PlantsLoader(ConfigPaths.PLANTS)
    keys = LoginsLoader(ConfigPaths.LOGINS)

    current_month = 'jan'

    AuroraController.run(plants, keys, folder_name=current_month, sleep_time=4)

    SicesController.run(plants, keys, 'Mês Passado', folder_name=current_month, sleep_time=8)
