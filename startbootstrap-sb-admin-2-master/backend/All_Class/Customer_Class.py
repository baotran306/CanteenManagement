from All_Class import Person_Class

Person = Person_Class.Person


class Customer(Person):
    def __init__(self, id_person="", name=None, gender=None, id_card=None, dob=None,
                 phone_num=None, address=None, vip='NO'):
        super().__init__(id_person, name, gender, id_card, dob, phone_num, address)
        self.__vip = vip

    def set_id_person(self, ids=""):
        super(Customer, self).set_id_person(ids)

    def get_id_person(self):
        return super(Customer, self).get_id_person()

    def set_name(self, name=None):
        super(Customer, self).set_name(name)

    def get_name(self):
        return super(Customer, self).get_name()

    def set_gender(self, gender=None):
        super(Customer, self).set_gender(gender)

    def get_gender(self):
        return super(Customer, self).get_gender()

    def set_phone_num(self, phone=None):
        super(Customer, self).set_phone_num(phone)

    def get_phone_num(self):
        return super(Customer, self).get_phone_num()

    def set_address(self, add=None):
        super(Customer, self).set_address(add)

    def get_address(self):
        return super(Customer, self).get_address()

    def set_identity_card(self, id_card=None):
        super(Customer, self).set_identity_card(id_card)

    def get_identity_card(self):
        return super(Customer, self).get_identity_card()

    def set_day_of_birth(self, dob=None):
        super(Customer, self).set_day_of_birth(dob)

    def get_day_of_birth(self):
        return super(Customer, self).get_day_of_birth()

    def set_vip(self, vip='NO'):
        self.__vip = vip

    def get_vip(self):
        return self.__vip


# if __name__ == '__main__':
#     cus = Customer()
#     cus.set_name("Nguyen Quoc Thang")
