#Esto me INICIALIZA la aplicación flask
from flask import Flask

app = Flask(__name__)

#Establecemos una secret key
app.secret_key = "Esto es Secretosky"