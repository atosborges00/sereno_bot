from util.BaseLoader import BaseLoader

""" Class responsible for loading the Plants' data to the workspace """


class PlantsLoader(BaseLoader):

    """ Loading the Plants' data as a table to the workspace """

    def __init__(self, file_path) -> None:
        super().__init__(file_path)
