class Person:
    def __init__(self, id_person="", name=None, gender=None, id_card=None, dob=None, phone_num=None, address=None):
        self.__id_person = id_person
        self.__name = name
        self.__gender = gender
        self.__identity_card = id_card
        self.__day_of_birth = dob
        self.__phone_num = phone_num
        self.__address = address

    def set_id_person(self, ids=""):
        self.__id_person = ids

    def get_id_person(self):
        return self.__id_person

    def set_name(self, name=None):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_gender(self, gender=None):
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_phone_num(self, phone=None):
        self.__phone_num = phone

    def get_phone_num(self):
        return self.__phone_num

    def set_address(self, add=None):
        self.__address = add

    def get_address(self):
        return self.__address

    def set_identity_card(self, id_card=None):
        self.__identity_card = id_card

    def get_identity_card(self):
        return self.__identity_card

    def set_day_of_birth(self, dob=None):
        self.__day_of_birth = dob

    def get_day_of_birth(self):
        return self.__day_of_birth
