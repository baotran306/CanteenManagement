from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import ConnectSQL
import CheckValidTime
connect = ConnectSQL.SqlFunction()

app = Flask(__name__)
CORS(app)


@app.route("/staff", methods=['GET'])
def get_all_staff():
    rows = connect.get_info_all_staff()
    data = []
    for r in rows:
        data.append({
            'id': r[0],
            'name': r[1],
            'gender': r[2],
            'identity_card': r[3],
            'day_of_birth': r[4],
            'phone_num': r[5],
            'address': r[6],
            'role_name': r[7],
            'salary': r[8]
        })
    return jsonify(data)


@app.route("/staff/<string:staff_id>", methods=['GET'])
def get_staff_by_id(staff_id):
    row = connect.get_info_staff_by_id(staff_id)
    data = {
        'id': row[0],
        'name': row[1],
        'gender': row[2],
        'identity_card': row[3],
        'day_of_birth': row[4],
        'phone_num': row[5],
        'address': row[6],
        'role_name': row[7],
        'salary': row[8]
    }
    return jsonify(data)


@app.route("/customer", methods=['GET'])
def get_info_customer():
    rows = connect.get_all_info_customer()
    data = []
    for r in rows:
        data.append({
            'id': r[0],
            'name': r[1],
            'gender': r[2],
            'identity_card': r[3],
            'day_of_birth': r[4],
            'phone_num': r[5],
            'address': r[6],
            'vip': r[7]
        })
    return jsonify(data)


@app.route("/customer/<string:customer_id>", methods=['GET'])
def get_info_customer_by_id(customer_id):
    info = connect.get_info_customer_by_id(customer_id)
    data = {
        'id': info[0],
        'name': info[1],
        'gender': info[2],
        'identity_card': info[3],
        'day_of_birth': info[4],
        'phone_num': info[5],
        'address': info[6],
        'vip': info[7]
    }
    return jsonify(data)


@app.route("/admin/stats/order", methods=['GET'])
def stats_order_revenue():
    rows = connect.stats_order_revenue()
    data = []
    for r in rows:
        data.append({
            'order_id': r[0],
            'total': r[1],
            'order_time': r[2],
            'status_now': r[3],
            'staff_id': r[4],
            'address': r[5],
            'customer_id': r[6]
        })
    return jsonify(data)


@app.route("/admin/stats/month/<int:year>", methods=['GET'])
def stats_revenue_by_month(year):
    rows = connect.stats_revenue_by_month(year)
    data = []
    for r in rows:
        data.append({
            'month': r[0],
            'revenue': r[1]
        })
    return jsonify(data)


@app.route("/admin/stats/day", methods=['POST'])
def stats_revenue_by_day():
    day = request.json['day']
    info = connect.stats_revenue_by_day(day)
    data = {'day': info[0], 'revenue': info[1], 'num_success': info[2], 'percent_success': info[3]}
    return jsonify(data)


@app.route("/customer/stats/<string:customer_id>", methods=['GET'])
def stats_order_by_customer(customer_id):
    info = connect.get_all_order_by_cus_id(customer_id)
    data = []
    for r in info:
        data.append({
            'id_order': r[0],
            'food': r[1],
            'num_of_food': r[2],
            'price': r[3],
            'total': r[4],
            'order_time': r[5],
            'status': r[6],
            'address': r[7],
            'name_customer': r[8]
        })
    return jsonify(data)


@app.route("/admin/stats/all_order", methods=['GET'])
def get_all_order():
    rows = connect.get_all_info_order(4)
    data = []
    for r in rows:
        data.append({
            'id_order': r[0],
            'food': r[1],
            'num_of_food': r[2],
            'price': r[3],
            'total': r[4],
            'order_time': r[5],
            'status': r[6],
            'address': r[7],
            'name_customer': r[8]
        })
    return jsonify(data)


@app.route("/admin/all_food", methods=['GET'])
def get_all_food():
    rows = connect.get_all_food()
    data = []
    for r in rows:
        data.append({
            'id_food': r[0],
            'food_name': r[1],
            'describe': r[2],
            'cur_price': r[3],
            'image': r[4]
        })
    return jsonify(data)


@app.route("/admin/menu/detail", methods=['POST'])
def get_food_menu_detail():
    session = request.json['session']
    day = request.json['day']
    menu_id = connect.get_id_menu_by_session_day(day, session)
    list_food = connect.get_info_menu_detail(menu_id)
    list_id = []
    for food in list_food:
        list_id.append(food[0])
    data = {
        'id_food': list_id
        # 'food_name': r[1],
        # 'describe': r[2],
        # 'cur_price': r[3],
        # 'image': r[4]
    }
    return jsonify(data)


