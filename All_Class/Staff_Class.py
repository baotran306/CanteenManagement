from All_Class import Person_Class
Person = Person_Class.Person


class Staff(Person):
    def __init__(self, id_person="", name=None, gender=None, id_card=None, dob=None,
                 phone_num=None, address=None, salary=1000):
        super().__init__(id_person, name, gender, id_card, dob, phone_num, address)
        self.__salary = salary

    def set_id_person(self, ids=""):
        super(Staff, self).set_id_person(ids)

    def get_id_person(self):
        return super(Staff, self).get_id_person()

    def set_name(self, name=None):
        super(Staff, self).set_name(name)

    def get_name(self):
        return super(Staff, self).get_name()

    def set_gender(self, gender=None):
        super(Staff, self).set_gender(gender)

    def get_gender(self):
        return super(Staff, self).get_gender()

    def set_phone_num(self, phone=None):
        super(Staff, self).set_phone_num(phone)

    def get_phone_num(self):
        return super(Staff, self).get_phone_num()

    def set_address(self, add=None):
        super(Staff, self).set_address(add)

    def get_address(self):
        return super(Staff, self).get_address()

    def set_identity_card(self, id_card=None):
        super(Staff, self).set_identity_card(id_card)

    def get_identity_card(self):
        return super(Staff, self).get_identity_card()

    def set_day_of_birth(self, dob=None):
        super(Staff, self).set_day_of_birth(dob)

    def get_day_of_birth(self):
        return super(Staff, self).get_day_of_birth()

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


# if __name__ == '__main__':
#     ls = []
#     for i in range(5):
#         staff = Staff()
#         staff.set_name("Huy " + str(i))
#         ls.append(staff)
#     for i in ls:
#         print(i.get_name())
