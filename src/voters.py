from flask import jsonify, request
from flask_jwt_extended import jwt_required
from database import conexion


# GET /voters
def listar_votantes():

    name = request.args.get('name')
    email = request.args.get('email')

    try:
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 5))
    except ValueError:
        return jsonify({
            'error': 'page y limit deben ser números'
        }), 400

    if page < 1 or limit < 1:
        return jsonify({
            'error': 'page y limit deben ser mayores que 0'
        }), 400

    offset = (page - 1) * limit

    cursor = conexion.connection.cursor()

    query = """
        SELECT
            v.id,
            p.name,
            v.email,
            v.has_voted
        FROM voter v
        INNER JOIN personas p
            ON v.persona_id = p.id
        WHERE 1=1
    """

    parametros = []

    if name:
        query += " AND p.name LIKE %s"
        parametros.append(f"%{name}%")

    if email:
        query += " AND v.email LIKE %s"
        parametros.append(f"%{email}%")

    query += " ORDER BY v.id LIMIT %s OFFSET %s"

    parametros.append(limit)
    parametros.append(offset)

    cursor.execute(query, tuple(parametros))

    votantes = cursor.fetchall()

    cursor.close()

    resultado = []

    for votante in votantes:
        resultado.append({
            'id': votante[0],
            'name': votante[1],
            'email': votante[2],
            'has_voted': bool(votante[3])
        })

    return jsonify({
        'page': page,
        'limit': limit,
        'voters': resultado
    }), 200


# POST /voters
@jwt_required()
def registrar_voter():

    try:
        datos = request.get_json(silent=True)

        if not datos:
            return jsonify({
                "error": "El cuerpo de la petición debe ser un JSON válido"
            }), 400

        persona_id = datos.get('persona_id')
        email = datos.get('email')

        if persona_id is None or not email:
            return jsonify({
                "error": "Los campos 'persona_id' y 'email' son obligatorios"
            }), 400

        cursor = conexion.connection.cursor()

        # Verificar persona
        cursor.execute(
            """
            SELECT id
            FROM personas
            WHERE id = %s
            """,
            (persona_id,)
        )

        persona = cursor.fetchone()

        if not persona:
            cursor.close()

            return jsonify({
                "error": "La persona no existe"
            }), 404

        # Verificar candidato
        cursor.execute(
            """
            SELECT id
            FROM candidates
            WHERE persona_id = %s
            """,
            (persona_id,)
        )

        candidato = cursor.fetchone()

        if candidato:
            cursor.close()

            return jsonify({
                "error": "Esta persona ya está registrada como candidato y no puede ser votante"
            }), 409

        # Verificar votante
        cursor.execute(
            """
            SELECT id
            FROM voter
            WHERE persona_id = %s
            """,
            (persona_id,)
        )

        votante = cursor.fetchone()

        if votante:
            cursor.close()

            return jsonify({
                "error": "Esta persona ya está registrada como votante"
            }), 409

        # Verificar email
        cursor.execute(
            """
            SELECT id
            FROM voter
            WHERE email = %s
            """,
            (email,)
        )

        correo = cursor.fetchone()

        if correo:
            cursor.close()

            return jsonify({
                "error": "El correo ya está registrado"
            }), 409

        # Insertar votante
        cursor.execute(
            """
            INSERT INTO voter (persona_id, email)
            VALUES (%s, %s)
            """,
            (persona_id, email)
        )

        conexion.connection.commit()

        cursor.close()

        return jsonify({
            "mensaje": "Votante registrado correctamente"
        }), 201

    except Exception as ex:

        conexion.connection.rollback()

        return jsonify({
            "error": str(ex)
        }), 500


# DELETE /voters/<id>
@jwt_required()
def eliminar_voter(id):

    try:
        cursor = conexion.connection.cursor()

        cursor.execute(
            """
            DELETE FROM voter
            WHERE id = %s
            """,
            (id,)
        )

        conexion.connection.commit()

        filas_afectadas = cursor.rowcount

        cursor.close()

        if filas_afectadas == 0:
            return jsonify({
                "error": "El votante no existe"
            }), 404

        return jsonify({
            "mensaje": "Votante eliminado correctamente"
        }), 200

    except Exception as ex:

        conexion.connection.rollback()

        return jsonify({
            "error": str(ex)
        }), 500


def registrar_rutas(app):

    app.route(
        '/voters',
        methods=['GET']
    )(listar_votantes)

    app.route(
        '/voters',
        methods=['POST']
    )(registrar_voter)

    app.route(
        '/voters/<int:id>',
        methods=['DELETE']
    )(eliminar_voter)