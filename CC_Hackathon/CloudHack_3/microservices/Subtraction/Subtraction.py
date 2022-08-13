from flask import Flask, Response, json
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)


def subfunc(n1, n2):
    return float(n1) - float(n2)


class Subtract(Resource):
    def get(self, num1, num2):
        return subfunc(num1, num2)


api.add_resource(Subtract, '/<string:num1>/<string:num2>')


if __name__ == '__main__':
    app.run(debug=True,
            port=5050,
            host="0.0.0.0")
