import pyodbc
import Processing.CheckValidTime as ck
import Processing.ExtraFunctions as ef

connect = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=WINDOWS-A251ALV;"
    "Database=CanTeenManagement;"
    "Trusted_Connection=yes;"
)


class SqlFunction:
    def __init__(self):
        self.func = connect.cursor()

    def check_existed_id(self, tablename, idb):
        # Note: be careful with no existed table name
        try:
            cursor = self.func
            if tablename.lower() == 'userlogin' or tablename.lower() == 'customeruser':
                cursor.execute("select * from {} where user_id = ?".format(tablename), idb)
            elif tablename.lower() == 'orderdetail':
                cursor.execute("select * from {} where order_id = ?".format(tablename), idb)
            elif tablename.lower() == 'menudetail':
                cursor.execute("select * from {} where menu_id = ?".format(tablename), idb)
            else:
                cursor.execute("select * from {} where id = ?".format(tablename), idb)
            cnt = 0
            for _ in cursor:
                cnt += 1
                break
            cursor.commit()
            if cnt == 0:
                return False
            else:
                return True
        except Exception as ex:
            print("----Error in check_existed_id----")
            print(ex)
            return False

    def check_existed_foreign_key_order(self, person_id, type_person=0):
        """
        :param person_id: id of person who need to check existed
        :param type_person: type_person = 0 is customer, person_id is customer_id, else staff_id
        :return: True if existed, else false
        """
        try:
            cnt = 0
            cursor = self.func
            if type_person == 0:
                cursor.execute("select * from CustomerOrder where customer_id = ?", person_id)
            else:
                cursor.execute("select * from CustomerOrder where staff_id = ?", person_id)
            for _ in cursor:
                cnt += 1
                break
            cursor.commit()
            if cnt == 0:
                return False
            return False
        except Exception as ex:
            print("----Error in check_existed_foreign_key_order----")
            print(ex)
            return False

    def is_empty(self, table_name):
        # Be careful with no existed table name
        try:
            cursor = self.func
            cursor.execute('select * from {}'.format(table_name))

            cnt = 0
            for _ in cursor:
                cnt += 1
                break
            cursor.commit()
            if cnt == 0:
                return True
            else:
                return False
        except Exception as ex:
            print('----Error in is_empty----')
            print(ex)
            return False

    def check_existed_column(self, table_name, col):
        try:
            cursor = self.func
            cursor.execute("select {}.{} from {}".format(table_name, col, table_name))
        except Exception as ex:
            print(ex)
            print('maybe col not found in table')
            return False
        return True

    def get_pass_of_staff(self, ids):
        cursor = self.func
        cursor.execute("select password from userlogin where user_id = ?", ids)
        ans = ""
        for i in cursor:
            ans = i
        if ans != "":
            return ans[0]
        else:
            return None

    def get_pass_of_customer(self, idc):
        cursor = self.func
        cursor.execute("select password from customeruser where user_id = ?", idc)
        ans = ""
        for i in cursor:
            ans = i
        if ans != "":
            return ans[0]
        else:
            return None

    def insert_menu(self, date_start, date_end):
        try:
            if not ck.check_format_datetime(date_start) or not ck.check_format_datetime(date_end):
                return False
            if not ck.check_limit_time(date_start) or not ck.check_limit_time(date_end):
                return False
            if not ck.check_start_end_time(date_start, date_end):
                return False
            cursor = self.func
            cursor.execute(
                'insert into Menu values (?, ?);',
                date_start, date_end
            )
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in insert_menu----')
            print(ex)
            return False

    def insert_food(self, name, des, price, img=""):
        try:
            cursor = self.func
            cursor.execute(
                'insert into food values (?, ?, ?, ?);',
                (name, des, price, img)
            )
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in insert food----')
            print(ex)
            return False

    def insert_person(self, ids, name=None, gender=None, id_card=None, dob=None, phone=None, addr=None):
        try:
            if self.check_existed_id("person", ids):
                return False
            if not ef.check_str_all_num(phone) or not ef.check_str_all_num(id_card):
                return False
            cursor = self.func
            cursor.execute(
                'insert into person values (?, ?, ?, ?, ?, ?, ?);',
                (ids, name, gender, id_card, dob, phone, addr)
            )
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in insert_person----')
            print(ex)
            return False

    def insert_staff(self, ids, salary=None):
        try:
            if not self.check_existed_id("person", ids):
                return False
            if self.check_existed_id("staff", ids):
                return False
            cursor = self.func
            cursor.execute("insert into staff values(?, ?)", ids, salary)
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in insert_staff----')
            print(ex)
            return False

    def insert_customer(self, idc, vip):
        try:
            vip = vip.upper()
            if not ef.check_type_customer(vip):
                return False
            if not self.check_existed_id("person", idc):
                return False
            if self.check_existed_id("customer", idc):
                return False
            cursor = self.func
            cursor.execute("insert into customer values(?, ?)", idc, vip)
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in insert customer----')
            print(ex)
            return False

    def insert_customer_order(self, time, stt, staff_id, address=None, cus_id=None):
        try:
            if not ck.check_limit_time(time):
                return False
            if not self.check_existed_id("Staff", staff_id):
                return False
            if not ck.check_format_datetime(time):
                return False
            if not ef.check_status_order(stt):
                return False
            cursor = self.func
            cursor.execute(
                'insert into CustomerOrder values (?, ?, ?, ?, ?);',
                (time, stt, staff_id, address, cus_id)
            )
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in insert_customer_order----')
            print(ex)
            return False

    def insert_role(self, role_name):
        try:
            cursor = self.func
            cursor.execute("insert into Role values (?);", role_name)
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in insert_role----')
            print(ex)
            return False

    def insert_user_login(self, user_id, password, role_id, staff_id):
        try:
            if not self.check_existed_id("staff", staff_id):
                return False
            if self.check_existed_id("userlogin", user_id):
                return False
            if not self.check_existed_id("Role", role_id):
                return False
            if not ef.check_regex_password(password):
                return False
            cursor = self.func
            cursor.execute("insert into UserLogin values (?, ?, ?, ?);", (user_id, password, role_id, staff_id))
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error insert_user_logic----')
            print(ex)
            return False

    def insert_customer_user(self, user_id, password, customer_id):
        try:
            if self.check_existed_id("CustomerUser", user_id):
                return False
            if not self.check_existed_id("Customer", customer_id):
                return False
            if not ef.check_regex_password(password):
                return False
            cursor = self.func
            cursor.execute("insert into CustomerUser values(?, ?, ?);", (user_id, password, customer_id))
            cursor.commit()
            return True
        except Exception as ex:
            print("----Error in insert_customer_user")
            print(ex)
            return False

    def insert_menu_detail(self, menu_id, food_id):
        try:
            if self.check_existed_id("menu", menu_id) and self.check_existed_id("food", food_id):
                cursor = self.func
                cnt = 0
                cursor.execute('select * from MenuDetail where menu_id = ? and food_id = ?', menu_id, food_id)
                for _ in cursor:
                    cnt += 1
                    break
                if cnt == 0:
                    cursor.execute('insert into MenuDetail values (?, ?)', menu_id, food_id)
                    cursor.commit()
                    return True
                else:
                    print('Food existed in menu, don\'t need add')
                    cursor.commit()
                    return False
            else:
                print('No existed menu_id or food_id in insert_menu_detail')
                return False
        except Exception as ex:
            print("----Error in insert_menu_detail----")
            print(ex)
            return False

    def insert_order_detail(self, order_id, food_id, num_of_food, cur_price):
        try:
            if num_of_food < 0 or cur_price < 0:
                return False
            if self.check_existed_id("Food", food_id) and self.check_existed_id("CustomerOrder", order_id):
                cursor = self.func
                cursor.execute("select * from OrderDetail where order_id = ?, food_id = ?", order_id, food_id)
                cnt = 0
                for _ in cursor:
                    cnt += 1
                    break
                if cnt == 0:
                    cursor.execute("insert into OrderDetail values (?, ?, ?, ?)",
                                   order_id, food_id, num_of_food, cur_price)
                    cursor.commit()
                    return True
                else:
                    print('food existed in current OrderDetail, don\'t need to add')
                    cursor.commit()
                    return False

            else:
                print('No existed order_id or food_id in insert_order_detail')
                return False
        except Exception as ex:
            print("----Error in insert_order_detail----")
            print(ex)
            return False

    def delete_function(self, table_name, col, val):
        """
        ex: "menu", "id", "1123"
        Be careful with no existed table name
        should be delete foreign key reference table first
        Example, must be delete all bill of staff before delete staff else return false

        :param table_name: name of table  in sql
        :param val: id of row need to delete
        :param col: id of row need to delete
        :return: if delete success return True(maybe delete 0 row if val not existed), else return False
        """
        try:
            if self.is_empty(table_name):
                return False
            if not self.check_existed_column(table_name, col):
                return False
            # loi
            cursor = self.func
            cursor.execute('delete from {} where {} = {}'.format(table_name, col, val))
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in delete_function----')
            print(ex)
            return False

    def update_menu(self, idm, date_start, date_end):
        try:
            if not self.check_existed_id("menu", idm):
                return False
            if not ck.check_format_datetime(date_start):
                return False
            if not ck.check_format_datetime(date_end):
                return False
            if not ck.check_start_end_time(date_start, date_end):
                return False
            if not ck.check_limit_time(date_start) or not ck.check_limit_time(date_end):
                return False
            cursor = self.func
            cursor.execute(
                'update Menu set time_start = ?, time_end = ? where id = ?',
                (date_start, date_end, idm)
            )
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in update_menu----')
            print(ex)
            return False

    def update_food(self, idf, name, des, price, img=""):
        try:
            if not self.check_existed_id("food", idf):
                return False
            cursor = self.func
            cursor.execute(
                'update food set name = ?, describe = ?, price = ?, img = ? where id = ?;',
                (name, des, price, img, idf)
            )
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in update_food----')
            print(ex)
            return False

    def update_person(self, ids, name=None, gender=None, id_card=None, dob=None, phone=None, addr=None):
        try:
            if not self.check_existed_id("person", ids):
                return False
            cursor = self.func
            cursor.execute(
                'update person set name = ?, gender = ?, identity_card = ?, day_of_birth = ?,'
                ' phone_num = ?, address = ? where id = ?;',
                (name, gender, id_card, dob, phone, addr, ids)
            )
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in update_person----')
            print(ex)
            return False

    def update_staff(self, ids, salary):
        try:
            cursor = self.func
            if not self.check_existed_id("Staff", ids):
                return False
            cursor.execute("update staff set salary = ? where id = ?", salary, ids)
            cursor.commit()
            return True
        except Exception as ex:
            print("----Error in update_staff----")
            print(ex)
            return False

    def update_customer(self, ids, vip):
        try:
            vip = vip.upper()
            if not ef.check_type_customer(vip):
                return False
            cursor = self.func
            if not self.check_existed_id("Customer", ids):
                return False
            cursor.execute("update Customer set vip = ? where id = ?", vip, ids)
            cursor.commit()
            return True
        except Exception as ex:
            print("----Error in update_customer----")
            print(ex)
            return False

    def update_user_login_password(self, user_id, password):
        try:
            if not self.check_existed_id("userlogin", user_id):
                return False
            if not ef.check_regex_password(password):
                return False
            cursor = self.func
            cursor.execute("update UserLogin set password = ? where user_id = ?", (password, user_id))
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error update_user_login_password----')
            print(ex)
            return False

    def update_user_login_role(self, user_id, role_id):
        try:
            if not self.check_existed_id("userlogin", user_id):
                return False
            if not self.check_existed_id("Role", role_id):
                return False
            cursor = self.func
            cursor.execute("update UserLogin set role_id = ? "
                           "where user_id = ?", (role_id, user_id))
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error insert_user_login_role----')
            print(ex)
            return False

    def update_customer_user_password(self, user_id, password):
        try:
            if not self.check_existed_id("CustomerUser", user_id):
                return False
            if not ef.check_regex_password(password):
                return False
            cursor = self.func
            cursor.execute("update CustomerUser set password = ? where user_id = ?;", (password, user_id))
            cursor.commit()
            return True
        except Exception as ex:
            print("----Error in insert_customer_user_password")
            print(ex)
            return False

    def update_customer_order(self, ido, stt):
        try:
            if not ef.check_status_order(stt):
                return False
            if not self.check_existed_id("CustomerOrder", ido):
                return False
            cursor = self.func
            cursor.execute("update CustomerOrder set status_now = ? where id = ?", stt, ido)
            cursor.commit()
            return True
            pass
        except Exception as ex:
            print('----Error in update_customer_order')
            print(ex)
            return False

    def check_login_staff(self, user_id, pass_staff):
        try:
            if not self.check_existed_id("UserLogin", user_id):
                return False
            else:
                if pass_staff == self.get_pass_of_staff(user_id):
                    return True
                else:
                    return False
        except Exception as ex:
            print('----Error in check_login_staff----')
            print(ex)
            return False

    def check_login_customer(self, user_id, pass_cus):
        try:
            if not self.check_existed_id("CustomerUser", user_id):
                return False
            else:
                if pass_cus == self.get_pass_of_customer(user_id):
                    return True
                else:
                    return False
        except Exception as ex:
            print('----Error in check_login_customer----')
            print(ex)
            return False

    def get_info_staff_by_id(self, ids):
        """
        :param ids: id of staff need to find info
        :return: List of all info of this staff
        [staff_id, name, gender, identity_card, day_of_birth, phone_num, address, role_name, salary]
        """
        try:
            if self.check_existed_id("staff", ids):
                cursor = self.func
                sql = "select * from dbo.SelectInfoStaffByID(?)"
                cursor.execute(sql, ids)
                ans = []
                for row in cursor:
                    ans.append(row[0])
                    ans.append(row[1])
                    ans.append(row[2])
                    ans.append(row[3])
                    ans.append(str(row[4]))
                    ans.append(row[5])
                    ans.append(row[6])
                    ans.append(row[7])
                    if row[8] is None:
                        row[8] = 0
                    ans.append(float(row[8]))
                    break
                cursor.commit()
                return ans
            else:
                print("Id staff not existed in get_info_staff_by_id")
                return None
        except Exception as ex:
            print("----Error in get_info_staff_by_id----")
            print(ex)
            return False

    def get_info_all_staff(self):
        """
        :return: List of all staff
        [staff_id, name, gender, identity_card, day_of_birth, phone_num, address, role_name, salary]
        """
        try:
            cursor = self.func
            sql = "select * from dbo.SelectAllInfoStaff()"
            rows = cursor.execute(sql)
            ans = []
            for row in rows:
                if row[8] is None:
                    row[8] = 0
                tmp = [row[0], row[1], row[2], row[3], str(row[4]), row[5], row[6], row[7], float(row[8])]
                ans.append(tmp)
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_all_info_staff----")
            print(ex)
            return False

    def get_info_customer_by_id(self, ids):
        """
        :param ids: id of customer need to find info
        :return: List of all info of this customer
        [customer_id, name, gender, identity_card, day_of_birth, phone_num, address, vip_member]
        """
        try:
            if self.check_existed_id("customer", ids):
                cursor = self.func
                sql = "select * from dbo.SelectInfoCustomerByID(?)"
                cursor.execute(sql, ids)
                ans = []
                for row in cursor:
                    ans.append(row[0])
                    ans.append(row[1])
                    ans.append(row[2])
                    ans.append(row[3])
                    ans.append(str(row[4]))
                    ans.append(row[5])
                    ans.append(row[6])
                    ans.append(row[7])
                    break
                cursor.commit()
                return ans
            else:
                print("Id customer not existed in get_info_customer_by_id")
                return None
        except Exception as ex:
            print("----Error in get_info_customer_by_id----")
            print(ex)
            return False

    def get_all_info_customer(self):
        """
        :return: List of all info of all customer
        [customer_id, name, gender, identity_card, day_of_birth, phone_num, address, vip_member]
        """
        try:
            cursor = self.func
            sql = "select * from dbo.SelectAllInfoCustomer()"
            cursor.execute(sql)
            ans = []
            for row in cursor:
                tmp = [row[0], row[1], row[2], row[3], str(row[4]), row[5], row[6], row[7]]
                ans.append(tmp)
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_all_info_customer----")
            print(ex)
            return False

    def get_all_food(self):
        try:
            cursor = self.func
            cursor.execute("select * from food")
            list_food = []
            for r in cursor:
                list_food.append([r[0], r[1], r[2], float(r[3]), r[4]])
            return list_food
        except Exception as ex:
            print("----Error in all_food----")
            print(ex)
            return []

    def get_info_food_by_id(self, id_food):
        try:
            cursor = self.func
            cursor.execute("select * from food where id = ?", id_food)
            info_food = []
            for r in cursor:
                info_food = [r[0], r[1], r[2], float(r[3]), r[4]]
            return info_food
        except Exception as ex:
            print("----Error in all_food----")
            print(ex)
            return []

    def get_info_menu_detail(self, menu_id):
        try:
            cursor = self.func
            if not self.check_existed_id("MenuDetail", menu_id):
                return []
            cursor.execute("select name, describe, price, img from Food, MenuDetail "
                           "where food.id = menudetail.food_id and menudetail.menu_id = ?", menu_id)
            ans = []
            for r in cursor:
                tmp = [r[0], r[1], float(r[2]), r[3]]
                ans.append(tmp)
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_info_menu_detail----")
            print(ex)
            return []

    def calculate_order_id(self, order_id):
        try:
            if not self.check_existed_id("OrderDetail", order_id):
                print('----order_id not existed, cann\'t calculate revenue----')
                return 0
            cursor = self.func
            cursor.execute("select dbo.CalculateOrderID(?)", order_id)
            ans = []
            for c in cursor:
                ans = c
            cursor.commit()
            return float(ans[0])
        except Exception as ex:
            print("----Error in calculate_order_id----")
            print(ex)
            return 0

    def stats_order_revenue(self):
        try:
            cursor = self.func
            cursor.execute("select * from dbo.InfoOrder()")
            ans = []
            for r in cursor:
                tmp = [r[0], float(r[1]), str(r[3]), ef.status_type(r[4]), r[5], r[6], r[7]]
                ans.append(tmp)
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in stats_order_revenue----")
            print(ex)
            return False

    def stats_revenue_by_month(self, year):
        try:
            cursor = self.func
            cursor.execute("select * from dbo.StatsRevenueByMonth(?)", year)
            ans = []
            for r in cursor:
                tmp = [r[0], float(r[1])]
                ans.append(tmp)
            cursor.commit()
            return ans
        except Exception as ex:
            print('----Error in stats_revenue_by_month----')
            print(ex)
            return False

    def stats_revenue_by_day(self, day):
        try:
            day = day.strip()
            cursor = self.func
            cursor.execute("select * from dbo.StatsRevenueByDay(?)", day)
            ans = []
            for r in cursor:
                ans.append(r[0])
                ans.append(float(r[1]))
                break
            cursor.execute("select * from dbo.CountSuccessOrder(?)", day)
            for r in cursor:
                ans.append(r[1])
                break
            cursor.execute("select * from dbo.CountAllOrder(?)", day)
            for r in cursor:
                ans.append('{:.02f}%'.format(float(ans[-1]) / r[1] * 100))
                break
            cursor.commit()
            if len(ans) == 0:
                ans.append(day)
                ans.append(float(0))
                ans.append(float(0))
                ans.append('0%')
            return ans
        except Exception as ex:
            print('----Error in stats_revenue_by_day----')
            print(ex)
            return False

    def generate_new_id_person(self, type_id):
        try:
            cursor = self.func
            if type_id == 0:  # type 0 is Staff
                cursor.execute("select top(1) id from Person where id like 'NV%' order by id desc")
            else:  # Customer
                cursor.execute("select top(1) id from Person where id like 'KH%' order by id desc")
            ans = ""
            for r in cursor:
                ans = r[0]
                break
            cursor.commit()
            ans = ef.auto_generate_id_person(ans)
            return ans
        except Exception as ex:
            print("----Error in generate_new_id_person----")
            print(ex)
            return ""

    def get_id_card(self, id_inp):
        """
        Get identity card of person
        :param id_inp: id of person who need to get identity car
        :return: identity card of this Person
        """
        try:
            if not self.check_existed_id("Person", id_inp):
                return ""
            cursor = self.func
            cursor.execute("select identity_card from Person where id = ?", id_inp)
            ans = ""
            for c in cursor:
                ans = c[0]
                break
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_id_card----")
            print(ex)
            return ""

    def get_phone_num(self, id_inp):
        """
        Get identity card of person
        :param id_inp: id of person who need to get phone number
        :return: phone number of this Person
        """
        try:
            if not self.check_existed_id("Person", id_inp):
                return ""
            cursor = self.func
            cursor.execute("select phone_num from Person where id = ?", id_inp)
            ans = ""
            for c in cursor:
                ans = c[0]
                break
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_phone_num----")
            print(ex)
            return ""

    def get_id_person_from_user(self, user_name, type_person=0):
        """
        Get identity card of person
        :param user_name: user name of person who need to get id
        :param type_person: if type_person = 0 is customer else staff
        :return: id of this Person
        """
        try:
            cursor = self.func
            if type_person == 0:
                if not self.check_existed_id("CustomerUser", user_name):
                    return ""
                cursor.execute("select customer_id from CustomerUser where user_id = ?", user_name)
            else:
                if not self.check_existed_id("UserLogin", user_name):
                    return ""
                cursor.execute("select staff_id from UserLogin where user_id = ?", user_name)
            ans = ""
            for c in cursor:
                ans = c[0]
                break
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_id_person_from_user----")
            print(ex)
            return ""

    def get_user_from_id(self, id_person, type_person=0):
        """
        Get identity card of person
        :param id_person: id of person who need to get id
        :param type_person: if type_person = 0 is customer else staff
        :return: user_name of this Person
        """
        try:
            cursor = self.func
            if type_person == 0:
                if not self.check_existed_id("Customer", id_person):
                    return ""
                cursor.execute("select user_id from CustomerUser where customer_id = ?", id_person)
            else:
                if not self.check_existed_id("Staff", id_person):
                    return ""
                cursor.execute("select user_id from UserLogin where staff_id = ?", id_person)
            ans = ""
            for c in cursor:
                ans = c[0]
                break
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_user_from_id----")
            print(ex)
            return ""

    def reset_password_staff(self, user_name, id_card, phone, new_pass):
        try:
            if not self.check_existed_id("UserLogin", user_name):
                return False
            if not ef.check_regex_password(new_pass):
                return False
            id_staff = self.get_user_from_id(user_name, 1)
            if self.get_id_card(id_staff) == id_card and self.get_phone_num(id_staff) == phone:
                return self.update_user_login_password(user_name, new_pass)
            else:
                return False
        except Exception as ex:
            print('----Error in reset_password_staff')
            print(ex)
            return False

    def reset_password_customer(self, user_name, id_card, phone, new_pass):
        try:
            if not self.check_existed_id("CustomerUser", user_name):
                return False
            if not ef.check_regex_password(new_pass):
                return False
            id_customer = self.get_user_from_id(user_name, 0)
            if self.get_id_card(id_customer) == id_card and self.get_phone_num(id_customer) == phone:
                return self.update_customer_user_password(user_name, new_pass)
            else:
                return False
        except Exception as ex:
            print('----Error in reset_password_customer')
            print(ex)
            return False

    def get_cus_name_in_order(self, id_order):
        try:
            if not self.check_existed_id("CustomerOrder", id_order):
                return ""
            cursor = self.func
            cursor.execute("select customer_id from CustomerOrder where id = ?", id_order)
            cus_id = ""
            for row in cursor:
                cus_id = row[0]
                break
            if cus_id is None:
                return ""
            cursor.execute("select name from Person where id = ?", cus_id)
            cus_name = ""
            for row in cursor:
                cus_name = row[0]
                break
            if cus_name is None:
                return ""
            else:
                return cus_name
        except Exception as ex:
            print("----error in get_cus_name_in_order----")
            print(ex)
            return ""

    def get_order_time_stt_address_by_id(self, id_order):
        try:
            if not self.check_existed_id("CustomerOrder", id_order):
                return []
            cursor = self.func
            cursor.execute("select order_time, status_now, address from CustomerOrder where id = ?", id_order)
            ans = []
            for r in cursor:
                ans.append(str(r[0]))
                ans.append(ef.status_type(r[1]))
                ans.append(r[2])
                break
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_order_time_and_stt_by_id")
            print(ex)
            return []

    def get_info_order_detail_by_id(self, id_order):
        try:
            if not self.check_existed_id("OrderDetail", id_order):
                return []
            cursor = self.func
            cursor.execute("select food_id, num_of_food, cur_price from OrderDetail where order_id = ?", id_order)
            info = [id_order]
            food_list = []
            num_list = []
            cur_price = []
            for r in cursor:
                food_list.append(r[0])
                num_list.append(int(r[1]))
                cur_price.append(float(r[2]))
            info.append([self.get_food_name_by_id(x) for x in food_list])
            info.append(num_list)
            info.append(cur_price)
            info.append(self.calculate_order_id(id_order))
            info_order = self.get_order_time_stt_address_by_id(id_order)
            info.append(info_order[0])
            info.append(info_order[1])
            info.append(info_order[2])
            info.append(self.get_cus_name_in_order(id_order))
            cursor.commit()
            return info
        except Exception as ex:
            print('----Error in get_info_order_detail_by_id')
            print(ex)
            return []

    def get_all_order_by_cus_id(self, customer_id):
        try:
            if not self.check_existed_id("Customer", customer_id):
                return []
            cursor = self.func
            cursor.execute("select id from CustomerOrder where customer_id = ?", customer_id)
            list_id = []
            info = []
            for id_order in cursor:
                list_id.append(id_order[0])
            for id_order in list_id:
                info.append(self.get_info_order_detail_by_id(id_order))
            cursor.commit()
            return info
        except Exception as ex:
            print("----Error in get_all_order_by_cus_id----")
            print(ex)
            return []

    def get_all_info_order(self, type_inp=0):
        """
        :param type_inp: type of order which want to select.
            - type = 0 is  order has status = 0 (Not complete ship)
            - type = 1 is  order has status = 1 (Completed ship)
            - type = 2 is order has status = 2 (Delivering)
            - type = 3 is  order has status = 3 (Cancel Order)
            else all of order
        :return: list of info order
        """
        try:
            cursor = self.func
            if type_inp not in [0, 1, 2, 3]:
                cursor.execute("select id from CustomerOrder")
            else:
                cursor.execute("select id from CustomerOrder where status_now = ?", type_inp)
            list_id = []
            for r in cursor:
                list_id.append(r[0])
            ans = []
            for id_order in list_id:
                if not self.check_existed_id("OrderDetail", id_order):
                    continue
                ans.append(self.get_info_order_detail_by_id(id_order))
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_all_info_order----")
            print(ex)
            return []

    def get_food_name_by_id(self, food_id):
        try:
            cursor = self.func
            if not self.check_existed_id("Food", food_id):
                return ""
            cursor.execute("select name from food where id = ? ", food_id)
            ans = ""
            for r in cursor:
                ans = r[0]
                break
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_food_name_by_id----")
            print(ex)
            return ""

    def get_role_id_by_name(self, role_name):
        try:
            cursor = self.func
            if not self.check_existed_id("Role", role_name):
                return ""
            cursor.execute("select id from Role where role_name = ? ", role_name)
            ans = ""
            for r in cursor:
                ans = r[0]
                break
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_role_id_name_by_name----")
            print(ex)
            return ""

    def get_id_order_by_time_staff_id(self, time, staff_id):
        try:
            cursor = self.func
            if not self.check_existed_id("Staff", staff_id):
                return ""
            cursor.execute("select id from CustomerOrder where order_time = ? and staff_id = ?", time, staff_id)
            ans = ""
            for r in cursor:
                ans = r[0]
                break
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_id_order_by_time_staff_id----")
            print(ex)
            return ""

    def get_id_order_by_time_customer_id(self, time, customer_id):
        try:
            cursor = self.func
            if not self.check_existed_id("Customer", customer_id):
                return ""
            cursor.execute("select id from CustomerOrder where order_time = ? and customer_id = ?", time, customer_id)
            ans = ""
            for r in cursor:
                ans = r[0]
                break
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_id_order_by_time_customer_id----")
            print(ex)
            return ""

    def get_menu_in_session_day(self, day, session):
        try:
            ans = []
            time = ck.get_time_from_session(session)
            time_check = day + " " + time
            cursor = self.func
            cursor.execute("select id from menu where time_start <= ? and time_end >= ?", time_check, time_check)
            menu_id = ""
            for row in cursor:
                menu_id = row[0]
                break
            cursor.execute("select food_id from MenuDetail where menu_id = ?", menu_id)
            list_food_id = []
            for food in cursor:
                list_food_id.append(food[0])
            for food_id in list_food_id:
                ans.append(self.get_info_food_by_id(food_id))
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_menu_in_session_day")
            print(ex)
            return []


