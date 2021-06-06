class Food:
    def __init__(self, idf="", name="", des="", price=1000, img=""):
        self.__id = idf
        self.__name = name
        self.__describe = des
        self.__price = price
        self.__image = img

    def set_id(self, idf=""):
        self.__id = idf

    def get_id(self):
        return self.__id

    def set_name(self, name=""):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_describe(self, des=""):
        self.__describe = des

    def get_describe(self):
        return self.__describe

    def set_price(self, price=""):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_image(self, img=""):
        self.__image = img

    def get_image(self):
        return self.__image
