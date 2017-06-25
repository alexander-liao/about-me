from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def serveRoot():
    return ''

if __name__ == '__main__':
    app.run(debug = True, port = 5000, host = '0.0.0.0')
