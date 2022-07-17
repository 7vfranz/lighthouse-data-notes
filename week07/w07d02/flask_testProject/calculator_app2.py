# %%
# import Flask and jsonify
from flask import Flask, jsonify

# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse

# %%
app = Flask(__name__)
api = Api(app)

# %%
class add(Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create argument 'number'
        parser.add_argument('num1', type=int, location='args')
        parser.add_argument('num2', type=int, location='args')

        # parse 'number'
        num1 = parser.parse_args().get('num1')
        num2 = parser.parse_args().get('num2')

        result = num1 + num2
        # make json result
        return jsonify(result=result)

class subtract(Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create argument 'number'
        parser.add_argument('num1', type=int, location='args')
        parser.add_argument('num2', type=int, location='args')

        # parse 'number'
        num1 = parser.parse_args().get('num1')
        num2 = parser.parse_args().get('num2')

        result = num1 - num2
        # make json result
        return jsonify(result=result)

class multiply(Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create argument 'number'
        parser.add_argument('num1', type=int, location='args')
        parser.add_argument('num2', type=int, location='args')

        # parse 'number'
        num1 = parser.parse_args().get('num1')
        num2 = parser.parse_args().get('num2')

        result = num1 * num2
        # make json result
        return jsonify(result=result)

class divide(Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create argument 'number'
        parser.add_argument('num1', type=int, location='args')
        parser.add_argument('num2', type=int, location='args')

        # parse 'number'
        num1 = parser.parse_args().get('num1')
        num2 = parser.parse_args().get('num2')

        result = num1 / num2
        # make json result
        return jsonify(result=result)

# %%
# assign endpoints
api.add_resource(add, '/add',)
api.add_resource(subtract, '/subtract',)
api.add_resource(multiply, '/multiply',)
api.add_resource(divide, '/divide',)

# %%
if __name__ == '__main__':
    app.run(debug=True)
