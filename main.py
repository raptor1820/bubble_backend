from flask import Flask,request
from flask_cors import CORS
from ml_utils import driver
from waitress import serve

app = Flask(__name__)
CORS(app)
@app.route("/")
def root():
    url  = request.args['url']
    try:
        return driver(url)
    except:
        return {"error": "error"}
    
if __name__== "__main__":
    serve(app, host='127.0.0.1', port=5000)