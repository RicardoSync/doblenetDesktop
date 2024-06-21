-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-06-2024 a las 04:28:33
-- Versión del servidor: 8.4.0
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `alpha`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id` int NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Direccion` varchar(255) NOT NULL,
  `Telefono` varchar(15) NOT NULL,
  `Equipos` int NOT NULL,
  `Ip` varchar(15) NOT NULL,
  `Velocidad` varchar(20) NOT NULL,
  `FechaInstalacion` date NOT NULL,
  `ProximoPago` date NOT NULL,
  `Mensualidad` decimal(10,2) NOT NULL,
  `estado` varchar(10) DEFAULT NULL,
  `api` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id`, `Nombre`, `Direccion`, `Telefono`, `Equipos`, `Ip`, `Velocidad`, `FechaInstalacion`, `ProximoPago`, `Mensualidad`, `estado`, `api`) VALUES
(1, 'Ma de Lourdes', '', '4981442266', 1, '122.122.123.25', '100M/10M', '2024-06-07', '2024-07-09', 250.00, 'activado', NULL),
(26, 'Gabriel Hernandez', '', '4962080151', 2, '122.122.125.94', '100M/15M', '2024-06-09', '2024-07-10', 300.00, 'activado', NULL),
(27, 'Paolina Rico', '', '4961340710', 2, '122.122.123.7', '100M/10M', '2024-06-10', '2024-07-11', 250.00, 'activado', NULL),
(28, 'Jose Robledo Resendiz', '', '4961336777', 3, '122.122.123.17', '100M/10M', '2024-06-10', '2024-07-11', 250.00, 'activado', NULL),
(29, 'Magaly Sanchez Briano', 'Sato Toribio', '4961485495', 2, '122.122.123.14', '100M15M', '2024-06-12', '2024-07-13', 300.00, 'activado', NULL),
(30, 'Ma de Jesus Hernandez', '', '', 2, '122.122.125.100', '100M/15M', '2024-06-15', '2024-07-16', 300.00, 'activado', NULL),
(31, 'Lupe Montoya', '', '', 2, '122.122.124.5', '100M/15M', '2024-06-15', '2024-07-16', 300.00, 'activado', NULL),
(32, 'Juana Medina', '', '', 2, '122.122.123.22', '100M/6M', '2024-06-15', '2024-07-16', 250.00, 'activado', NULL),
(33, 'Karina Sanchez', '', '', 2, '122.122.125.90', '100M/15M', '2024-06-15', '2024-07-16', 300.00, 'activado', NULL),
(34, 'Isaac Kali', 'Iglesia', '', 2, '122.122.123.3', '100M/15M', '2024-06-16', '2024-07-17', 300.00, 'activado', NULL),
(35, 'Julieta Casillas', 'Plan de Ayala', '4961286330', 2, '122.122.123.18', '100M/15M', '2024-06-18', '2024-07-19', 300.00, 'activado', NULL),
(36, 'Samuel Ortiz', 'Plan de Ayala', '4961184329', 2, '122.122.123.21', '100M/15M', '2024-06-18', '2024-07-19', 300.00, 'activado', NULL),
(37, 'Ana Isabel', '', '4961232168', 2, '122.122.123.19', '100M/15M', '2024-06-20', '2024-07-21', 300.00, 'activado', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagos`
--

CREATE TABLE `pagos` (
  `id` int NOT NULL,
  `NombreCliente` varchar(100) NOT NULL,
  `Mensualidad` decimal(10,2) NOT NULL,
  `FechaPago` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `pagos`
--

INSERT INTO `pagos` (`id`, `NombreCliente`, `Mensualidad`, `FechaPago`) VALUES
(41, '22', 250.00, '2024-06-07'),
(42, '22', 250.00, '2024-06-07'),
(43, '22', 250.00, '2024-06-07'),
(44, '22', 250.00, '2024-06-07'),
(45, '22', 250.00, '2024-06-07'),
(46, '22', 250.00, '2024-06-07'),
(47, '22', 250.00, '2024-06-08'),
(48, '26', 300.00, '2024-06-09'),
(49, '27', 250.00, '2024-06-10'),
(50, '28', 200.00, '2024-06-10'),
(51, '29', 300.00, '2024-06-12'),
(52, '30', 300.00, '2024-06-15'),
(53, '31', 300.00, '2024-06-15'),
(54, '32', 250.00, '2024-06-15'),
(55, '33', 300.00, '2024-06-15'),
(56, '34', 300.00, '2024-06-16'),
(57, '35', 300.00, '2024-06-18'),
(58, '36', 300.00, '2024-06-18'),
(59, '37', 300.00, '2024-06-20');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pagos`
--
ALTER TABLE `pagos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de la tabla `pagos`
--
ALTER TABLE `pagos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
