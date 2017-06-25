from flask import Flask
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def serveRoot():
    with open('static/triggers.txt', 'r') as f:
        return f.read()

@app.route('/write/<trigger>')
def write(trigger):
    print 'write', trigger
    with open('static/triggers.txt', 'a') as f:
        f.write(str(trigger) + '\n')
    return 'success'

@app.route('/clear')
def clear():
    with open('static/triggers.txt', 'w') as f:
        f.write('')
    return 'success'

def main():
    app.run(debug = True, host = '0.0.0.0', port = 5000)

if __name__ == '__main__':
    main()
