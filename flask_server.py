from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    x = [{'a':1, 'b':2}, {'c': [1,2,3]}]
    return jsonify(x)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085, debug=True)