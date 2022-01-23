from loggingFolder.FileLogging import FileLogger


class ListOperation:
    def __init__(self, list):
        '''
        Adding list to the class
        :param list: list
        '''
        self.list = list
        self.logger = FileLogger()
        self.logger.info('ListOperations class initialized')

    def get_list(self):
        '''
        get all elements as list
        :return: list
        '''
        self.logger.info(f'Getting list {self.list}')
        return self.list

    def add_to_list(self, item):
        '''
        Adding item to list
        :param item : element
        return : list
        '''
        self.logger.info(f'Adding item {item} to list')
        self.list.append(item)
        self.logger.info(f'Returning list {self.list}')
        return self.list

    def remove_from_list(self, item):
        '''
        Removing item from list
        :param item: element
        :return: list
        '''
        self.logger.info(f'Removing item {item} from list')
        self.list.remove(item)
        self.logger.info(f'Returning list {self.list}')
        return self.list

    def sort_list(self):
        '''
        sorting the element in the list
        :return: list
        '''
        self.logger.info(f'Sorting list {self.list}')
        self.list.sort()
        self.logger.info(f'Returning sorted list {self.list}')
        return self.list

    def reverse_list(self):
        '''
        reverse the element in the list
        :return: list
        '''
        self.logger.info(f'Reversing list {self.list}')
        self.list.reverse()
        self.logger.info(f'Returning list {self.list}')
        return self.list

    def get_list_length(self):
        '''
        get the length of the list
        :return: int
        '''
        self.logger.info(f'Getting length of list {len(self.list)}')
        return len(self.list)
