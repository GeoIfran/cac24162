from flask import Flask
from app.views import index

#Instancia de Flask
app = Flask(__name__)

#Asociacion de rutas con vistas
app.route('/helloworld', methods=['GET'])(index)

#permite separa el codigo que se ejecuta al correr el archivo
if __name__=='__main__':
    app.run(debug=True)