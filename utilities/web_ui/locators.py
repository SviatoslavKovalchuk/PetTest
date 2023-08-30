class Locators:
    def __init__(self, method, locator):
        self.__method = method
        self.__locator = locator

    def find_locator(self):
        return self.__method, self.__locator