"""Testing"""
sql_func = SqlFunction()
# print(sql_func.get_id_card('KH006'))
# print(sql_func.reset_password_staff('Taideeptry2', '198299328', '0987287188', 'conAiDepTraiHonTai1'))
# print(sql_func.reset_password_customer('gamelade', '198738192', '0918231231', 'gggTai1234'))
# print(sql_func.get_id_person_from_user('gamelade', 0))
# print(sql_func.insert_person('KH006', 'Nguyễn Quốc Thắng', 'Nam', '123123123', '20150503', '0987654432', 'Quận 9'))
# print(sql_func.insert_customer('KH005', 'No'))
# print(sql_func.insert_customer_user("mumumu", "mumumu123A", "KH005"))
# print(sql_func.get_all_info_customer())
# print(sql_func.get_info_all_staff())
# print(sql_func.get_info_menu_detail(2))
# print(sql_func.insert_menu("2021-04-11 20:06:00", "2021-04-11 06:06:00"))
# print(sql_func.insert_food("1412222", "Bánh abc", "Test 3, mô tả sau", 20000,
#                            "https://drive.google.com/file/d/1wK-NZkD33_ZqxlKzWBGCodfGbs-xQaRi/view?usp=sharing"))
# print(sql_func.insert_staff("90000", "Nguyễn Thị Hoa", "197406988", "2000-03-21", "0940123334", "Quận 12"))
# print(sql_func.insert_bill("9900022", "2021-03-21 10:30:00", 1, "9191919"))
# print(sql_func.insert_role("4", "Nhân viên vệ sinh"))
# print(sql_func.insert_user_login("9191919", "ggggg", "4"))
# ok
# print(sql_func.check_existed_id("menu", "123444"))
# print(sql_func.delete_function("menu", "id", "127800"))
# print(sql_func.update_menu("123444", "2021-11-17 19:30:00"))
# print(sql_func.update_food("1412222", "Bánh hỏi", "update", 25000,
#                            "https://drive.google.com/file/d/1wK-NZkDh2_ZqxlKzWBGCodfGbs-xQaRi/view?usp=sharing"))
# print(sql_func.update_staff("9191919", "Nguyễn Đình Trung", "198293812", "2000-03-21", "0908969231", "Quận Thủ Đức"))
#
# print(ck.check_date("2016-02-29"))
# print(ck.check_format_datetime("1996-02-29 24:59:08"))
# print(ck.check_format_datetime("1998-01-28"))
# print(ck.check_hms("23:65:03"))
# print(ck.convert_date("20/03/2020 15:03:05"))
# print(sql_func.get_pass_of_staff("9191919"))
# print(sql_func.check_login_staff('9191919', 'ggggg'))
# print(sql_func.check_existed_id('staff', '9191919'))
# print(np.random.permutation(10))
# print(sql_func.get_info_customer_by_id("KH001"))
# print(sql_func.get_all_info_customer())
# print(sql_func.get_info_all_staff())
# print(sql_func.get_info_staff_by_id('NV002'))
# print(sql_func.add_food_to_menu('123444', '12311'))
# print(sql_func.add_food_to_menu('12671', '141'))
# for i in range(0, 10):
#     print(sql_func.insert_food("Bánh xèo", "test" + str(i), 19000 + 1000 * i))
# print(sql_func.select_food_to_menu(123, 10))
# print(sql_func.get_info_menu_detail(2))
# print("select * from {} where id = {}".format("MenuDetail", '123'))
# Id ở Role, Menu, Food và customer order nên để tự tăng
# print(sql_func.calculate_order_id(2))
# print(sql_func.stats_order_revenue())
# print(sql_func.stats_revenue_by_month())
# print(sql_func.last_id_person(0))
# print(sql_func.get_info_order_detail_by_id(2))
# print(sql_func.get_all_info_order(1))
# print(sql_func.get_all_food())
# print(sql_func.get_id_order_by_time_customer_id('2021-04-12 19:34:00', 'KH005'))
# print(sql_func.get_id_person_from_user('admin', 1))
# print(sql_func.get_info_staff_by_id(sql_func.get_id_person_from_user('admin', 1)))
# for i in [1, 4, 2, 6, 10, 14, 15, 20, 22, 23, 24, 27, 29, 30, 8]:
#     sql_func.insert_menu_detail(11, i)
# print(sql_func.get_menu_in_session_day("2021-04-12", "Chiều"))
# print(sql_func.stats_revenue_by_day('2021-04-12'))
# print(sql_func.generate_new_id_person(0))
# print(sql_func.get_all_order_by_cus_id('KH001'))
# print(sql_func.delete_function("Food", "id", 31))
# print(sql_func.get_user_from_id("NV00", 1))

