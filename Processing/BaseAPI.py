from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import Processing.ConnectSQL
connect = Processing.ConnectSQL.SqlFunction()

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


@app.route("/admin/menu_detail", methods=['POST'])
def insert_menu_detail(ls):
    # don't comple
    sign = False
    if connect.insert_menu_detail(ls[0], ls[1]):
        sign = True
    return jsonify(sign)


@app.route("/staff/order", methods=['POST'])
def insert_order_off():
    # don't complete
    time_now = str(datetime.now())
    time_now, _ = time_now.split('.')
    staff_id = request.json['staff_id']
    if connect.insert_customer_order(time_now, 1, staff_id, "Tại chỗ", None):
        id_order = connect.get_id_order_by_time_staff_id(time_now, staff_id)
        # use loop to add menu food in order
        food_name = request.json['food_name']
        num_food = request.json['num_food']
        cur_price = request.json['cur_price']
        if connect.insert_order_detail(id_order, food_name, num_food, cur_price):
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
        food_name = request.json['food_name']
        num_food = request.json['num_food']
        cur_price = request.json['cur_price']
        if connect.insert_order_detail(id_order, food_name, num_food, cur_price):
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
        return jsonify(data)
    else:
        data = {'result': False, 'info': info}
        return jsonify(data)


@app.route("/admin/menu/breakfast", methods=['POST'])
def menu_breakfast():
    day = request.json['day']
    session = request.json['session']
    return get_menu_detail(day, session)


@app.route("/admin/menu/lunch", methods=['POST'])
def menu_lunch():
    day = request.json['day']
    session = request.json['session']
    return get_menu_detail(day, session)


@app.route("/admin/menu/dinner", methods=['POST'])
def menu_dinner():
    day = request.json['day']
    session = request.json['session']
    return get_menu_detail(day, session)


if __name__ == "__main__":
    app.run(port=5000)
