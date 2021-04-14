import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-D7ND4M2H\SQLEXPRESS;"
    "Database=CanteenManagement;"
    "Trusted_Connection=yes;"
)


def check_existed_id(table, idx):
    cursor = conn.cursor()
    if table.lower() == 'userlogin':
        row = cursor.execute('select * from {} where userid = {}'.format(table, idx)).fetchall()
    else:
        row = cursor.execute('select * from {} where id = {}'.format(table, idx)).fetchall()
    cnt = 0
    for _ in row:
        cnt += 1
        break
    cursor.commit()
    if cnt == 0:
        return False
    else:
        return True


def get_all_info(table_name):
    print("Read")
    cursor = conn.cursor()
    res = cursor.execute(
        'select * from {}'.format(table_name)
    ).fetchall()
    # fetchall() lay tat ca, fetchone lay mot cai
    cursor.commit()
    ans = {}
    ls = []
    # for row in cursor:
    #     ls.append(row)pi
    # ans['staff'] = ls
    return res
# chay dc 

def get_info_staff():
    sql = 'select staff.id, staff_name, phone_num, address, password, role_name from staff, UserLogin, role ' \
          'where role.id = staff.roleid and UserLogin.userid = Staff.id'
    cursor = conn.cursor()
    res = cursor.execute(sql).fetchall()
    cursor.commit()
    return res


def get_password(ids):
    if check_existed_id('Staff', ids):
        cursor = conn.cursor()
        pas = cursor.execute('select password from UserLogin where userid = ?', ids).fetchone()
        cursor.commit()
        return pas[0]
    else:
        return False


if __name__ == "__main__":
    print(get_all_info("staff"))
    print(get_password('167'))
    print(check_existed_id('USERlogin', '155'))
    print(get_info_staff())
