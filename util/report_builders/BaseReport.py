from os.path import join
from pandas import read_excel, ExcelWriter, DataFrame


class BaseReport:
    """Class to define basic report behaviour and properties"""

    def __init__(self, raw_data_folder, export_folder, plants_list):
        self.raw_data_folder = raw_data_folder
        self.export_folder = export_folder
        self.df_report = DataFrame(data=plants_list)

    """Reading and exporting files"""

    def read_plant_file(self, file_name, sheet_number=0):
        data_file = join(self.raw_data_folder, file_name)
        return read_excel(data_file, sheet_number)

    def save_report(self, report_name):
        report_file = join(self.export_folder, report_name)
        report_writer = ExcelWriter(report_file, engine='xlsxwriter')
        self.df_report.to_excel(writer=report_writer, index=True)

    """Adder functions"""

    def add_plants_generation(self, power_generation_list):
        self.df_report['generation'] = power_generation_list

    def add_plants_status(self, status_list):
        self.df_report['status'] = status_list

    def add_expected_generation(self, expected_generation_list):
        self.df_report['expected_generation'] = expected_generation_list

    def add_performance(self, performance_list):
        self.df_report['performance'] = performance_list
