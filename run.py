from flask import Flask
from app.views import *
#iMPORTO CONECCION A BASE DE DATOS
from app.database import init_app
#Importo corrs para poder trabajar desde otros dominios
from flask_cors import CORS

#Instancia de Flask
app = Flask(__name__)

#habilito el uso de la conexion a la base de datos
init_app()

# Habilito CORS
CORS(app)

#Asociacion de rutas con vistas
app.route('/helloworld', methods=['GET'])(index)
app.route('/nuevo_usuario', methods=['POST'])(create_usuario)
app.route('/actualizar_usuario/<int:usuario_id>', methods=['PUT'])(update_usuario)
app.route('/eliminar_usuario/<int:usuario_id>', methods=['DELETE'])(del_usuario)
app.route('/usuario/<int:usuario_id>', methods=['GET'])(get_usuario)
app.route('/usuarios/', methods=['GET'])(get_all_usuarios)
 
#permite separa el codigo que se ejecuta al correr el archivo
if __name__=='__main__':
    app.run(debug=True)



