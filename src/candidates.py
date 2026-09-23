from flask import jsonify, request
from flask_jwt_extended import jwt_required
from database import conexion


# POST /candidates
@jwt_required()
def registrar_candidate():

    try:
        datos = request.get_json(silent=True)

        if not datos:
            return jsonify({
                "error": "El cuerpo de la petición debe ser un JSON válido"
            }), 400

        persona_id = datos.get('persona_id')
        party = datos.get('party')

        if persona_id is None:
            return jsonify({
                "error": "El campo 'persona_id' es obligatorio"
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
                "error": "Esta persona ya está registrada como votante y no puede ser candidato"
            }), 409

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
                "error": "Esta persona ya está registrada como candidato"
            }), 409

        # Insertar candidato
        cursor.execute(
            """
            INSERT INTO candidates (persona_id, party)
            VALUES (%s, %s)
            """,
            (persona_id, party)
        )

        conexion.connection.commit()

        cursor.close()

        return jsonify({
            "mensaje": "Candidato registrado correctamente"
        }), 201

    except Exception as ex:

        conexion.connection.rollback()

        return jsonify({
            "error": str(ex)
        }), 500


# GET /candidates
def listar_candidatos():

    name = request.args.get('name')
    party = request.args.get('party')

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
            c.id,
            p.name,
            c.party,
            c.votes
        FROM candidates c
        INNER JOIN personas p
            ON c.persona_id = p.id
        WHERE 1=1
    """

    parametros = []

    if name:
        query += " AND p.name LIKE %s"
        parametros.append(f"%{name}%")

    if party:
        query += " AND c.party LIKE %s"
        parametros.append(f"%{party}%")

    query += " ORDER BY c.id LIMIT %s OFFSET %s"

    parametros.append(limit)
    parametros.append(offset)

    cursor.execute(query, tuple(parametros))

    candidatos = cursor.fetchall()

    cursor.close()

    resultado = []

    for candidato in candidatos:

        resultado.append({
            'id': candidato[0],
            'name': candidato[1],
            'party': candidato[2],
            'votes': candidato[3]
        })

    return jsonify({
        'page': page,
        'limit': limit,
        'candidates': resultado
    }), 200


def registrar_rutas(app):

    app.route(
        '/candidates',
        methods=['POST']
    )(registrar_candidate)

    app.route(
        '/candidates',
        methods=['GET']
    )(listar_candidatos)