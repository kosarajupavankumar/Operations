from loggingFolder.FileLogging import FileLogger

class SetOperation:

    def __init__(self, set):
        '''
        Adding set to SetoperationsConstructor
        :param set:
        '''

        self.set = set
        self.logger = FileLogger()
        self.logger.info("SetOperations class initialized")

    # create the function to add element in set
    def add_to_set(self, element):
        '''
        "function is used to Adding element to the set
        :param element:
        :return:
        '''
        self.logger.info(f"Adding element {element} to the set")
        self.set.add(element)
        self.logger.info(f"Element {element} added to the set")
        return self.set

    # Delete the element from the set
    def delete_from_set(self, element):
        '''
        "function is used to Delete the element in the set"
        :param element:
        :return:
        '''
        self.logger.info(f"Deleting element {element} from the set")
        self.set.discard(element)
        self.logger.info(f"Element {element} deleted from the set--> {self.set}")
        return self.set

    # Add multiple elements in the set
    def add_mulitple_elements(self, elements):
        '''
        "function is used to Add multiple elements in the set"
        :param elements:
        :return:
        '''
        self.logger.info(f"Adding multiple elements {elements} to the set")
        self.set.update(elements)
        self.logger.info(f"Multiple elements {elements} added to the set--> {self.set}")
        return self.set

    # clear all the elements in the set
    def clear_set(self):
        '''
        function is used to clear all the elements in the set
        :return:
        '''
        self.logger.info(f"Clearing all the elements in the set")
        self.set.clear()
        self.logger.info(f"All the elements in the set cleared successfully --> {self.set}")
        return self.set
