from flask import Flask
from flask import jsonify
import Read
import json

app = Flask(__name__)

@app.route('/logs/')
def log():
    data=Read.ReadJson()
    json_object = json.dumps(data, indent = 4)
    return jsonify(json_object)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
   