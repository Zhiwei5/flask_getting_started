from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/name", methods=["GET"])
def name():
    """
    Returns the string of my name to the caller
    """
    abc = {
        "name": "Zhiwei"
    }
    return jsonify(abc)


@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    """
    Returns a hello message to the caller
    """
    data = {
        "message": "Hello {0}".format(name)
    }
    return jsonify(data)


@app.route("/distance", methods=["POST"])
def distance():
    r = request.get_json()  # parses the POST request body as JSON
    dis_x = abs(r["a"][0] - r["b"][0])
    dis_y = abs(r["a"][1] - r["b"][1])
    cartesian_distance = calculate_distance(dis_x, dis_y)

    distance_dic = {
        "distance": cartesian_distance ,
        "a": r["a"],
        "b": r["b"]
    }
    return jsonify(distance_dic), 200


def calculate_distance(a,b):
    c_dis = (a**2 + b**2)**0.5

    return c_dis

if __name__ == "__main__":
    app.run()