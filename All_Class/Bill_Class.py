class Bill:
    def __init__(self, idb="", ordertime="", status_now=1, staffid=""):
        self.__id_bill = idb
        self.__order_time = ordertime
        self.__staff_id = staffid
        self.__status_now = status_now  # status = 1 is delivered, status = 0 is not com

    def set_id_bill(self, idb):
        self.__id_bill = idb

    def get_id_bill(self):
        return self.__id_bill

    def set_order_time(self, ort):
        self.__order_time = ort

    def get_order_time(self):
        return self.__order_time

    def set_staff_id(self, ids):
        self.__staff_id = ids

    def get_staff_id(self):
        return self.__staff_id

    def set_status_now(self, st):
        self.__status_now = st

    def get_status_now(self):
        return self.__status_now
