from flask import Flask, jsonify
import def_utils as utils
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)
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


@app.route("/news/add", methods=["POST"])
def insert_news():
    pass


if __name__ == "__main__":
    app.run(port=3000)
# chay lai xme
