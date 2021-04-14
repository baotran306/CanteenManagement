from flask import Flask, jsonify, request
from flask_cors import CORS
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
            'salary': r[8],
            'password': r[9]
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
            'VIP': r[7],
            'password': r[8]
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
            'customer_id': r[5]
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


if __name__ == "__main__":
    app.run(3000)
