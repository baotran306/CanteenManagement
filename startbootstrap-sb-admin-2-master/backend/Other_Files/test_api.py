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


@app.route("/staff/<int:staff_id>", methods=['GET'])
def get_news_by_id(staff_id):
    # pass
    r = utils.get_info_staff_by_id(staff_id)
    data = {
        'name': r[0],
        'phone': r[1],
        'address': r[2],
        'password': r[3],
        'role': r[4]
    }
    return jsonify(data)


@app.route("/staff/<int:new_id>", methods=["POST"])
def insert_news(new_id):
    if request.form.get(jsonify("abc")):
        utils.add_menu(new_id, '2021-03-06 23:45:05')
        return jsonify({"success": 1})
    return jsonify({"error_code": -1})


if __name__ == "__main__":
    app.run()
