class OderDetail:
    def __init__(self, order_id, food_id, num=1, price=0):
        self.__order_id = order_id
        self.__food_id = food_id
        self.__num_of_foods = num
        self.__cur_price = price

    def set_order_id(self, ido):
        self.__order_id = ido

    def get_order_id(self):
        return self.__order_id

    def set_food_id(self, idf):
        self.__food_id = idf

    def get_food_id(self):
        return self.__food_id

    def set_num_of_foods(self, num):
        self.__num_of_foods = num

    def get_num_of_foods(self):
        return self.__num_of_foods

    def set_cur_price(self, price):
        self.__cur_price = price

    def get_cur_price(self):
        return self.__cur_price