@app.route("/admin/stats/not_complete_order", methods=['GET'])
def get_not_complete_order():
    rows = connect.get_all_info_order(0)
    data = []
    for r in rows:
        data.append({
            'id_order': r[0],
            'food': r[1],
            'num_of_food': r[2],
            'price': r[3],
            'total': r[4],
            'order_time': r[5],
            'status': r[6],
            'address': r[7],
            'name_customer': r[8]
        })
    return jsonify(data)


@app.route("/admin/stats/delivering_order", methods=['GET'])
def get_delivering_order():
    rows = connect.get_all_info_order(2)
    data = []
    for r in rows:
        data.append({
            'id_order': r[0],
            'food': r[1],
            'num_of_food': r[2],
            'price': r[3],
            'total': r[4],
            'order_time': r[5],
            'status': r[6],
            'address': r[7],
            'name_customer': r[8]
        })
    return jsonify(data)


@app.route("/admin/stats/completed_order", methods=['GET'])
def get_completed_order():
    rows = connect.get_all_info_order(1)
    data = []
    for r in rows:
        data.append({
            'id_order': r[0],
            'food': r[1],
            'num_of_food': r[2],
            'price': r[3],
            'total': r[4],
            'order_time': r[5],
            'status': r[6],
            'address': r[7],
            'name_customer': r[8]
        })
    return jsonify(data)


@app.route("/admin/stats/cancel_order", methods=['GET'])
def get_cancel_order():
    rows = connect.get_all_info_order(3)
    data = []
    for r in rows:
        data.append({
            'id_order': r[0],
            'food': r[1],
            'num_of_food': r[2],
            'price': r[3],
            'total': r[4],
            'order_time': r[5],
            'status': r[6],
            'address': r[7],
            'name_customer': r[8]
        })
    return jsonify(data)


@app.route("/customer/register", methods=['POST'])
def insert_customer():
    new_id = connect.generate_new_id_person(1)
    name = request.json['name']
    gender = request.json['gender']
    id_card = request.json['id_card']
    dob = request.json['dob']
    phone = request.json['phone']
    address = request.json['address']
    user = request.json['user']
    password = request.json['password']
    if connect.check_existed_id("CustomerUser", user):
        data = {'result': False, 'error': 'Đăng kí thất bại'}
        return jsonify(data)
    if connect.insert_person(new_id, name, gender, id_card, dob, phone, address):
        if connect.insert_customer(new_id, vip="NO"):
            if connect.insert_customer_user(user, password, new_id):
                data = {'result': True, 'error': 'Đăng kí thành công'}
                return jsonify(data)
    data = {'result': False, 'error': 'Đăng kí thất bại'}
    return jsonify(data)


@app.route("/admin/register", methods=['POST'])
def insert_staff():
    new_id = connect.generate_new_id_person(0)
    name = request.json['name']
    gender = request.json['gender']
    id_card = request.json['id_card']
    dob = request.json['dob']
    phone = request.json['phone']
    address = request.json['address']
    user = request.json['user']
    password = request.json['password']
    role_name = request.json['role_name']
    role_id = connect.get_role_id_by_name(role_name)
    if connect.check_existed_id("UserLogin", user):
        data = {'result': False, 'error': 'Đăng kí thất bại'}
        return jsonify(data)
    if connect.insert_person(new_id, name, gender, id_card, dob, phone, address):
        if connect.insert_staff(new_id):
            if connect.insert_user_login(user, password, role_id, new_id):
                data = {'result': True, 'error': 'Đăng kí nhân viên thành công'}
                return jsonify(data)
    data = {'result': False, 'error': 'Đăng kí thất bại'}
    return jsonify(data)


@app.route("/admin/food", methods=['POST'])
def insert_food():
    name = request.json['name']
    describe = request.json['describe']
    price = request.json['price']
    image = request.json['image']
    if connect.insert_food(name, describe, price, image):
        data = {'result': True, 'error': 'Thêm món mới thành công'}
        return jsonify(data)
    data = {'result': False, 'error': 'Thêm thất bại'}
    return jsonify(data)


@app.route("/admin/menu", methods=['POST'])
def insert_menu():
    time_start = request.json['time_start']
    time_end = request.json['time_end']
    if connect.insert_menu(time_start, time_end):
        data = {'result': True, 'error': 'Thêm thực đơn thành công'}
        return jsonify(data)
    data = {'result': False, 'error': 'Thêm thất bại'}
    return jsonify(data)


