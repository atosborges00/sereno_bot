from util.BaseLoader import BaseLoader

""" Class responsible for loading the Login data from the database """


class LoginsLoader(BaseLoader):

    """ Loading the Logins to the application's workspace and setting its properties """

    def __init__(self, file_path) -> None:
        super(LoginsLoader, self).__init__(file_path)
