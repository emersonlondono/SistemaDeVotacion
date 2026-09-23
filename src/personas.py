from flask import jsonify, request
from flask_jwt_extended import jwt_required
from database import conexion


# POST /personas
@jwt_required()
def registrar_persona():
    try:
        datos = request.get_json(silent=True)

        if not datos:
            return jsonify({
                "error": "El cuerpo de la petición debe ser un JSON válido"
            }), 400

        name = datos.get('name')

        if not name:
            return jsonify({
                "error": "El campo 'name' es obligatorio"
            }), 400

        cursor = conexion.connection.cursor()

        sql = """
            INSERT INTO personas (name)
            VALUES (%s)
        """

        cursor.execute(sql, (name,))

        conexion.connection.commit()

        persona_id = cursor.lastrowid

        cursor.close()

        return jsonify({
            "mensaje": "Persona registrada correctamente",
            "persona_id": persona_id
        }), 201

    except Exception as ex:
        conexion.connection.rollback()

        return jsonify({
            "error": str(ex)
        }), 500


# GET /personas
def lista_personas():
    try:
        cursor = conexion.connection.cursor()

        sql = """
            SELECT id, name
            FROM personas
        """

        cursor.execute(sql)

        datos = cursor.fetchall()

        cursor.close()

        return jsonify(datos), 200

    except Exception as ex:
        return jsonify({
            "error": str(ex)
        }), 500


def registrar_rutas(app):
    app.route(
        '/personas',
        methods=['POST']
    )(registrar_persona)

    app.route(
        '/personas',
        methods=['GET']
    )(lista_personas)