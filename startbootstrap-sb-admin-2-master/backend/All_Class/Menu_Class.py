class Menu:
    def __init__(self, idm="", time_start="", time_end=""):
        self.__id = idm
        self.__time_start = time_start
        self.__time_end = time_end

    def set_id(self, idm=""):
        self.__id = idm

    def get_id(self):
        return self.__id

    def set_time_start(self, time=""):
        self.__time_start = time

    def get_time_start(self):
        return self.__time_start

    def set_time_end(self, time=""):
        self.__time_end = time

    def get_time_end(self):
        return self.__time_end
