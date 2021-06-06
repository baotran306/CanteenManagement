class User:
    def __init__(self, user_id="", password="", role_id="", staff_id=""):
        self.__user_id = user_id
        self.__password = password
        self.__role_id = role_id
        self.__staff_id = staff_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_user_id(self):
        return self.__user_id

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_role_id(self, role_id):
        self.__role_id = role_id

    def get_role_id(self):
        return self.__role_id

    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

    def get_staff_id(self):
        return self.__staff_id
