class Staff:
    def __init__(self, id_staff="", name="", id_card="", dob="", phone_num="", address=""):
        self.__id_staff = id_staff
        self.__name = name
        self.__identity_card = id_card
        self.__day_of_birth = dob
        self.__phone_num = phone_num
        self.__address = address

    def set_id_staff(self, ids):
        self.__id_staff = ids

    def get_id_staff(self):
        return self.__id_staff

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_phone_num(self, phone):
        self.__phone_num = phone

    def get_phone_num(self):
        return self.__phone_num

    def set_address(self, add):
        self.__address = add

    def get_address(self):
        return self.__address

    def set_identity_card(self, id_card):
        self.__identity_card = id_card

    def get_identity_card(self):
        return self.__identity_card

    def set_day_of_birth(self, dob):
        self.__day_of_birth = dob

    def get_day_of_birth(self):
        return self.__day_of_birth
