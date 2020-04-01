
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/info')
def mostrar_info():
    s = "<h1>Informacion sobre mi</h1>"
    s += "<img src='' alt='img personal'>"
    return s

if __name__ == '__main__':
    app.run()
