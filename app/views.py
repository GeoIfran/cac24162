from flask import jsonify

def index():
    response={'mwssage':'Hola mundo API FLASK'}
    return jsonify(response)