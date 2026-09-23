from flask import jsonify, request
from flask_jwt_extended import jwt_required
from database import conexion


# POST /votes
@jwt_required()
def registrar_vote():

    try:
        datos = request.get_json(silent=True)

        if not datos:
            return jsonify({
                "error": "El cuerpo de la petición debe ser un JSON válido"
            }), 400

        voter_id = datos.get('voter_id')
        candidate_id = datos.get('candidate_id')

        if voter_id is None or candidate_id is None:
            return jsonify({
                "error": "Los campos 'voter_id' y 'candidate_id' son obligatorios"
            }), 400

        cursor = conexion.connection.cursor()

        # Verificar votante
        cursor.execute(
            """
            SELECT id, has_voted
            FROM voter
            WHERE id = %s
            """,
            (voter_id,)
        )

        votante = cursor.fetchone()

        if not votante:
            cursor.close()

            return jsonify({
                "error": "El votante no existe"
            }), 404

        # Verificar candidato
        cursor.execute(
            """
            SELECT id
            FROM candidates
            WHERE id = %s
            """,
            (candidate_id,)
        )

        candidato = cursor.fetchone()

        if not candidato:
            cursor.close()

            return jsonify({
                "error": "El candidato no existe"
            }), 404

        # Verificar si ya votó
        if votante[1]:
            cursor.close()

            return jsonify({
                "error": "El votante ya ha emitido su voto"
            }), 409

        # Registrar voto
        cursor.execute(
            """
            INSERT INTO votes (voter_id, candidate_id)
            VALUES (%s, %s)
            """,
            (voter_id, candidate_id)
        )

        # Marcar votante
        cursor.execute(
            """
            UPDATE voter
            SET has_voted = TRUE
            WHERE id = %s
            """,
            (voter_id,)
        )

        # Aumentar votos candidato
        cursor.execute(
            """
            UPDATE candidates
            SET votes = votes + 1
            WHERE id = %s
            """,
            (candidate_id,)
        )

        conexion.connection.commit()

        cursor.close()

        return jsonify({
            "mensaje": "Voto registrado correctamente"
        }), 201

    except Exception as ex:

        conexion.connection.rollback()

        return jsonify({
            "error": str(ex)
        }), 500


# GET /votes
def lista_votes():

    try:
        cursor = conexion.connection.cursor()

        sql = """
            SELECT
                v.id,
                v.voter_id,
                p1.name AS voter_name,
                v.candidate_id,
                p2.name AS candidate_name
            FROM votes v
            INNER JOIN voter vo
                ON v.voter_id = vo.id
            INNER JOIN personas p1
                ON vo.persona_id = p1.id
            INNER JOIN candidates c
                ON v.candidate_id = c.id
            INNER JOIN personas p2
                ON c.persona_id = p2.id
        """

        cursor.execute(sql)

        datos = cursor.fetchall()

        cursor.close()

        return jsonify(datos), 200

    except Exception as ex:

        return jsonify({
            "error": str(ex)
        }), 500


# GET /votes/statistics
def estadisticas_votes():

    try:
        cursor = conexion.connection.cursor()

        # Total de votos
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM votes
            """
        )

        total_votos = cursor.fetchone()[0]

        # Votos por candidato
        cursor.execute(
            """
            SELECT
                c.id,
                p.name,
                c.party,
                COUNT(v.id) AS total_votos
            FROM candidates c
            INNER JOIN personas p
                ON c.persona_id = p.id
            LEFT JOIN votes v
                ON c.id = v.candidate_id
            GROUP BY c.id, p.name, c.party
            ORDER BY total_votos DESC
            """
        )

        candidatos = cursor.fetchall()

        # Total votantes que votaron
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM voter
            WHERE has_voted = TRUE
            """
        )

        total_votantes_votaron = cursor.fetchone()[0]

        cursor.close()

        resultados = []

        for candidato in candidatos:

            votos = candidato[3]

            if total_votos > 0:
                porcentaje = (votos / total_votos) * 100
            else:
                porcentaje = 0

            resultados.append({
                "candidate_id": candidato[0],
                "name": candidato[1],
                "party": candidato[2],
                "total_votes": votos,
                "porcentaje": round(porcentaje, 2)
            })

        return jsonify({
            "total_votes": total_votos,
            "total_voters_who_voted": total_votantes_votaron,
            "results": resultados
        }), 200

    except Exception as ex:

        return jsonify({
            "error": str(ex)
        }), 500


def registrar_rutas(app):

    app.route(
        '/votes',
        methods=['POST']
    )(registrar_vote)

    app.route(
        '/votes',
        methods=['GET']
    )(lista_votes)

    app.route(
        '/votes/statistics',
        methods=['GET']
    )(estadisticas_votes)