@app.route("/admin/update/menu/detail", methods=['POST'])
def update_menu_detail():
    session = request.json['session']
    day = request.json['day']
    menu_id = connect.get_id_menu_by_session_day(day, session)
    list_food = request.json['list_food']
    if menu_id == "":
        time = CheckValidTime.get_start_end_time_session(session)
        time_start = day + " " + time[0]
        time_end = day + " " + time[1]
        connect.insert_menu(time_start, time_end)
        menu_id = connect.get_id_menu_by_session_day(day, session)
    else:
        connect.delete_function("MenuDetail", "menu_id", menu_id)
    check = False
    for i in range(len(list_food)):
        if connect.insert_menu_detail(menu_id, int(list_food[i])):
            check = True
        else:
            break
    if check:
        data = {'result': True, 'error': 'Cập nhật menu thành công', 'list_food': list_food}
        return jsonify(data)
    data = {'result': False, 'error': 'Cập nhật menu thất bại'}
    return jsonify(data)


@app.route("/staff/order", methods=['POST'])
def insert_order_off():
    time_now = str(datetime.now())
    time_now, _ = time_now.split('.')
    staff_id = request.json['staff_id']
    if connect.insert_customer_order(time_now, 1, staff_id, "Tại chỗ", None):
        id_order = connect.get_id_order_by_time_staff_id(time_now, staff_id)
        # use loop to add menu food in order
        food_id = request.json['food_id']
        num_food = request.json['num_food']
        cur_price = request.json['cur_price']
        check = False
        for i in range(len(food_id)):
            if connect.insert_order_detail(id_order, food_id[i], num_food[i], cur_price[i]):
                check = True
            else:
                break
        if check:
            data = {'result': True, 'error': 'Thêm hóa đơn thành công'}
            return jsonify(data)
    data = {'result': False, 'error': 'Thêm thất bại'}
    return jsonify(data)


@app.route("/customer/order", methods=['POST'])
def insert_order_onl():
    time_now = str(datetime.now())
    time_now, _ = time_now.split('.')
    address = request.json['address']
    customer_id = request.json['customer_id']
    if connect.insert_customer_order(time_now, 0, 'NV00', address, customer_id):
        id_order = connect.get_id_order_by_time_customer_id(time_now, customer_id)
        # use loop to add menu food in order
        food_id = request.json['food_id']
        num_food = request.json['num_food']
        cur_price = request.json['cur_price']
        check = False
        for i in range(len(food_id)):
            if connect.insert_order_detail(id_order, food_id[i], num_food[i], cur_price[i]):
                check = True
            else:
                check = False
        if check:
            data = {'result': True, 'error': 'Thêm hóa đơn thành công'}
            return jsonify(data)
    data = {'result': False, 'error': 'Thêm thất bại'}
    return jsonify(data)


@app.route("/customer/login", methods=['POST'])
def login_customer():
    user = request.json['user']
    password = request.json['password']
    if connect.check_login_customer(user, password):
        id_cus = connect.get_id_person_from_user(user, 0)
        info_cus = connect.get_info_customer_by_id(id_cus)
        data = {'result': True, 'id': info_cus[0], 'name': info_cus[1], 'vip': info_cus[7]}
        return jsonify(data)
    else:
        data = {'result': False, 'error': "Tài khoản hoặc mật khẩu không chính xác"}
        return jsonify(data)


@app.route("/staff/login", methods=['POST'])
def login_staff():
    user = request.json['user']
    password = request.json['password']
    if connect.check_login_staff(user, password):
        id_staff = connect.get_id_person_from_user(user, 1)
        info_staff = connect.get_info_staff_by_id(id_staff)
        data = {'result': True, 'id': info_staff[0], 'name': info_staff[1], 'role': info_staff[7]}
        return jsonify(data)
    else:
        data = {'result': False, 'error': "Tài khoản hoặc mật khẩu không chính xác"}
        return jsonify(data)


@app.route("/customer/change_password", methods=['POST'])
def change_password_customer():
    user = request.json['user']
    old_pass = request.json['old_pass']
    new_pass = request.json['new_pass']
    if connect.check_login_customer(user, old_pass):
        if connect.update_customer_user_password(user, new_pass):
            data = {'result': True, 'error': 'Thay đổi mật khẩu thành công!'}
            return jsonify(data)
        else:
            data = {'result': False, 'error': 'Thay đổi mật khẩu thất bại!'}
            return jsonify(data)
    data = {'result': False, 'error': 'Thay đổi mật khẩu thất bại!'}
    return jsonify(data)


