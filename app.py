from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostedData(postedData, functionName):
  if ("x" not in postedData or "y" not in postedData):
    return 301
  else:
    return 200


class Add(Resource):
  def post(self):
    postedData = request.get_json()

    status_code = checkPostedData(postedData, "add")
    if (status_code != 200):
      retJson = {
        "Message": "An error occurred",
        "Status Code": status_code
      }

    x = postedData["x"]
    y = postedData["y"]

    x = int(x)
    y = int(y)

    ret = x + y
    retMap = {
      'Message': ret,
      'Status Code': 200
    }

    return jsonify(retMap)


class Subtract(Resource):
  pass


class Multiply(Resource):
  pass


class Divide(Resource):
  pass


api.add_resource(Add, "/add")


if __name__ == "__main__":
  # app.run() # This works pefectly
  app.run(debug=True) # This helps to give feedback, in times of errors
  # app.run(host="127.0.0.1", port=80) # This is good for production/deployment
