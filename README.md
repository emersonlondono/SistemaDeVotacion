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

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-09-2026 a las 12:13:01
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistema_votacion`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `candidates`
--

CREATE TABLE `candidates` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `party` varchar(100) DEFAULT NULL,
  `votes` int(11) NOT NULL DEFAULT 0,
  `persona_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `candidates`
--

INSERT INTO `candidates` (`id`, `name`, `party`, `votes`, `persona_id`) VALUES
(8, '', 'Partido Verde', 4, 17),
(9, '', 'Partido Liberal', 1, 13),
(10, '', 'Partido Conservador', 3, 11),
(11, '', 'Partido Centro', 1, 12),
(12, '', NULL, 2, 19);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`id`, `name`) VALUES
(3, 'Emerson Londoño'),
(4, 'laura gomez'),
(5, 'Juan perez'),
(6, 'Felipe Rodriguez'),
(7, 'Mariana Lopez'),
(8, 'Sofía Martínez'),
(9, 'Alejandro Gómez'),
(10, 'Valentina Rodríguez'),
(11, 'Mateo Fernández'),
(12, 'Camila López'),
(13, 'Lucas Silva'),
(14, 'Isabella Torres'),
(15, 'Diego Morales'),
(16, 'Mariana Castro'),
(17, 'Gabriel Ramírez'),
(18, 'Sonia Sanchez'),
(19, 'Ana hernandez'),
(20, 'Alvaro'),
(21, 'jesus'),
(22, 'jesus'),
(23, 'jesus'),
(24, 'jesus'),
(25, 'jesus'),
(26, 'jesus');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `email`, `password`) VALUES
(1, 'admin@gmail.com', '123456');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `voter`
--

CREATE TABLE `voter` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `has_voted` tinyint(1) NOT NULL DEFAULT 0,
  `persona_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `voter`
--

INSERT INTO `voter` (`id`, `name`, `email`, `has_voted`, `persona_id`) VALUES
(40, '', 'emerson@gmail.com', 1, 15),
(41, '', 'juan@gmail.com', 1, 16),
(42, '', 'mariana@gmail.com', 1, 5),
(43, '', 'andres@gmail.com', 1, 6),
(44, '', 'carlos@gmail.com', 1, 7),
(45, '', 'santiago@gmail.com', 1, 8),
(46, '', 'daniel@gmail.com', 1, 9),
(47, '', 'miguel@gmail.com', 1, 10),
(48, '', 'soniasanchez@gmail.com', 1, 18),
(49, '', 'alva@gmail.com', 1, 20),
(50, '', 'jesus@gmail', 1, 26);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `votes`
--

CREATE TABLE `votes` (
  `id` int(11) NOT NULL,
  `voter_id` int(11) NOT NULL,
  `candidate_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `votes`
--

INSERT INTO `votes` (`id`, `voter_id`, `candidate_id`) VALUES
(4, 40, 8),
(5, 41, 8),
(6, 42, 8),
(7, 43, 8),
(8, 44, 10),
(9, 45, 10),
(10, 46, 10),
(11, 47, 11),
(12, 48, 12),
(13, 49, 12),
(14, 50, 9);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `voto`
--

CREATE TABLE `voto` (
  `id` int(11) NOT NULL,
  `voter_id` int(11) NOT NULL,
  `eleccion_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `candidates`
--
ALTER TABLE `candidates`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_candidate_persona` (`persona_id`);

--
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `voter`
--
ALTER TABLE `voter`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `fk_voter_persona` (`persona_id`);

--
-- Indices de la tabla `votes`
--
ALTER TABLE `votes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_voter_vote` (`voter_id`),
  ADD KEY `fk_vote_candidate` (`candidate_id`);

--
-- Indices de la tabla `voto`
--
ALTER TABLE `voto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `voter_id` (`voter_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `candidates`
--
ALTER TABLE `candidates`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `personas`
--
ALTER TABLE `personas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `voter`
--
ALTER TABLE `voter`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT de la tabla `votes`
--
ALTER TABLE `votes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `voto`
--
ALTER TABLE `voto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `candidates`
--
ALTER TABLE `candidates`
  ADD CONSTRAINT `fk_candidate_persona` FOREIGN KEY (`persona_id`) REFERENCES `personas` (`id`);

--
-- Filtros para la tabla `voter`
--
ALTER TABLE `voter`
  ADD CONSTRAINT `fk_voter_persona` FOREIGN KEY (`persona_id`) REFERENCES `personas` (`id`);

--
-- Filtros para la tabla `votes`
--
ALTER TABLE `votes`
  ADD CONSTRAINT `fk_vote_candidate` FOREIGN KEY (`candidate_id`) REFERENCES `candidates` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_vote_voter` FOREIGN KEY (`voter_id`) REFERENCES `voter` (`id`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `voto`
--
ALTER TABLE `voto`
  ADD CONSTRAINT `voto_ibfk_1` FOREIGN KEY (`voter_id`) REFERENCES `voter` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
Crear las tablas necesarias para el sistema.

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
