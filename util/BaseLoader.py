from csv import reader

""" Super class for importing the CSV files from the database """


class BaseLoader:

    """ BaseLoader super class for importing CSV files """
    def __init__(self, file_path) -> None:
        with open(file_path, newline='\n', encoding='utf-8-sig') as file:
            self._table = list(reader(file, delimiter=";"))

    """ Common methods for all children classes """

    def _get_column(self, column_number) -> list:
        return [element[column_number] for element in self._table]

    def _get_row(self, row_number) -> list:
        return self._table[row_number]
