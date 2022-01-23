from loggingFolder.FileLogging import FileLogger
from list.ListOperations import ListOperation
from set.SetOperations import SetOperation
from tuple.TupleOperations import TupleOperation
from dictnary.DictOperations import DictOperation


class AllOperations:
    def __init__(self, list, set, dict, tuple):
        """
            Pass list, set , dictnary and tuple
        :type tuple: object
        """
        self.list = list
        self.set = set
        self.dict = dict
        self.tuple = tuple
        self.logger = FileLogger()
        self.logger.info("Logging Started")

    def submit_list(self):
        '''
        submit only list to listOperations file
        :return:
        '''
        try:
            self.logger.info("List submitted to the listOperations file ")
            list1 = ListOperation(self.list)
            list1.get_list()
            list1.sort_list()
            list1.reverse_list()
            list1.add_to_list(10)
            list1.remove_from_list(10)
        except Exception as e:
            self.logger.warning("Exception occured in listOperations file")
            self.logger.error(e)

    def submit_set(self):
        try:
            self.logger.info("Set submitted to the setOperations file ")
            set1 = SetOperation(self.set)
            set1.add_to_set(1000)
            set1.add_mulitple_elements([10, 20, 30])
            set1.delete_from_set(1000)
            set1.clear_set()
        except Exception as e:
            self.logger.warning("Exception occured in setOperations file")
            self.logger.error(e)

    def submit_tuple(self):
        try:
            self.logger.info("Tuple submitted to the tupleOperations file ")
            tuple1 = TupleOperation(self.tuple)
            tuple1.getTuple()
            tuple1.sort_tuple()
            tuple1.add_element(100)
            tuple1.index_tuple(3)
            tuple1.slice_tuple(0, 5)

        except Exception as e:
            self.logger.warning(("Exception occured in tupleOperations file"))
            self.logger.error(e)

    def submit_dict(self):
        try:
            self.logger.info("Dictionary submitted to the dictionaryOperations file ")
            dict1=DictOperation(self.dict)
            dict1.get_keys()
            dict1.get_values()
            dict1.insert_dict("name","pavan")
            dict1.delete_dict("name")

        except Exception as e:
            self.logger.warning("Exception occured in dictionaryOperations file")
            self.logger.error(e)


list = [1, 2, 4, 2, 10, 6, 78, 100, 45, 98, 56, 12]
set = {1, 2, 4, 2, 10, 6, 78, 100, 45, 98, 56, 12}
dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
tuple = (1, 2, 4, 2, 10, 6, 78, 100, 45, 98, 56, 12)

operations = AllOperations(list, set, dict, tuple)
operations.submit_list()
operations.submit_set()
operations.submit_tuple()
operations.submit_dict()
