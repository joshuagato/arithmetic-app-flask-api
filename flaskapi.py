from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World!"


@app.route('/hithere')
def hi_there_everyone():
  return "I just hit /hithere"


if __name__  == "__main__":
  # app.run() # This works pefectly
  # app.run(debug=True) # This helps to give feedback, in times of errors
  app.run(host="127.0.0.1", port=80) # This is good for production/deployment
