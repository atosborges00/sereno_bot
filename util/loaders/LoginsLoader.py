from util.loaders.BaseLoader import BaseLoader

""" Class responsible for loading the Login data from the database """


class LoginsLoader(BaseLoader):

    """ Loading the Logins to the application's workspace and setting its properties """

    def __init__(self, file_path) -> None:
        super().__init__(file_path)

        self._COLUMN_MAP = {column: self._table[0].index(column) for column in self._table[0]}

    """ Properties for the Logins object """

    @property
    def logins(self) -> list:
        return self._get_column(self._COLUMN_MAP['logins'])

    @property
    def passwords(self) -> list:
        return self._get_column(self._COLUMN_MAP['passwords'])
