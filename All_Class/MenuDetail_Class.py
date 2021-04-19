class MenuDetail:
    def __init__(self, menu_id="", food_id=""):
        self.__menu_id = menu_id
        self.__food_id = food_id

    def set_menu_id(self, ido=""):
        self.__menu_id = ido

    def get_menu_id(self):
        return self.__menu_id

    def set_food_id(self, idf=""):
        self.__food_id = idf

    def get_food_id(self):
        return self.__food_id
