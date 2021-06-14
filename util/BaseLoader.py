from csv import reader

""" Super class for importing the CSV files from the database """


class BaseLoader:

    """ BaseLoader super class for importing CSV files """
    def __init__(self, file_path):
        with open(file_path, newline='\n', encoding='utf-8-sig') as file:
            self.table = list(reader(file, delimiter=";"))

    """ Common methods for all children classes """

    def get_column(self, column_number):
        return [element[column_number] for element in self.table]

    def get_row(self, row_number):
        return self.table[row_number]
