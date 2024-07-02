#Importar librerias a utilizar
# de flask importo jsonify para enviar el return en formato JSON y la funcion request para poder leer json
from flask import jsonify, request
#Importo la Clase Usuario
from app.models import Usuario
#funcion de prueba inicial
def index():
    response={'mwssage':'Hola mundo API FLASK'}
    return jsonify(response)
#Traer los datos de un usuario
def get_usuario(usuario_id):
    print('usuario recibido',type(usuario_id),usuario_id)
    usuario = Usuario.perfil(usuario_id)
    if not usuario:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    return jsonify(usuario.serialize())
def create_usuario():
#datos recibidos en formato json
    data = request.json
    nuevo_usuario = Usuario(apellido=data['firstname'], nombre=data['lastname'], email=data['email'], fecha_nacimiento=data['birthdate'], clave=data['password'], genero=data['gender'])
    nuevo_usuario.grabar()
    return jsonify({'message': 'Usuario Creado correctamente','data':data}), 201
# Actualizar usuario
def update_usuario(usuario_id):
    #creo la instancia de usuario para el id dado
    usuario= Usuario.perfil(usuario_id)
    usuario.id_usuario=usuario_id
    # confirmo que exista ese id de usuario y sino devuelco usuario no encontrado error 404
    if not usuario:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    #datos recibidos en formato json
    data = request.json
    usuario.apellido=data['firstname']
    usuario.nombre=data['lastname']
    usuario.email=data['email']
    usuario.fecha_nacimiento=data['birthdate']
    usuario.clave=data['password']
    usuario.genero=data['gender']
    usuario.grabar()
    return jsonify({'message': 'Usuario modificado exitosamente','data':data,'Usuario':usuario.email,'id': usuario.id_usuario}), 201
def del_usuario(usuario_id):
    usuario= Usuario.perfil(usuario_id)
    if not usuario:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    data = request.json
    usuario.borrar()
    return jsonify({'message': 'Usuario ha sido eliminado exitosamente','data':data,'id':usuario_id}), 201
# creo funcion que traiga todos los usuarios
def get_all_usuarios():
    usuarios = Usuario.get_all()
    return jsonify([usuario.serialize() for usuario in usuarios])
