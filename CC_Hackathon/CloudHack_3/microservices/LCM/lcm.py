from flask import Flask, Response, json
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)


def calculate_lcm(x, y):  
    # selecting the greater number  
    if x > y:  
        greater = x  
    else:  
        greater = y  
    while(True):  
        if((greater % x == 0) and (greater % y == 0)):  
            lcm = greater  
            break  
        greater += 1  
    return lcm    
  

class LCM(Resource):
    def get(self, num1, num2):
        return calculate_lcm(num1, num2)


api.add_resource(LCM, '/<string:num1>/<string:num2>')


if __name__ == '__main__':
    app.run(debug=True,
            port=5050,
            host="0.0.0.0")


