class CustomerUser:
    def __init__(self, user_id="", password="", customer_id=""):
        self.__user_id = user_id
        self.__password = password
        self.__customer_id = customer_id

    def set_user_id(self, idu=""):
        self.__user_id = idu

    def get_user_id(self):
        return self.__user_id

    def set_password(self, password=""):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_customer_id(self, idc=""):
        self.__customer_id = idc

    def get_customer_id(self):
        return self.__customer_id
