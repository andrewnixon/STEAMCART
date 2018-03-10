from enum import Enum
import numpy as np

class _pType(Enum):
    RANGED = 1
    LISTED = 2

class Parameter(object):
    """Parameter from JSON for each model write

    Attributes:
        key - name of parameter being rewritten
        type - RANGED or LISTED parameter


    """
    def get_list(self, endpoint=True):
        if self.type == _pType.RANGED:
            return np.linspace(self.start, self.stop, num=self.num, endpoint=endpoint)
        elif self.type == _pType.LISTED:
            return self.list
        else:
            # not ideal.. should be a different exception
            self.__bad_json_exception()

    def ranged_parameter(self, dictionary):
        self.type = _pType.RANGED
        self.start = dictionary['start']
        self.stop = dictionary['stop']
        self.num = dictionary['num']

    def listed_parameter(self, dictionary):
        self.type = _pType.LISTED

    def __init__(self, key, dictionary):
        if not isinstance(dictionary, dict):
            self.__bad_json_exception()

        self.key = key
        if 'start' in dictionary and 'stop' in dictionary:
            self.ranged_parameter(dictionary)
        elif 'list' in dictionary:
            self.listed_parameter(dictionary)
        else:
            self.__bad_json_exception()

    def __bad_json_exception():
        raise Exception("Likely that the JSON is not correct")
