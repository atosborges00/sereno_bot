from os.path import join
from BaseReport import BaseReport
from config.ConfigSices import ConfigSices
from config.ConfigPaths import ConfigPaths


class SicesReport(BaseReport):

    """Class to define the behaviour of the Sices Report Builder"""

    def __init__(self, plants_list):
        super().__init__(ConfigSices.RAW_DATA_PATH, ConfigPaths.REPORTS_DATA_PATH, plants_list)

    """Importation functions"""

    @staticmethod
    def _get_total_generation(inverter_data):
        first_register = float(inverter_data['Energia CA (kWh)'].iloc[0].replace(',', '.'))
        final_register = float(inverter_data['Energia CA (kWh)'].iloc[-1].replace(',', '.'))

        return final_register - first_register

    def double_inverter_reading(self, plant, dates):
        plant_file = join(self.raw_data_folder, plant, dates)
        first_inverter_data = self.read_plant_file(plant_file, 0)
        second_inverter_data = self.read_plant_file(plant_file, 1)

        generation_first_inverter = self._get_total_generation(first_inverter_data)
        generation_second_inverter = self._get_total_generation(second_inverter_data)

        return generation_first_inverter + generation_second_inverter

    def single_inverter_reading(self, plant, dates):
        plant_file = join(self.raw_data_folder, plant, dates)
        inverter_data = self.read_plant_file(plant_file)
        return self._get_total_generation(inverter_data)
