from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@app.route('/sayhi/<name>', methods=['GET'])
def sayhi(name):
    return 'Say hi, '+ name


@app.route('/sayhi2/<name>', methods=['GET'])
def sayhi(name):
    return 'Say hi2, '+ name


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
#port 5000 = flask.
    
