-- Adminer 4.8.1 MySQL 5.5.5-10.3.38-MariaDB-0+deb10u1 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `DonneesBrut`;
CREATE TABLE `DonneesBrut` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `identifiant` int(11) NOT NULL,
  `donnees` float NOT NULL,
  `donnees2` float NOT NULL,
  `type` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `date_recept` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `Specs`;
CREATE TABLE `Specs` (
  `identifiant` int(11) NOT NULL,
  `grandeur` text NOT NULL,
  `ratio` int(8) NOT NULL,
  `unite` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `Specs` (`identifiant`, `grandeur`, `ratio`, `unite`) VALUES
(11523820,	'eau',	1,	'KWh'),
(12300057,	'temp',	1,	'°C'),
(12126620,	'temp',	1,	'°C'),
(12126702,	'temp',	1,	'°C'),
(12300003,	'temp',	1,	'°C'),
(11500342,	'elec',	1,	'KWh'),
(11500236,	'elec',	1,	'KWh'),
(11500310,	'chauff',	10,	'KWh');

-- 2023-06-06 13:20:36