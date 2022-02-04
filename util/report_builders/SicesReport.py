from BaseReport import BaseReport


class SicesReport(BaseReport):

    """Class to define the behaviour of the Sices Report Builder"""
    
    def __init__(self, raw_data_folder, export_folder, plants_list):
        super().__init__(raw_data_folder, export_folder, plants_list)
