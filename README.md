# SistemaDeVotacion

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

