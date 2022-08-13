from flask import Flask, Response, json
from flask_restful import Resource, Api

from math import gcd
app = Flask(__name__)

api = Api(app)




class GCD(Resource):
    def get(self, num1, num2):
        return gcd(num1, num2)


api.add_resource(GCD, '/<string:num1>/<string:num2>')


if __name__ == '__main__':
    app.run(debug=True,
            port=5050,
            host="0.0.0.0")
