from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/logs/')
def log():
    return jsonify({'id':'1',
                    'time':'2023_03_04'})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
   