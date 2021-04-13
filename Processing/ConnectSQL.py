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

    def insert_person(self, ids, name, gender, id_card, dob, phone, addr):
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

    def insert_customer_order(self, time, stt, stid, cus_id=None):
        try:
            if not ck.check_limit_time(time):
                return False
            if not self.check_existed_id("Staff", stid):
                return False
            if not ck.check_format_datetime(time):
                return False
            cursor = self.func
            cursor.execute(
                'insert into CustomerOrder values (?, ?, ?, ?);',
                (time, stt, stid, cus_id)
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

    def update_user_login(self, user_id, password, role_id):
        try:
            if not self.check_existed_id("userlogin", user_id):
                return False
            if not self.check_existed_id("Role", role_id):
                return False
            if not ef.check_regex_password(password):
                return False
            cursor = self.func
            cursor.execute("update UserLogin set password = ?, role_id = ? "
                           "where user_id = ?", (password, role_id, user_id))
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error insert_user_logic----')
            print(ex)
            return False

    def update_customer_user(self, user_id, password):
        try:
            if not self.check_existed_id("CustomerUser", user_id):
                return False
            if ef.check_regex_password(password):
                return False
            cursor = self.func
            cursor.execute("update CustomerUser set password = ? where user_id = ?;", (password, user_id))
            cursor.commit()
            return True
        except Exception as ex:
            print("----Error in insert_customer_user")
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
        [staff_id, name, gender, identity_card, day_of_birth, phone_num, address, role_name, salary, password]
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
                    ans.append(float(row[8]))
                    ans.append(row[9])
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
        [staff_id, name, gender, identity_card, day_of_birth, phone_num, address, role_name, salary, password]
        """
        try:
            cursor = self.func
            sql = "select * from dbo.SelectAllInfoStaff()"
            rows = cursor.execute(sql)
            ans = []
            for row in rows:
                tmp = [row[0], row[1], row[2], row[3], str(row[4]), row[5], row[6], row[7], float(row[8]), row[9]]
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
        [customer_id, name, gender, identity_card, day_of_birth, phone_num, address, vip_member, password]
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
                    ans.append(row[8])
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
        [customer_id, name, gender, identity_card, day_of_birth, phone_num, address, vip_member, password]
        """
        try:
            cursor = self.func
            sql = "select * from dbo.SelectAllInfoCustomer()"
            cursor.execute(sql)
            ans = []
            for row in cursor:
                tmp = [row[0], row[1], row[2], row[3], str(row[4]), row[5], row[6], row[7], row[8]]
                ans.append(tmp)
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_all_info_customer----")
            print(ex)
            return False

    def all_food(self):
        try:
            cursor = self.func
            cursor.execute("select * from food")
            list_food = []
            for r in cursor:
                list_food.append(r)
            return list_food
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
                tmp = [r[0], float(r[1]), str(r[3]), ef.status_type(r[4]), r[5], r[6]]
                ans.append(tmp)
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in stats_order_revenue----")
            print(ex)
            return False

    def stats_revenue_by_month(self):
        try:
            cursor = self.func
            cursor.execute("select * from dbo.StatsRevenueByMonth()")
            ans = []
            for r in cursor:
                tmp = [r[0], float(r[1])]
                ans.append(tmp)
            cursor.commit()
            return ans
        except Exception as ex:
            print('----Error in stats_revenue_by_month')
            print(ex)
            return False


"""Testing"""
sql_func = SqlFunction()
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
# print(ck.check_format_datetime("1998-01-28 15:05:08"))
# print(ck.check_format_datetime("1998-01-28"))
# print(ck.check_hms("23:65:03"))
# print(ck.convert_date("20/03/2020 15:03:05"))
# print(sql_func.get_pass_of_staff("9191919"))
# print(sql_func.check_login_staff('9191919', 'ggggg'))
# print(sql_func.check_existed_id('staff', '9191919'))
# print(np.random.permutation(10))
# print(sql_func.get_info_customer_by_id("KH001"))
# print(sql_func.add_food_to_menu('123444', '12311'))
# print(sql_func.add_food_to_menu('12671', '141'))
# for i in range(0, 20):
#     print(sql_func.insert_food("Bánh xèo", "test" + str(i), 19000 + 1000 * i))
# print(sql_func.select_food_to_menu(123, 10))
# print(sql_func.get_info_menu_detail(2))
# print("select * from {} where id = {}".format("MenuDetail", '123'))
# Id ở Role, Menu, Food và customer order nên để tự tăng
# print(sql_func.calculate_order_id(2))
# print(sql_func.stats_order_revenue())
# print(sql_func.stats_revenue_by_month())
