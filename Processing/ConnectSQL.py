import pyodbc
import numpy as np
import Processing.CheckValid as ck

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
            if tablename.lower() == 'userlogin':
                cursor.execute("select * from {} where userid = ?".format(tablename), idb)
            elif tablename.lower() == 'orderdetail':
                cursor.execute("select * from {} where orderid = ?".format(tablename), idb)
            elif tablename.lower() == 'menudetail':
                cursor.execute("select * from {} where menuid = ?".format(tablename), idb)
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
        cursor.execute("select password from userlogin where userid = ?", ids)
        ans = ""
        for i in cursor:
            ans = i
        if ans != "":
            return ans[0]
        else:
            return "Empty"

    def insert_menu(self, idm, date):
        try:
            if self.check_existed_id("menu", idm):
                return False
            if not ck.check_format_datetime(date):
                return False
            cursor = self.func
            cursor.execute(
                'insert into Menu values (?, ?);',
                (idm, date)
            )
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in insert_menu----')
            print(ex)
            return False

    def insert_food(self, idf, name, des, price, img=""):
        try:
            if self.check_existed_id("food", idf):
                return False
            cursor = self.func
            cursor.execute(
                'insert into food values (?, ?, ?, ?, ?);',
                (idf, name, des, price, img)
            )
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in insert food----')
            print(ex)
            return False

    def insert_staff(self, ids, name, id_card, dob, phone, addr):
        try:
            if self.check_existed_id("staff", ids):
                return False
            cursor = self.func
            cursor.execute(
                'insert into staff values (?, ?, ?, ?, ?, ?);',
                (ids, name, id_card, dob, phone, addr)
            )
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in insert_staff----')
            print(ex)
            return False

    def insert_bill(self, idb, time, stt, stid):
        try:
            if self.check_existed_id("Customer_Order", idb):
                return False
            if not self.check_existed_id("Staff", stid):
                return False
            if not ck.check_format_datetime(time):
                return False
            cursor = self.func
            cursor.execute(
                'insert into Customer_Order values (?, ?, ?, ?);',
                (idb, time, stt, stid)
            )
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in insert_bill----')
            print(ex)
            return False

    def insert_role(self, role_id, role_name):
        try:
            if self.check_existed_id("Role", role_id):
                return False
            cursor = self.func
            cursor.execute("insert into Role values (?, ?);", (role_id, role_name))
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in insert_role----')
            print(ex)
            return False

    def insert_user_login(self, ids, password, role_id):
        try:
            if not self.check_existed_id("staff", ids):
                return False
            if self.check_existed_id("userlogin", ids):
                return False
            if not self.check_existed_id("Role", role_id):
                return False
            cursor = self.func
            cursor.execute("insert into UserLogin values (?, ?, ?);", (ids, password, role_id))
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error insert_user_logic----')
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

    def update_menu(self, idm, date):
        try:
            if not self.check_existed_id("menu", idm):
                return False
            if not ck.check_format_datetime(date):
                return False
            cursor = self.func
            cursor.execute(
                'update Menu set time_now = ? where id = ?',
                (date, idm)
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

    def update_staff(self, ids, name, id_card=None, dob=None, phone=None, addr=None):
        try:
            if not self.check_existed_id("staff", ids):
                return False
            cursor = self.func
            cursor.execute(
                'update staff set staff_name = ?, identity_card = ?, day_of_birth = ?,'
                ' phone_num = ?, address = ? where id = ?;',
                (name, id_card, dob, phone, addr, ids)
            )
            cursor.commit()
            return True
        except Exception as ex:
            print('----Error in update_staff----')
            print(ex)
            return False

    def check_login_staff(self, ids, passw):
        try:
            if not self.check_existed_id("userlogin", ids):
                return False
            else:
                if passw == self.get_pass_of_staff(ids):
                    return True
                else:
                    return False
        except Exception as ex:
            print('----Error in check_login_staff----')
            print(ex)
            return False

    def get_info_staff_by_id(self, ids):
        try:
            if self.check_existed_id("staff", ids):
                cursor = self.func
                sql = "select staff_name, identity_card, day_of_birth, phone_num, address, role_name, " \
                      "password from staff, " \
                      "UserLogin, role where role.id = UserLogin.roleid and UserLogin.userid = Staff.id " \
                      "and staff.id = ?"
                cursor.execute(sql, ids)
                ans = []
                ans.append(ids)
                for row in cursor:
                    ans.append(row[0])
                    ans.append(row[1])
                    ans.append(row[2])
                    ans.append(row[3])
                    ans.append(row[4])
                    ans.append(row[5])
                    ans.append(row[6])
                    break
                cursor.commit()
                return ans
            else:
                print("Id staff not existed in get_info_staff_by_id")
                return False
        except Exception as ex:
            print("----Error in get_info_staff_by_id----")
            print(ex)
            return False

    def add_food_to_menu(self, menuid, foodid):
        try:
            if self.check_existed_id("menu", menuid) and self.check_existed_id("food", foodid):
                cursor = self.func
                cnt = 0
                cursor.execute('select * from MenuDetail where menuid = ? and foodid = ?', menuid, foodid)
                for _ in cursor:
                    cnt += 1
                    break
                if cnt == 0:
                    cursor.execute('insert into MenuDetail values (?, ?)', menuid, foodid)
                    cursor.commit()
                    return True
                else:
                    print('Food existed in menu, don\'t need add')
                    cursor.commit()
                    return False
            else:
                print('No existed menuid or foodid in add_food_to_menu')
                return False
        except Exception as ex:
            print("----Error in add_food_to_menu----")
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

    def select_food_to_menu(self, menu_id, num_food_in_menu):
        """
        :param menu_id:<string> id of menu need to add food
        :param num_food_in_menu:<int> the number of food need to add in this menu
        :return: True if add success else False
        """
        try:
            arr = np.random.permutation(20)
            arr = arr[:num_food_in_menu]
            for i in arr:
                food = self.all_food()[i]
                self.add_food_to_menu(menu_id, food[0])
            return True
        except Exception as ex:
            print('----Error in select_food_to_menu----')
            print(ex)
            return False

    def get_info_menu_detail(self, menu_id):
        try:
            cursor = self.func
            if not self.check_existed_id("MenuDetail", menu_id):
                return []
            cursor.execute("select name, describe, price, img from Food, MenuDetail "
                           "where food.id = menudetail.foodid and menudetail.menuid = ?", menu_id)
            ans = []
            for r in cursor:
                ans.append(r)
            cursor.commit()
            return ans
        except Exception as ex:
            print("----Error in get_info_menu_detail----")
            print(ex)
            return []


"""Testing"""
sql_func = SqlFunction()
# print(sql_func.insert_menu("127800", "2020-08-15 04:06:00"))
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
print(sql_func.get_info_staff_by_id("9191919"))
# print(sql_func.add_food_to_menu('123444', '12311'))
# print(sql_func.add_food_to_menu('12671', '141'))
# for i in range(0, 20):
#     print(sql_func.insert_food("123" + str(i), "Bánh xèo", "test" + str(i), 19000 + 1000 * i))
# print(sql_func.select_food_to_menu(123, 10))
# print(sql_func.get_info_menu_detail('123'))
# print("select * from {} where id = {}".format("MenuDetail", '123'))
# Id ở Role, Menu, Food và customer order nên để tự tăng
