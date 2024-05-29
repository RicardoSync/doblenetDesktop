-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: alpha
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Cliente de Prueba','123 Calle Principal','123-456-7890',1,'192.168.1.100','100M/25M','2024-05-26','2024-08-04',50.00,NULL),(2,'Cliente de Prueba 2','123 Calle Principal','123-456-7890',1,'192.168.1.100','100M/25M','2024-05-26','2024-06-26',50.00,NULL),(3,'Cliente de Prueba 3','123 Calle Principal','123-456-7890',1,'192.168.1.100','100M/25M','2024-05-26','2024-06-28',50.00,'suspendido'),(4,'Cliente de Prueba 5','123 Calle Principal','123-456-7890',1,'192.168.1.100','100M/25M','2024-05-26','2024-06-26',50.00,NULL),(5,'PC13','123 Calle Principal','123-456-7890',1,'122.122.126.94','100M/25M','2024-04-10','2024-06-11',50.00,NULL),(6,'TUNDERBILD','123 Calle Principal','123-456-7890',1,'122.122.126.98','100M/25M','2024-04-10','2024-05-11',50.00,NULL),(7,'Lap','Lap','09090909',2,'122.122.126.94','100M/20M','2024-05-26','2024-06-28',450.00,'suspendido'),(8,'Martin Antonio','Socorro','4976542312',2,'122.122.125.92','100M/10M','2024-04-10','2024-06-28',350.00,'suspendido'),(9,'Cliente de Prueba 5','123 Calle Principal','123-456-7890',1,'122.122.126.45','100M/25M','2024-05-26','2024-06-26',300.00,NULL),(10,'Enero','Enero','1234567890',3,'122.122.126.32','100M/25M','2024-01-10','2024-06-26',300.00,NULL),(11,'Febrero','1 de Febrero','0987654321',5,'10.10.1.45','100M/100M','2024-02-01','2024-06-28',450.00,'suspendido'),(12,'Chavez Test','test','6663332211',7,'20.20.1.39','10M/10M','2024-05-26','2024-06-26',800.00,NULL),(13,'Adriana Contreras','Juvrntino Rosas','4961121876',3,'122.122.123.9','100M/15M','2024-05-26','2024-06-26',300.00,NULL),(14,'Victor Daniel','Tec','1234567890',2,'122.122.126.98','100M/20M','2024-01-01','2024-06-28',450.00,'suspendido'),(15,'Fernando','Tec','098766543',2,'122.122.126.88','100M/23M','2024-01-01','2024-02-01',350.00,NULL),(16,'ewew','ewew','33333',1,'122.567.98.3','100M/45M','2024-05-28','2024-06-28',235.00,'suspendido'),(17,'test','test','1234567890',1,'','','2024-05-28','2024-06-28',450.00,'suspendido'),(18,'ewe','ewe','123545454',1,'','wq','2024-05-28','2024-07-29',240.00,'suspendido');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagos`
--

DROP TABLE IF EXISTS `pagos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `NombreCliente` varchar(100) NOT NULL,
  `Mensualidad` decimal(10,2) NOT NULL,
  `FechaPago` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagos`
--

LOCK TABLES `pagos` WRITE;
/*!40000 ALTER TABLE `pagos` DISABLE KEYS */;
INSERT INTO `pagos` VALUES (1,'Cliente de Prueba',50.00,'2024-05-26'),(2,'Cliente de Prueba 2',50.00,'2024-05-26'),(3,'Cliente de Prueba',450.00,'2024-05-26'),(4,'Cliente de Prueba',900.00,'2024-06-05'),(5,'Cliente de Prueba',800.00,'2024-07-04'),(6,'PC12',500.00,'2024-05-11'),(7,'6',500.00,'2024-05-26'),(8,'2',88888.00,'2024-05-26'),(9,'2',50.00,'2024-05-26'),(10,'4',6767670.00,'2024-05-26'),(11,'3',50050.00,'2024-05-26'),(12,'6',54440.00,'2024-05-26'),(13,'5',340.00,'2024-05-26'),(14,'8',350.00,'2024-05-26'),(15,'1',450.00,'2024-05-26'),(16,'1',50.00,'2024-05-26'),(17,'10',300.00,'2024-02-10'),(18,'10',300.00,'2024-05-26'),(19,'11',450.00,'2024-03-02'),(20,'11',550.00,'2024-04-01'),(21,'12',500.00,'2024-06-25'),(22,'13',300.00,'2024-05-26'),(23,'12',800.00,'2024-05-26'),(24,'14',450.00,'2024-02-01'),(25,'14',450.00,'2024-05-28'),(26,'14',450.00,'2024-05-28'),(29,'3',50.00,'2024-05-28'),(30,'3',50.00,'2024-05-28'),(31,'16',235.00,'2024-05-28'),(32,'16',235.00,'2024-05-28'),(33,'7',450.00,'2024-05-28'),(34,'8',350.00,'2024-05-28'),(35,'3',50.00,'2024-05-28'),(36,'11',450.00,'2024-05-28'),(37,'18',240.00,'2024-06-28');
/*!40000 ALTER TABLE `pagos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-28 23:27:15
