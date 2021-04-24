from flask import Flask, jsonify, request
from flask_cors import CORS
import ConnectSQL
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
            'VIP': r[7]
        })
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


@app.route("/admin/stats/month", methods=['GET'])
def stats_revenue_by_month():
    rows = connect.stats_revenue_by_month()
    data = []
    for r in rows:
        data.append({
            'month': r[0],
            'revenue': r[1]
        })
    return jsonify(data)


@app.route("/admin/stats/all_order", methods=['GET'])
def get_all_order():
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
            'address': r[7]
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
            'image': r[3]
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
            'address': r[7]
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
            'address': r[7]
        })
    return jsonify(data)


@app.route("/admin/stats/cancel_order", methods=['GET'])
def get_cancel_order():
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
            'address': r[7]
        })
    return jsonify(data)


@app.route("/customer/register", methods=['POST', 'GET'])
def insert_customer(ls):
    # not complete, ls is list of all info of register customer
    sign = False
    new_id = connect.generate_new_id_person(1)
    if connect.insert_person(new_id):
        if connect.insert_customer(new_id, vip="NO"):
            if connect.insert_customer_user(ls[-1], ls[-2], new_id):
                sign = True
    return jsonify(sign)


@app.route("/admin/register", methods=['POST', 'GET'])
def insert_staff(ls):
    # not complete, ls is list of all info of register customer
    sign = False
    new_id = connect.generate_new_id_person(0)
    if connect.insert_person(new_id):
        if connect.insert_staff(new_id):
            if connect.insert_user_login(ls[-1], ls[-2], ls[-3], new_id):
                sign = True
    return jsonify(sign)


@app.route("/admin/food", methods=['POST', 'GET'])
def insert_food(ls):
    sign = False
    if connect.insert_food(ls[0], ls[1], ls[2], ls[3]):
        sign = True
    return jsonify(sign)


@app.route("/admin/menu", methods=['GET', 'POST'])
def insert_menu(ls):
    sign = False
    if connect.insert_menu(ls[0], ls[1]):
        sign = True
    return jsonify(sign)


@app.route("/admin/menudetail", methods=['POST', 'GET'])
def insert_menu_detail(ls):
    sign = False
    if connect.insert_menu_detail(ls[0], ls[1]):
        sign = True
    return jsonify(sign)


@app.route("/admin/role", methods=['POST', 'GET'])
def insert_role(ls):
    sign = True
    for i in ls():
        if not connect.insert_role(i):
            sign = False
    return jsonify(sign)


@app.route("/staff/order", methods=['POST', 'GET'])
def insert_order(ls):
    sign = False
    if connect.insert_customer_order(ls[0], ls[1], ls[2], ls[3]):
        # use loop to add menu food in order
        if connect.insert_order_detail(ls[0], ls[4], ls[5], ls[6]):
            sign = True
    return jsonify(sign)


if __name__ == "__main__":
    app.run(port=5000)