@app.route('/staff/change_password', methods=['POST'])
def change_password_staff():
    user = request.json['user']
    old_pass = request.json['old_pass']
    new_pass = request.json['new_pass']
    if connect.check_login_staff(user, old_pass):
        if connect.update_user_login_password(user, new_pass):
            data = {'result': True, 'error': 'Thay đổi mật khẩu thành công!'}
            return jsonify(data)
        else:
            data = {'result': False, 'error': 'Thay đổi mật khẩu thất bại!'}
            return jsonify(data)
    data = {'result': False, 'error': 'Thay đổi mật khẩu thất bại!'}
    return jsonify(data)


@app.route('/customer/reset_password', methods=['POST'])
def reset_password_customer():
    user = request.json['user']
    id_card = request.json['id_card']
    phone = request.json['phone']
    new_pass = request.json['new_pass']
    if connect.reset_password_customer(user, id_card, phone, new_pass):
        data = {'result': True, 'error': 'Thay đổi mật khẩu thành công!'}
        return jsonify(data)
    data = {'result': False, 'error': 'Thay đổi mật khẩu thất bại!'}
    return jsonify(data)


@app.route('/staff/reset_password', methods=['POST'])
def reset_password_staff():
    user = request.json['user']
    id_card = request.json['id_card']
    phone = request.json['phone']
    new_pass = request.json['new_pass']
    if connect.reset_password_staff(user, id_card, phone, new_pass):
        data = {'result': True, 'error': 'Thay đổi mật khẩu thành công!'}
        return jsonify(data)
    data = {'result': False, 'error': 'Thay đổi mật khẩu thất bại!'}
    return jsonify(data)


def get_menu_detail(day, session):
    info = connect.get_menu_in_session_day(day, session)
    if len(info) == 0:
        data = {'result': False, 'error': 'Menu không tồn tại'}
        return data
    id_food = []
    food_name = []
    description = []
    food_price = []
    picture = []
    for row in info:
        id_food.append(row[0])
        food_name.append(row[1])
        description.append(row[2])
        food_price.append(row[3])
        picture.append(row[4])
    data = {'result': True, 'id': id_food, 'food_name': food_name,
            'description': description, 'food_price': food_price, 'picture': picture}
    return data


@app.route("/admin/menu/breakfast", methods=['POST'])
def menu_breakfast():
    day_b_now = request.json['day']
    session_b_now = request.json['session']
    return jsonify(get_menu_detail(day_b_now, session_b_now))


@app.route("/admin/menu/lunch", methods=['POST'])
def menu_lunch():
    day_l_now = request.json['day']
    session_l_now = request.json['session']
    return jsonify(get_menu_detail(day_l_now, session_l_now))


@app.route("/admin/menu/dinner", methods=['POST'])
def menu_dinner():
    day_d_now = request.json['day']
    session_d_now = request.json['session']
    return jsonify(get_menu_detail(day_d_now, session_d_now))


@app.route("/admin/manage/food/<int:food_id>", methods=['DELETE'])
def delete_food(food_id):
    if connect.delete_function("Food", "id", food_id):
        data = {'result': True, 'error': 'Đã xóa món ăn thành công'}
        return jsonify(data)
    data = {'result': False, 'error': 'Món ăn đã tồn tại trong Menu, không thể xóa'}
    return jsonify(data)


@app.route("/admin/manage/menu/<int:menu_id>", methods=['DELETE'])
def delete_menu(menu_id):
    if connect.delete_function("Menu", "id", menu_id):
        data = {'result': True, 'error': 'Đã xóa Menu thành công'}
        return jsonify(data)
    data = {'result': False, 'error': 'Menu chứa món ăn, không thể xóa'}
    return jsonify(data)


@app.route("/admin/manage/staff/<string:staff_id>", methods=['DELETE'])
def delete_staff(staff_id):
    if connect.check_existed_foreign_key_order(staff_id, 1):
        connect.delete_function("UserLogin", "staff_id", staff_id)
        connect.delete_function("Staff", "id", staff_id)
        connect.delete_function("Person", "id", staff_id)
        data = {'result': True, 'error': 'Xóa nhân viên thành công'}
        return jsonify(data)
    data = {'result': False, 'error': 'Nhân viên đã từng lập hóa đơn, không thể xóa'}
    return jsonify(data)


@app.route("/admin/manage/customer/<string:customer_id>", methods=['DELETE'])
def delete_customer(customer_id):
    if connect.check_existed_foreign_key_order(customer_id, 0):
        connect.delete_function("UserLogin", "staff_id", customer_id)
        connect.delete_function("Staff", "id", customer_id)
        connect.delete_function("Person", "id", customer_id)
        data = {'result': True, 'error': 'Xóa khách hàng thành công'}
        return jsonify(data)
    data = {'result': False, 'error': 'Khách hàng đã từng lập hóa đơn, không thể xóa'}
    return jsonify(data)


