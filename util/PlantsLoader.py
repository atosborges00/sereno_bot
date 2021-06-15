from util.BaseLoader import BaseLoader

""" Class responsible for loading the Plants' data to the workspace """


class PlantsLoader(BaseLoader):

    """ Loading the Plants' data as a table to the workspace and setting the properties """

    def __init__(self, file_path) -> None:
        super().__init__(file_path)

        self._COLUMN_MAP = {column: self._table[0].index(column) for column in self._table[0]}
        del self._table[0]

        self.sices = self._set_platform_index('SICES')
        self.auroravision = self._set_platform_index('AURORA VISION')
        self.isolarcloud = self._set_platform_index('ISOLARCLOUD')

    """ Properties for the Plants object """

    @property
    def id(self) -> list:
        return self._get_column(self._COLUMN_MAP['id'])

    @property
    def platform_names(self) -> list:
        return self._get_column(self._COLUMN_MAP['platform_names'])

    @property
    def plants_names(self) -> list:
        return self._get_column(self._COLUMN_MAP['plants_names'])

    @property
    def installed_powers(self) -> list:
        return self._get_column(self._COLUMN_MAP['installed_powers'])

    @property
    def codes(self) -> list:
        return self._get_column(self._COLUMN_MAP['codes'])

    @property
    def login_codes(self) -> list:
        return self._get_column(self._COLUMN_MAP['login_codes'])

    @property
    def clients_ids(self) -> list:
        return self._get_column(self._COLUMN_MAP['clients_ids'])

    """ Methods for important queries """

    def _set_platform_index(self, name) -> dict:
        """ Returns the starting index and ending index on the table of a given platform """

        _platform_indices = [index for index in range(len(self.platform_names)) if self.platform_names[index] == name]
        return {'starting_index': _platform_indices[0], 'ending_index': _platform_indices[-1]}

    def head(self, row_range=5):
        """ Returns the first n rows of the plants table """

        return [self._get_row(row_number) for row_number in range(row_range)]
