import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=WINDOWS-A251ALV;"
    "Database=CanteenManagement;"
    "Trusted_Connection=yes;"
)


def add_menu(menu_id, date):
    try:
        cursor = conn.cursor()
        cursor.execute('insert into menu values (?, ?)', menu_id, date)
        cursor.commit()
    except Exception as ex:
        print(ex)
        return False
    return True


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
    cursor = conn.cursor()
    res = cursor.execute(
        'select * from {}'.format(table_name)
    ).fetchall()
    # fetchall() lay tat ca, fetchone lay mot cai
    cursor.commit()
    ans = {}
    ls = []
    # for row in cursor:
    #     ls.append(row)
    # ans['staff'] = ls
    return res


def get_info_staff():
    sql = 'select staff.id, staff_name, phone_num, address, password, role_name from staff, UserLogin, role ' \
          'where role.id = staff.roleid and UserLogin.userid = Staff.id'
    cursor = conn.cursor()
    res = cursor.execute(sql).fetchall()
    cursor.commit()
    return res


def get_info_staff_by_id(staff_id):
    sql = 'select staff.id, staff_name, phone_num, address, password, role_name from staff, UserLogin, role ' \
          'where role.id = staff.roleid and UserLogin.userid = Staff.id and staff.id = ?'
    cursor = conn.cursor()
    res = cursor.execute(sql, staff_id).fetchone()
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
    print(get_info_staff_by_id('12323'))
    print(add_menu('7777', '2021-03-06 23:45:05'))
