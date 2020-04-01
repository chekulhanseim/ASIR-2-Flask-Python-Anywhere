# ASIR-2-Flask-Python-Anywhere
Proyecto de Python Flask con su gestión en Python Anywhere

[Para más información sobre Flask](https://openwebinars.net/blog/que-es-flask/)

## Tareas ##
Ver el reto de Classrooom para las tareas de gestión

### Google Colab ###
Este proyecto fue creado con Google Colab. Para ejecutar un proyecto de Flask, solo hay que pip install *flask_ngrok*

*from flask_ngrok import run_with_ngrok* 
from flask import Flask

app = Flask(__name__)

*run_with_ngrok(app)* 

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
