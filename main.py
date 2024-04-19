print("Hello World")
from flask import Flask
from flask import request
from flask_cors import CORS
from ml_utils import driver
import os


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
    # app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"), )
    app.run(host='0.0.0.0', port=5000 )