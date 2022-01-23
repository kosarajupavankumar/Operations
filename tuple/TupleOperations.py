from loggingFolder.FileLogging import FileLogger

class TupleOperation:
    '''
    Tuple Operations class
    '''
    def __init__(self,tuple):
        '''
        tuple class constructor 
        :param tuple: 
        '''''
        self.tuple= tuple
        self.logger = FileLogger()
        self.logger.info("TupleOperations class initialized")

    def getTuple(self):
        '''
        get tuple
        :return: tuple
        '''
        self.logger.info(f"Get the tuple --> {self.tuple}")
        return self.tuple

    # create the function to add the element in the tuple

    def add_element(self,element):
        '''
        add element in the tuple
        :param element:
        '''
        self.logger.info(f"Add element in the tuple --> {element}")
        self.tuple = self.tuple + (element,)
        self.logger.info(f"Tuple after adding element --> {self.tuple}")

    # Indexing the tuple
    def index_tuple(self,index):
        '''
        indexing the tuple
        :param index:
        '''
        self.logger.info(f"Index of {index} the tuple --> {self.tuple[index]}")
        return self.tuple[index]

    # Slicing the tuple
    def slice_tuple(self,start,end):
        '''
        slicing the tuple
        :param start:
        :param end:
        '''
        self.logger.info(f"Slicing the tuple --> {self.tuple[start:end]}")
        return self.tuple[start:end]

    # Sorting the tuple
    def sort_tuple(self):
        '''
        sorting the tuple
        '''
        self.logger.info(f"Sorting the tuple --> {sorted(self.tuple)}")
        return sorted(self.tuple)

