# %%
# import Flask and jsonify
from flask import Flask, jsonify

# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse

# %%
app = Flask(__name__)
api = Api(app)

# %%
class calculator(Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create argument 'number'
        parser.add_argument('operation', type=str, location='args')
        parser.add_argument('number1', type=int, location='args')
        parser.add_argument('number2', type=int, location='args')

        # parse 'number'
        number1 = parser.parse_args().get('number1')
        number2 = parser.parse_args().get('number2')
        operation = parser.parse_args().get('operation')

        if operation=="add":
            res = number1 + number2
        elif operation=="subtract":
            res = number1 - number2
        elif operation=="multiply":
            res = number1 * number2
        elif operation=="divide":
            res = number1 / number2
        else:
            res = 'Invalid operation'

        # make json from greeting string 
        return jsonify(res=res)

# %%
# assign endpoints
api.add_resource(calculator, '/calculator',)

# %%
if __name__ == '__main__':
    app.run(debug=True)

# %%


# %%



