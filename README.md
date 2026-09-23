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
```
Host: localhost

Usuario: root

Contraseña: 
```

Base de datos: sistema_votacion

## 5. Ejecutar la API

Desde la carpeta principal del proyecto:

python .\src\app.py

## Autenticación

El sistema utiliza JWT para proteger los endpoints que modifican información.

Primero se debe iniciar sesión mediante:

POST /login

## Ejemplo 
```
{
    "email": "admin@gmail.com",
    "password": "123456"
}
```
## Su respuesta tiene un Acces_token 
```
{
    "mensaje": "Inicio de sesión exitoso",
    "access_token": "TOKEN_GENERADO"
}
```

## Para utilizar los endpoints protegidos se debe enviar el token como:

Authorization: Bearer TOKEN_GENERADO

Ejemplos de uso del API
Iniciar sesión
POST http://127.0.0.1:5000/login
```
Body:

{
    "email": "admin@gmail.com",
    "password": "123456"
}
```
Consultar personas
GET http://127.0.0.1:5000/personas
Registrar una persona
POST http://127.0.0.1:5000/personas



Body:
```
{
    "name": "Carlos Ramirez"
}

```
Este endpoint requiere autenticación JWT.

Consultar votantes
GET http://127.0.0.1:5000/voters

También permite filtros:
```
GET http://127.0.0.1:5000/voters?name=Emerson
GET http://127.0.0.1:5000/voters?email=gmail.com
```

Y paginación:
```

GET http://127.0.0.1:5000/voters?page=1&limit=5
Registrar un votante
POST http://127.0.0.1:5000/voters
```

Body:
```
{
    "persona_id": 3,
    "email": "juan@gmail.com"
}
```

Este endpoint requiere autenticación JWT.

Eliminar un votante
```
DELETE http://127.0.0.1:5000/voters/1
```

Este endpoint requiere autenticación JWT.

Consultar candidatos
```
GET http://127.0.0.1:5000/candidates
```
También permite filtros:
```

GET http://127.0.0.1:5000/candidates?name=Laura
GET http://127.0.0.1:5000/candidates?party=Verde
Registrar candidato
POST http://127.0.0.1:5000/candidates
```

Body:
```
{
    "persona_id": 2,
    "party": "Partido Verde"
}
```

Este endpoint requiere autenticación JWT.

```

Registrar un voto
POST http://127.0.0.1:5000/votes
```

Body:
```
{
    "voter_id": 1,
    "candidate_id": 1
}
```

Este endpoint requiere autenticación JWT.

El sistema valida que:

El votante exista.
El candidato exista.
El votante no haya votado anteriormente.
La persona no sea simultáneamente votante y candidato.
Consultar votos
```
GET http://127.0.0.1:5000/votes
```
Consultar estadísticas
```
GET http://127.0.0.1:5000/votes/statistics
```

La respuesta contiene:

Total de votos.
Total de votantes que han votado.
Cantidad de votos por candidato.
Porcentaje de votos de cada candidato.

Ejemplo:
```
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
```

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

## Algunas capturas de funcionamiento

1. Login funcionando

   <img width="1612" height="541" alt="image" src="https://github.com/user-attachments/assets/4569f1c2-e706-446c-8a43-b010e7cb63bc" />
2. Creacion de Persona

    <img width="1601" height="502" alt="image" src="https://github.com/user-attachments/assets/bffdc959-7d47-44d7-968f-2f32111600a5" />
## Se visualiza que se necesita el Token para poder agregar personas mediante el Post

<img width="1611" height="512" alt="image" src="https://github.com/user-attachments/assets/f5c4aa45-1b87-40ec-b0ce-20eedf7dca44" />
## Se visualiza el funcionamiento luego de authenticar el token, y se agrega el id de manera automatica como lo pide el caso de estudio.

3. Registrar votantes

<img width="1612" height="547" alt="image" src="https://github.com/user-attachments/assets/8913e92e-c3a5-4dc9-8b60-ef58df5ca45a" />

4. Lista de votantes

   <img width="511" height="912" alt="image" src="https://github.com/user-attachments/assets/fd506ffb-2268-468b-b6f6-e0cb4ecb329c" />

5. Listado de candidatos

<img width="772" height="936" alt="image" src="https://github.com/user-attachments/assets/e2cbe287-355a-464d-89fc-f568036ae941" />

7. Registrar un voto
<img width="1603" height="586" alt="image" src="https://github.com/user-attachments/assets/ee113151-fe56-4e7a-9e7f-cb57ef937bd8" />

En caso de que el candidato y votante no existan: 

<img width="1620" height="980" alt="image" src="https://github.com/user-attachments/assets/82436f15-00e0-4381-a544-ef12d102982d" />

<img width="1593" height="597" alt="image" src="https://github.com/user-attachments/assets/16c03bac-52b5-48c6-b460-9e42af8570af" />

En caso de votar dos veces: 

<img width="1612" height="346" alt="image" src="https://github.com/user-attachments/assets/0d4e7b0e-3c29-4d4d-a617-ca72873af040" />

9. Estadísticas

   <img width="613" height="953" alt="image" src="https://github.com/user-attachments/assets/58beb17b-1da2-47a6-9653-132c6e4bbd36" />
10. Validacion de que un votante no puede ser candidato y viceversa:
    <img width="1578" height="398" alt="image" src="https://github.com/user-attachments/assets/f4f6466d-3b98-40b5-9318-617925066a75" />
    <img width="1605" height="331" alt="image" src="https://github.com/user-attachments/assets/9905b635-a409-4641-bed2-eb6d79d48948" />
11. Prueba de filtros de busqueda:

    <img width="1605" height="507" alt="image" src="https://github.com/user-attachments/assets/d44da330-033e-40de-8e91-2ae3a1bccb9c" />
    
<img width="1582" height="943" alt="image" src="https://github.com/user-attachments/assets/716afd1f-6ae7-4f99-9833-127b48e7eab4" />



Estructura del proyecto
```
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
```
