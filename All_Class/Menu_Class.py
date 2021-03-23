class Menu:
    def __init__(self, idm="", date=""):
        self.__id = idm
        self.__date_now = date

    def set_id(self, idm):
        self.__id = idm

    def get_id(self):
        return self.__id

    def set_date_now(self, date):
        self.__date_now = date

    def get_date_now(self):
        return self.__date_now
