from os import path
import pandas as pd


class BaseReport:
    """Class to define basic report behaviour and properties"""

    def __init__(self, raw_data_folder):
        self.raw_data_folder = raw_data_folder
