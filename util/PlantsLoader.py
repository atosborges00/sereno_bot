from util.BaseLoader import BaseLoader

""" Class responsible for loading the Plants' data to the workspace """


class PlantsLoader(BaseLoader):

    """ Loading the Plants' data as a table to the workspace and setting the properties """

    def __init__(self, file_path) -> None:
        super().__init__(file_path)

        # mapping the columns-names to a dictionary
        self._COLUMN_MAP = {column: self._table[0].index(column) for column in self._table[0]}
        # deleting the columns-names row from the table
        del self._table[0]

    """ Properties for the Plants object """

    @property
    def id(self) -> list:
        return self._get_column(self._COLUMN_MAP['id'])

    @property
    def platform(self) -> list:
        return self._get_column(self._COLUMN_MAP['platform'])

    @property
    def plant_name(self) -> list:
        return self._get_column(self._COLUMN_MAP['plant_name'])

    @property
    def installed_power(self) -> list:
        return self._get_column(self._COLUMN_MAP['installed_power'])

    @property
    def code(self) -> list:
        return self._get_column(self._COLUMN_MAP['code'])

    @property
    def login_info(self) -> list:
        return self._get_column(self._COLUMN_MAP['login_info'])

    @property
    def client_id(self) -> list:
        return self._get_column(self._COLUMN_MAP['client_id'])
