class CustomerOrder:
    def __init__(self, idb="", order_time="", status_now=1, staff_id="", address=None, customer_id=None):
        self.__id_order = idb
        self.__order_time = order_time
        self.__staff_id = staff_id
        self.__status_now = status_now  # status = 1 is delivered, status = 0 is not complete, 2 is cancel
        self.__address = address
        self.__customer_id = customer_id

    def set_id_order(self, idb=""):
        self.__id_order = idb

    def get_id_order(self):
        return self.__id_order

    def set_order_time(self, ort=""):
        self.__order_time = ort

    def get_order_time(self):
        return self.__order_time

    def set_staff_id(self, ids=""):
        self.__staff_id = ids

    def get_staff_id(self):
        return self.__staff_id

    def set_status_now(self, st=1):
        self.__status_now = st

    def get_status_now(self):
        return self.__status_now

    def set_customer_id(self, idc=None):
        self.__customer_id = idc

    def get_customer_id(self):
        return self.__customer_id

    def set_address(self, address=None):
        self.__customer_id = address

    def get_address(self):
        return self.__customer_id
