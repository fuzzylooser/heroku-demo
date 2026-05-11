from flask import Flask
app = Flask(__name__)

@app.route("/")
def hekko():
  return{"message":"hello"}
