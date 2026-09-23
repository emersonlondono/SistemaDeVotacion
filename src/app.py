from flask import Flask
from flask_jwt_extended import JWTManager

from config import config
from database import conexion

import auth
import personas
import voters
import candidates
import votes


app = Flask(__name__)

app.config.from_object(config['development'])

app.config['JWT_SECRET_KEY'] = 'clave-secreta-votaciones-2026'

conexion.init_app(app)

jwt = JWTManager(app)


# Registrar las rutas de cada archivo
auth.registrar_rutas(app)
personas.registrar_rutas(app)
voters.registrar_rutas(app)
candidates.registrar_rutas(app)
votes.registrar_rutas(app)


# Manejo de error 404
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return {
        "error": "La ruta que intentas buscar no existe"
    }, 404


if __name__ == '__main__':
    app.run()