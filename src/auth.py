from flask import jsonify, request
from flask_jwt_extended import create_access_token
from database import conexion


def login():
    datos = request.get_json()

    if not datos:
        return jsonify({
            'error': 'Debes enviar los datos en formato JSON'
        }), 400

    email = datos.get('email')
    password = datos.get('password')

    if not email or not password:
        return jsonify({
            'error': 'El email y la contraseña son obligatorios'
        }), 400

    cursor = conexion.connection.cursor()

    cursor.execute(
        'SELECT id, email, password FROM usuarios WHERE email = %s',
        (email,)
    )

    usuario = cursor.fetchone()

    cursor.close()

    if not usuario:
        return jsonify({
            'error': 'Credenciales incorrectas'
        }), 401

    if password != usuario[2]:
        return jsonify({
            'error': 'Credenciales incorrectas'
        }), 401

    token = create_access_token(identity=str(usuario[0]))

    return jsonify({
        'mensaje': 'Inicio de sesión exitoso',
        'access_token': token
    }), 200


def registrar_rutas(app):
    app.route('/login', methods=['POST'])(login)