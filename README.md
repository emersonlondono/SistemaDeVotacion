# SistemaDeVotacion

Autor

Emerson Londoño

Proyecto académico - Tecnología en Desarrollo de Software

# Sistema de Votación - API REST

API REST para la gestión de un sistema de votación desarrollada con Python, Flask y MySQL.

El sistema permite registrar personas, votantes, candidatos y votos, además de consultar estadísticas y generar una gráfica con el estado actual de los votos.

## Tecnologías utilizadas

- Python
- Flask
- MySQL
- XAMPP
- Flask-MySQLdb
- Flask-JWT-Extended
- Pandas
- Matplotlib
- Requests
- Thunder Client

## Funcionalidades

- Registro de personas.
- Registro y consulta de votantes.
- Registro y consulta de candidatos.
- Registro de votos.
- Validación para evitar que un votante vote más de una vez.
- Validación para evitar que una persona sea votante y candidato al mismo tiempo.
- Consulta de votos registrados.
- Consulta de estadísticas.
- Generación de gráfica de resultados.
- Autenticación mediante JWT.
- Filtros y paginación para votantes y candidatos.

# Instalación y ejecución local

## 1. Clonar el repositorio

bash
git clone https://github.com/emersonlondono/SistemaDeVotacion.git
## Entrar al proyecto 
cd SistemaDeVotacion
## 2. crear el entorno virtual
python -m venv env
Activar el entorno virtual en windows
.\env\Scripts\Activate.ps1
## 3. instalar dependencias
pip install Flask
pip install flask-mysqldb
pip install Flask-JWT-Extended
pip install pandas
pip install matplotlib
pip install requests
## 4. configurar MySQL
El proyecto utiliza MySQL mediante XAMPP.

Abrir XAMPP.
Iniciar Apache.
Iniciar MySQL.
Abrir phpMyAdmin.
## Usar el siguiente script de bases de dato 
[sistema_votacion.sql](https://github.com/user-attachments/files/32557961/sistema_votacion.sql)

## La configuración utilizada en el proyecto es:

Host: localhost

Usuario: root

Contraseña: 

Base de datos: sistema_votacion

## 5. Ejecutar la API

Desde la carpeta principal del proyecto:

python .\src\app.py

## Autenticación

El sistema utiliza JWT para proteger los endpoints que modifican información.

Primero se debe iniciar sesión mediante:

POST /login

## Ejemplo 
{
    "email": "admin@gmail.com",
    "password": "123456"
}

## Su respuesta tiene un Acces_token  {
    "mensaje": "Inicio de sesión exitoso",
    "access_token": "TOKEN_GENERADO"
}

## Para utilizar los endpoints protegidos se debe enviar el token como:

Authorization: Bearer TOKEN_GENERADO

Ejemplos de uso del API
Iniciar sesión
POST http://127.0.0.1:5000/login

Body:

{
    "email": "admin@gmail.com",
    "password": "123456"
}

Consultar personas
GET http://127.0.0.1:5000/personas
Registrar una persona
POST http://127.0.0.1:5000/personas

Body:

{
    "name": "Carlos Ramirez"
}

Este endpoint requiere autenticación JWT.

Consultar votantes
GET http://127.0.0.1:5000/voters

También permite filtros:

GET http://127.0.0.1:5000/voters?name=Emerson
GET http://127.0.0.1:5000/voters?email=gmail.com

Y paginación:

GET http://127.0.0.1:5000/voters?page=1&limit=5
Registrar un votante
POST http://127.0.0.1:5000/voters

Body:

{
    "persona_id": 3,
    "email": "juan@gmail.com"
}

Este endpoint requiere autenticación JWT.

Eliminar un votante
DELETE http://127.0.0.1:5000/voters/1

Este endpoint requiere autenticación JWT.

Consultar candidatos
GET http://127.0.0.1:5000/candidates

También permite filtros:

GET http://127.0.0.1:5000/candidates?name=Laura
GET http://127.0.0.1:5000/candidates?party=Verde
Registrar candidato
POST http://127.0.0.1:5000/candidates

Body:

{
    "persona_id": 2,
    "party": "Partido Verde"
}

Este endpoint requiere autenticación JWT.

Registrar un voto
POST http://127.0.0.1:5000/votes

Body:

{
    "voter_id": 1,
    "candidate_id": 1
}

Este endpoint requiere autenticación JWT.

El sistema valida que:

El votante exista.
El candidato exista.
El votante no haya votado anteriormente.
La persona no sea simultáneamente votante y candidato.
Consultar votos
GET http://127.0.0.1:5000/votes
Consultar estadísticas
GET http://127.0.0.1:5000/votes/statistics

La respuesta contiene:

Total de votos.
Total de votantes que han votado.
Cantidad de votos por candidato.
Porcentaje de votos de cada candidato.

Ejemplo:
{
    "total_votes": 3,
    "total_voters_who_voted": 3,
    "results": [
        {
            "candidate_id": 1,
            "name": "Laura Gomez",
            "party": "Partido Verde",
            "total_votes": 2,
            "porcentaje": 66.67
        },
        {
            "candidate_id": 2,
            "name": "Felipe Rodriguez",
            "party": "Partido Liberal",
            "total_votes": 1,
            "porcentaje": 33.33
        }
    ]
}

# Generación de estadísticas gráficas

Para generar la gráfica se debe mantener la API ejecutándose en una terminal:
En otra terminal, activar el entorno virtual y ejecutar:

cd .\src
python .\grafico_votos.py

La gráfica muestra:

Candidatos en el eje X.
Cantidad de votos en el eje Y.
Estado actual de los votos.

## Capturas de resultados
Estadísticas de votación

Aquí se incluye una captura de la respuesta del endpoint:

GET /votes/statistics

Gráfica de resultados

Aquí se incluye la gráfica generada utilizando Pandas y Matplotlib.


<img width="787" height="708" alt="image" src="https://github.com/user-attachments/assets/e44d8b7e-4a43-4bba-a40d-f15f859bfce6" />


Estructura del proyecto
SistemaDeVotacion/
│
├── src/
│   ├── app.py
│   ├── auth.py
│   ├── candidates.py
│   ├── config.py
│   ├── database.py
│   ├── grafico_votos.py
│   ├── personas.py
│   ├── votes.py
│   └── voters.py
│
├── .gitignore
└── README.md