@app.route("/admin/manage/update/food/update", methods=['POST'])
def update_food():
    id_food = request.json['foodId']
    name = request.json['foodName']
    des = request.json['foodDescription']
    img = request.json['foodImg']
    price = request.json['foodPrice']
    if img == "":
        info = connect.get_info_food_by_id(id_food)
        img = info[4]
        if connect.update_food(id_food, name, des, price, img):
            data = {'result': True, 'error': 'Cập nhật thành công'}
            return jsonify(data)
    else:
        if connect.update_food(id_food, name, des, price, img):
            data = {'result': True, 'error': 'Cập nhật thành công'}
            return jsonify(data)
    data = {'result': False, 'error': 'Cập nhật thất bại'}
    return jsonify(data)


@app.route("/admin/manage/update/staff", methods=['POST'])
def update_staff():
    id_staff = request.json['staff_id']
    role_name = request.json['role_name']
    user_staff = connect.get_user_from_id(id_staff, 1)
    role_id = connect.get_role_id_by_name(role_name)
    staff_salary = request.json['staff_salary']
    if user_staff != "" and role_id != "":
        if connect.update_user_login_role(user_staff, role_id)\
                and connect.update_staff(id_staff, staff_salary):
            data = {'result': True, 'error': 'Cập nhật nhân viên thành công'}
            return jsonify(data)
        else:
            data = {'result': False, 'error': 'Cập nhật thất bại'}
            return jsonify(data)
    data = {'result': False, 'error': 'Có lỗi xảy ra, cập nhật thất bại'}
    return jsonify(data)


@app.route("/admin/manage/update/customer/vip", methods=['POST'])
def update_customer_type():
    customer_id = request.json['customer_id']
    customer_type = request.json['customer_type']
    if connect.update_customer(customer_id, customer_type):
        data = {'result': True, 'error': 'Cập nhật loại khách hàng thành công'}
        return jsonify(data)
    data = {'result': False, 'error': 'Cập nhật loại khách hàng thất bại'}
    return jsonify(data)


@app.route("/person/update/info", methods=['POST'])
def update_info_person():
    # customer and staff are similar format info
    id_cus = request.json['id']
    name = request.json['name']
    gender = request.json['gender']
    id_card = request.json['id_card']
    dob = request.json['dob']
    phone = request.json['phone']
    address = request.json['address']
    if connect.update_person(id_cus, name, gender, id_card, dob, phone, address):
        data = {'result': True, 'error': 'Cập nhật thông tin thành công'}
        return jsonify(data)
    data = {'result': False, 'error': 'Cập nhật thông tin thất bại'}
    return jsonify(data)


@app.route("/shipper/manage/order", methods=['POST'])
def shipper_change_status_order():
    check_complete = False
    status = request.json['status']
    id_order = request.json['id_order']
    id_staff = request.json['id_staff']
    if status.lower() == "chưa giao":
        if connect.update_customer_order(id_order, "đang giao"):  # update status
            if connect.update_shipper(id_order, id_staff):  # update shipper who is delivering this order
                check_complete = True
    elif status.lower() == "đang giao":
        if connect.update_customer_order(id_order, "đã giao"):
            check_complete = True
    if check_complete:
        data = {'result': True, 'error': 'Đã cập nhật trạng thái'}
        return jsonify(data)
    data = {'result': False, 'error': 'Cập nhật trạng thái thất bại'}
    return jsonify(data)


@app.route("/shipper/manage/show/<string:id_staff>", methods=['GET'])
def get_shipper_order(id_staff):
    not_complete = connect.get_all_info_order(0)
    delivering = connect.get_delivering_order_by_shipper(id_staff)
    rows = not_complete + delivering
    data = []
    for r in rows:
        data.append({
            'id_order': r[0],
            'food': r[1],
            'num_of_food': r[2],
            'price': r[3],
            'total': r[4],
            'order_time': r[5],
            'status': r[6],
            'address': r[7],
            'name_customer': r[8]
        })
    return jsonify(data)


@app.route("/customer/manage/order/<int:id_order>", methods=['GET'])
def customer_change_status_order(id_order):
    if connect.update_customer_order(id_order, "hủy"):
        data = {'result': True, 'error': 'Đã cập nhật trạng thái'}
        return jsonify(data)
    data = {'result': False, 'error': 'Cập nhật trạng thái thất bại'}
    return jsonify(data)


if __name__ == "__main__":
    app.run(port=5000)
