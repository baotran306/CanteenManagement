class Role:
    def __init__(self, role_id, role_name):
        self.__role_id = role_id
        self.__role_name = role_name

    def set_user_id(self, role_id):
        self.__role_id = role_id

    def get_user_id(self):
        return self.__role_id

    def set_role_name(self, name):
        self.__role_name = name

    def get_role_name(self):
        return self.__role_name
