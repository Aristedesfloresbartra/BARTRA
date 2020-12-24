-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-11-2020 a las 17:29:07
-- Versión del servidor: 10.4.13-MariaDB
-- Versión de PHP: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `perudelivery`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `categoria` varchar(50) NOT NULL,
  `cantidad` int(20) NOT NULL,
  `precio` double(10,5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `nombre`, `categoria`, `cantidad`, `precio`) VALUES
(15, 'Mascarilla 3 pliegue', 'Respiratoria', 10, 1.00000),
(16, 'Filtro 2071 p95', 'Respiratoria', 4, 25.00000),
(18, 'Casco de seguridad', 'Cabeza', 40, 25.00000),
(19, 'Gorra contra golpes pw66', 'Cabeza', 60, 15.00000),
(20, 'Casco diamond v', 'Cabeza', 4, 40.00000),
(21, 'Casco de rescate peak', 'Cabeza', 8, 13.00000),
(22, 'Casaca termica-Delta plus', 'Ropa', 10, 100.00000),
(23, 'Pantalon-delata plus', 'Ropa', 19, 78.00000),
(24, 'Casaca alta visibilidad', 'Ropa', 6, 120.00000),
(25, 'Bota cana - porwest', 'Calzado', 7, 45.00000),
(26, 'Zapato punta de acero', 'Calzado', 30, 55.00000),
(27, 'Zapato dielectrico', 'Calzado', 5, 77.00000),
(28, 'Zapato de seguridad s3', 'Calzado', 4, 80.00000),
(29, 'Virtua block plus', 'Lentes', 4, 80.00000),
(30, 'LENTE SECUREFIT 400', 'Lentes', 10, 100.00000),
(31, 'Lentes 3m clasico', 'Lentes', 23, 67.00000);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
