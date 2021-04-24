# import pyodbc
# from flask import Flask, request
# from flask_restful import Resource, Api
# from json import dumps
# from flask.json import jsonify
# import pandas as pd
#
#
# def read(conn, table_name):
#     print("Read")
#     cursor = conn.cursor()
#     abc = cursor.execute(
#         'select * from {}'.format(table_name)
#     )
#     ans = {}
#     ls = []
#     for row in cursor:
#         ls.append(row)
#     ans['staff'] = ls
#     return ans
#
#
# def insert(conn, a, b):
#     print("Insert")
#     cursor = conn.cursor()
#     cursor.execute(
#         'insert into Publisher values (?, ?);',
#         (a, b)
#     )
#     conn.commit()
#
#
# def update(conn):
#     print("Update")
#     cursor = conn.cursor()
#     cursor.execute(
#         'update Publisher set Name=? where id=?;',
#         ('Test2 Update', 'abc')
#     )
#     conn.commit()
#     read(conn, "Publisher")
#
#
# def delete(conn):
#     print("Delete")
#     cursor = conn.cursor()
#     cursor.execute(
#         'delete from Publisher where id=?;',
#         'abc'
#     )
#     conn.commit()
#
#
# conn = pyodbc.connect(
#     "Driver={SQL Server Native Client 11.0};"
#     "Server=WINDOWS-A251ALV;"
#     "Database=BookStore;"
#     "Trusted_Connection=yes;"
# )
# print(read(conn, "Staff"))
# # delete(conn)
# # insert(conn)
# # update(conn)
# # insert(conn, "aa", "Test2")
# conn.close()

from flask import Flask, jsonify, request
from flask_cors import CORS
import Other_Files.def_utils as utils

app = Flask(__name__)
CORS(app)


@app.route("/staff", methods=["GET"])
def get_news():
    rows = utils.get_info_staff()
    data = []
    for r in rows:
        data.append({
            'id': r[0],
            'name': r[1],
            'phone': r[2],
            'address': r[3],
            'password': r[4],
            'role': r[5]
        })
    return jsonify(data)


@app.route("/news/<int:news_id>", methods=['GET'])
def get_news_by_id(news_id):
    pass
    rows = utils.get_all_info("menu")
    data = []
    for r in rows:
        data.append({
            'id': r[0],
            'date_now': r[1]
        })
    return jsonify(data)


@app.route("/news/<int:new_id>", methods=["POST"])
def insert_news(new_id):
    if request.form.get("content"):
        utils.add_menu(new_id, '2021-03-06 19:00:05')
        return jsonify({"success": 1})
    return jsonify({"error_code": -1})


if __name__ == "__main__":
    app.run()
