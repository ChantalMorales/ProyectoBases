-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-07-2019 a las 23:02:20
-- Versión del servidor: 10.1.40-MariaDB
-- Versión de PHP: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `Proyecto_bases`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `Id_est` int(5) NOT NULL,
  `Nom_est` varchar(30) COLLATE utf8mb4_spanish_ci NOT NULL,
  `Apel_est` varchar(30) COLLATE utf8mb4_spanish_ci NOT NULL,
  `Nota` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`Id_est`, `Nom_est`, `Apel_est`, `Nota`) VALUES
(20191, 'Esteban', 'Calvopiña', 0),
(20192, 'Lain', 'Vinueza', 0),
(20193, 'Chantal', 'Morales', 0),
(20194, 'Alejandra', 'Rojas', 0),
(20195, 'Jonathan', 'Vasquez', 0),
(20196, 'Israel', 'Vivas', 0),
(20197, 'Kevin', 'Segovia', 0),
(20198, 'Sebastian', 'Morales', 0),
(20199, 'Nicole', 'Zambrano', 0),
(20190, 'Pepito', 'Suarez', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias`
--

CREATE TABLE `materias` (
  `Id_materia` varchar(5) COLLATE utf8mb4_spanish_ci NOT NULL,
  `Nom_materia` varchar(30) COLLATE utf8mb4_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `materias`
--

INSERT INTO `materias` (`Id_materia`, `Nom_materia`) VALUES
('SO01', 'Sistemas Operativos'),
('AF02', 'Algoritmos Fundamentales'),
('C03', 'Comunicaciones'),
('BD04', 'Bases de Datos'),
('PA05', 'Programacion Avanzada');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesor`
--

CREATE TABLE `profesor` (
  `Id_prof` int(5) NOT NULL,
  `Nom_prof` varchar(30) COLLATE utf8mb4_spanish_ci NOT NULL,
  `Apel_prof` varchar(30) COLLATE utf8mb4_spanish_ci NOT NULL,
  `Id_mate` varchar(5) COLLATE utf8mb4_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `profesor`
--

INSERT INTO `profesor` (`Id_prof`, `Nom_prof`, `Apel_prof`, `Id_mate`) VALUES
(12345, 'Leandro', 'Pazmiño', 'C01'),
(67890, 'Marina', 'Vintimilla', 'BD02'),
(54321, 'Pablo', 'Zaldumbide', 'PA03'),
(9876, 'Byron', 'Loarte', 'AF04'),
(13579, 'Richard', 'Rivera', 'SO05');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
