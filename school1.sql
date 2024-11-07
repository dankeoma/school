-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: school
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `api_logs`
--

DROP TABLE IF EXISTS `api_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_logs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `IP` varchar(255) DEFAULT NULL,
  `request` json DEFAULT NULL,
  `response` json DEFAULT NULL,
  `route` varchar(255) DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `status` tinyint DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_logs`
--

LOCK TABLES `api_logs` WRITE;
/*!40000 ALTER TABLE `api_logs` DISABLE KEYS */;
INSERT INTO `api_logs` VALUES (1,'127.1.1.0.1','{\"Age\": 30, \"Name\": \"Daniel\"}','{\"Gender\": \"Male\", \"Status\": \"Single\"}','/login','2024-10-06 22:45:51',1),(2,'request.remote_addr','{\"userid\": \"userid\", \"password\": \"password\"}','{\"userid\": \"userid\", \"password\": \"password\"}','request.path','2024-10-06 23:20:00',1),(3,'127.0.0.1','{\"userid\": \"userid\", \"password\": \"password\"}','{\"userid\": \"userid\", \"password\": \"password\"}','/login/','2024-10-06 23:21:16',1),(4,'127.1.1.0.1','{\"Age\": 30, \"Name\": \"Daniel\"}','{\"Gender\": \"Male\", \"Status\": \"Single\"}','/login','2024-10-07 00:16:01',1),(5,NULL,'{\"userid\": \"userid\", \"password\": \"password\"}','{\"userid\": \"userid\", \"password\": \"password\"}',NULL,'2024-10-07 00:26:58',1),(6,'127.0.0.1','{\"userid\": \"userid\", \"password\": \"password\"}','{\"userid\": \"userid\", \"password\": \"password\"}','/login/','2024-10-07 00:45:37',1),(7,'127.0.0.1','{\"userid\": \"STF-6998\", \"password\": \"password\"}','{\"userid\": \"userid\", \"password\": \"password\"}','/login/','2024-10-07 00:49:25',1),(8,'127.0.0.1','{\"userid\": \"STF-6998\", \"password\": \"dankeuto\"}','{\"userid\": \"STF-6998\", \"password\": \"dankeuto\"}','/login/','2024-10-07 01:09:24',1),(9,'127.0.0.1','{\"userid\": \"STF-6998\", \"password\": \"dankeuto\"}','{\"staffID\": \"STF-6998\", \"staffName\": \"dankeuto\"}','/login/','2024-10-07 01:10:51',1),(10,'127.0.0.1','{\"userid\": \"STF-6998\", \"password\": \"dankeuto\"}','{\"staffID\": \"STF-6998\", \"staffName\": \"Paul Mbaebie\"}','/login/','2024-10-07 01:11:59',1),(11,'127.0.0.1','{\"StaffID\": 5, \"staffName\": 5}','{\"StaffID\": 5, \"staffName\": 5}','/login/','2024-10-07 12:39:43',1),(12,'127.0.0.1','{\"UserID\": \"STF-6998\", \"Password\": \"dankeuto\"}','{\"StaffID\": 5, \"staffName\": \"Paul Mbaebie\"}','/login/','2024-10-07 12:51:53',1),(13,'127.0.0.1','{\"UserID\": \"STF-6998\", \"Password\": \"dankeuto\"}','{\"StaffID\": 5, \"staffName\": \"Paul Mbaebie\"}','/login/','2024-10-20 19:41:01',1),(14,'127.0.0.1','{\"UserID\": \"STF-6998\", \"Password\": \"dankeuto\"}','{\"StaffID\": 5, \"staffName\": \"Paul Mbaebie\"}','/login/','2024-10-20 21:23:29',1),(15,'127.0.0.1','{\"UserID\": \"STF-6998\", \"Password\": \"dankeuto\"}','{\"StaffID\": 5, \"staffName\": \"Paul Mbaebie\"}','/login/','2024-10-20 22:34:18',1);
/*!40000 ALTER TABLE `api_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `course_id` int NOT NULL AUTO_INCREMENT,
  `course_title` varchar(225) DEFAULT NULL,
  `course_code` varchar(50) DEFAULT NULL,
  `course_lecturer` varchar(225) DEFAULT NULL,
  `department_id` int DEFAULT NULL,
  `status` tinyint DEFAULT (1),
  PRIMARY KEY (`course_id`),
  KEY `department_id` (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES (1,'Physics Methods','PHS110','Engr. GKC',1,1),(2,'Electrical Conductors','EE210','Engr Mbaatu',2,1),(3,'Animal Husbandry','AG350','Modikpe Maureen',3,1),(4,'Blood Movement','MED240','Dr Mgbemene',4,1),(5,'Python Move','COMP210','Mr Paul',5,1),(6,'Classroom Ethics','EDU101','Mrs Somtochukwu',6,1),(7,'Physics','PHS110','Engr. GKC',1,1),(8,'Wood Work','WW210','Engr Mbaatu',1,1),(9,'Mechanical Issues','ML350','Azaka Umuwa',1,1),(10,'Tiper Measure','TP240','Dr Akalaka Mbaiwe',1,1),(11,'Vibration Move','VABOS210','Mr Mpanaka',1,1),(12,'Material Method','MTHD101','Mrs Akuruo Ngbemene',1,1);
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `deptID` int NOT NULL AUTO_INCREMENT,
  `deptName` varchar(100) DEFAULT NULL,
  `deptAbrv` varchar(225) DEFAULT NULL,
  `facID` int DEFAULT NULL,
  `deptCode` varchar(50) DEFAULT NULL,
  `status` tinyint DEFAULT (1),
  `createdBy` int DEFAULT NULL,
  `createdAt` date DEFAULT NULL,
  PRIMARY KEY (`deptID`),
  UNIQUE KEY `dept_name` (`deptName`),
  UNIQUE KEY `deptNo` (`deptCode`),
  UNIQUE KEY `deptAbrv` (`deptAbrv`),
  KEY `frk_deptFac` (`facID`),
  KEY `frk_deptcreatedByStaff` (`createdBy`),
  CONSTRAINT `frk_deptcreatedByStaff` FOREIGN KEY (`createdBy`) REFERENCES `staff` (`staffID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `frk_deptFac` FOREIGN KEY (`facID`) REFERENCES `faculty` (`facID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (18,'Animal Science','AnSc',1,'82MY',1,NULL,NULL),(19,'Crop Science','CrSc',1,'27OL',1,NULL,NULL),(20,'Agricultural Economic and Extension','AgEcEx',1,'31PY',1,NULL,NULL),(21,'Food Science and Technology','FoScTe',1,'57NJ',1,NULL,NULL),(22,'Forestly and Wildlife','FoWi',1,'83UM',1,NULL,NULL),(23,'Soil Science','SoSc',1,'36VH',1,NULL,NULL),(24,'Igbo, African and Asian Studies','IgAfAsSt',2,'37SS',1,NULL,NULL),(25,'English Language and Literature','EnLaLi',2,'60ZL',1,NULL,NULL),(26,'History and International Studies','HiInSt',2,'74LU',1,NULL,NULL),(27,'Linguistics','Li',2,'61HX',1,NULL,NULL),(28,'Modern Europian Languages','MoEuLa',2,'47KQ',1,NULL,NULL),(29,'Music','Mu',2,'61PI',1,NULL,NULL),(30,'Applied Biochemistry','ApBi',3,'39KM',1,NULL,NULL),(31,'Paracitology and Entomology','PaEn',3,'56DT',1,NULL,NULL),(32,'Applied Microbiology and Brewing','ApMiBr',3,'93CH',1,NULL,NULL),(33,'Botany','Bo',3,'62XX',1,NULL,NULL),(34,'Zoology','Zo',3,'71GU',1,NULL,NULL);
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deptstudent`
--

DROP TABLE IF EXISTS `deptstudent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deptstudent` (
  `reg_id` int NOT NULL AUTO_INCREMENT,
  `stuID` int DEFAULT NULL,
  `deptID` int DEFAULT NULL,
  `stuNo` varchar(50),
  `regYear` year DEFAULT NULL,
  `status` tinyint DEFAULT (1),
  PRIMARY KEY (`reg_id`),
  KEY `frk_deptstuDept` (`deptID`),
  KEY `frk_deptstuStu` (`stuID`),
  CONSTRAINT `frk_deptstuDept` FOREIGN KEY (`deptID`) REFERENCES `department` (`deptID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `frk_deptstuStu` FOREIGN KEY (`stuID`) REFERENCES `student` (`stuID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deptstudent`
--

LOCK TABLES `deptstudent` WRITE;
/*!40000 ALTER TABLE `deptstudent` DISABLE KEYS */;
INSERT INTO `deptstudent` VALUES (5,8,34,'00001',2023,1),(6,10,29,'00002',2023,1),(7,11,29,'00003',2023,1),(8,12,33,'00004',2023,1),(9,13,33,'00001',2024,1),(10,19,18,'00002',2024,1),(11,21,18,'00003',2024,1),(12,23,29,'00004',2024,1),(13,25,29,'00005',2024,1),(14,26,33,'00006',2024,1),(15,27,33,'00007',2024,1),(16,28,33,'00008',2024,1),(17,29,33,'00009',2024,1),(18,30,19,'00010',2024,1),(19,31,19,'00011',2024,1);
/*!40000 ALTER TABLE `deptstudent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty`
--

DROP TABLE IF EXISTS `faculty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faculty` (
  `facID` int NOT NULL AUTO_INCREMENT,
  `facName` varchar(225) DEFAULT NULL,
  `facDean` varchar(225) DEFAULT NULL,
  `progID` int DEFAULT NULL,
  `status` int DEFAULT (1),
  PRIMARY KEY (`facID`),
  KEY `frk_progFac` (`progID`),
  CONSTRAINT `frk_progFac` FOREIGN KEY (`progID`) REFERENCES `program` (`progID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty`
--

LOCK TABLES `faculty` WRITE;
/*!40000 ALTER TABLE `faculty` DISABLE KEYS */;
INSERT INTO `faculty` VALUES (1,'AGRICULTURE',NULL,1,1),(2,'ARTS',NULL,1,1),(3,'BIOSCIENCE',NULL,1,1),(4,'EDUCATION',NULL,1,1),(5,'ENGINEERING',NULL,1,1),(6,'MEDICINE',NULL,1,1),(7,'BASIC MEDICAL SCIENCES',NULL,1,1),(8,'ENVIRONMENTAL SCIENCES',NULL,1,1),(9,'HEALTH SCIENCES AND TECHNOLOGY',NULL,1,1),(10,'LAW',NULL,1,1),(11,'MANAGEMENT SCIENCES',NULL,1,1),(12,'MEDICAL LABORATORY SCIENCES',NULL,1,1);
/*!40000 ALTER TABLE `faculty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `params`
--

DROP TABLE IF EXISTS `params`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `params` (
  `paramID` int NOT NULL AUTO_INCREMENT,
  `apiKey` varchar(255) DEFAULT NULL,
  `vendorCode` varchar(255) DEFAULT NULL,
  `vendor` varchar(100) DEFAULT NULL,
  `createdAt` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `expiresAt` datetime DEFAULT NULL,
  `db` varchar(100) DEFAULT NULL,
  `status` tinyint DEFAULT '1',
  PRIMARY KEY (`paramID`),
  UNIQUE KEY `apiKey` (`apiKey`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `params`
--

LOCK TABLES `params` WRITE;
/*!40000 ALTER TABLE `params` DISABLE KEYS */;
INSERT INTO `params` VALUES (1,'5LU7#3UD4UXICLFU@072W5$BP','2576885106','University of Nigeria Nsuka','2024-10-06 01:08:08','2025-01-06 00:00:00','school',1);
/*!40000 ALTER TABLE `params` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `program`
--

DROP TABLE IF EXISTS `program`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `program` (
  `progID` int NOT NULL AUTO_INCREMENT,
  `progName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`progID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `program`
--

LOCK TABLES `program` WRITE;
/*!40000 ALTER TABLE `program` DISABLE KEYS */;
INSERT INTO `program` VALUES (1,'Undergraduate'),(2,'Postgraduate'),(3,'Continuing Education(CEP)'),(4,'Pre_science Programme'),(5,'Sandwich Programme'),(6,'JUPEB Programme'),(7,'Certificate Programme');
/*!40000 ALTER TABLE `program` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `staffID` int NOT NULL AUTO_INCREMENT,
  `staffName` varchar(100) DEFAULT NULL,
  `staffNo` varchar(100) DEFAULT NULL,
  `staffEmail` varchar(100) DEFAULT NULL,
  `staffPhone` varchar(100) DEFAULT NULL,
  `password` varchar(225) DEFAULT NULL,
  PRIMARY KEY (`staffID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (4,'Nwankwo Odinga','STF-1720','nwankwodaniel287@gmail.com','08069161366','$2b$12$XBUelH3IOsT7ZDLmyV8z6OuFZfYbwD2bqCbJiied1jRXQrInUSKcO'),(5,'Paul Mbaebie','STF-6998','nwankwodaniel287@gmail.com','08069161366','$2b$12$ogT/ETxWtVI7AfBrLEEuR.vmUfrNNi6CLF35G7P4DP8oTl8/iz4Ya'),(6,'Paul Mbaebie','STF-5015','nwankwodaniel281@gmail.com','08069161366','$2b$12$aNVKp35JQZmwT5fGk3UySewDPjChvZkYD3sju0MZ8Xw5QFmx2EMFW');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `stuID` int NOT NULL AUTO_INCREMENT,
  `fullName` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `regNo` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `regNoGenerated` tinyint DEFAULT '0',
  `regNoGeneratedBy` int DEFAULT NULL,
  `regNoGeneratedAt` date DEFAULT NULL,
  `createdBy` int DEFAULT NULL,
  `createdAt` date DEFAULT NULL,
  PRIMARY KEY (`stuID`),
  UNIQUE KEY `regNo` (`regNo`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  KEY `frk_regNoGenByStu` (`regNoGeneratedBy`),
  KEY `frk_createdByStaff` (`createdBy`),
  CONSTRAINT `frk_createdByStaff` FOREIGN KEY (`createdBy`) REFERENCES `staff` (`staffID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `frk_regNoGenByStu` FOREIGN KEY (`regNoGeneratedBy`) REFERENCES `staff` (`staffID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (8,'Nwankwo Daniel','08069919940',20,'Anambra','202371GU00001','$2b$12$73B9SFs0nEnwcafymn5xhO1p1bIX1HzdjosPPIGnbXZ7OcN7YEfQC','utenketere284@gmail.com',1,4,'2024-09-26',NULL,NULL),(10,'Okeke Udoka','08069919941',25,'Anambra','202361PI00002','$2b$12$4kIicgas2hrsNgUi6IiSw.TRA.jn2PpvoO9wAaXs9wU08/WmNRZc.','utenketere280@gmail.com',1,4,'2024-09-26',NULL,NULL),(11,'Muoka Jude','08069919942',25,'Anambra','202361PI00003','$2b$12$Uq18aTAMtSfNqnb8Y5g1qusnnjh8n8X58KUGolyTiUB9XEZgxQFgm','utenketere281@gmail.com',1,4,'2024-09-26',NULL,NULL),(12,'Mmadu Okilo','08069919943',25,'Anambra','202362XX00004','$2b$12$GypAlLlAxrY5fCJ8rI/.BOcMz6R1FRbkWl3PEAIpjdIojVxi65Kwu','utenketere282@gmail.com',1,4,'2024-09-26',NULL,NULL),(13,'Adaka Case','08069919944',25,'Anambra','202462XX00001','$2b$12$ZUPYsv3CmJ7ort0b7q35o.oAyd..BU4Qy5XcYG4Ei2JvfgdCWI/ai','utenketere283@gmail.com',1,4,'2024-09-26',NULL,NULL),(19,'Nwando Mary','08069919946',25,'Anambra','202482MY00002','$2b$12$vgv/aoIaSVZvhy44EvXaHOGYM90x7dGXivlgouYo300E26ku8NF3i','utenketere285@gmail.com',1,4,'2024-09-26',NULL,NULL),(21,'Azubike Nkiru','08069919945',25,'Anambra','202482MY00003','$2b$12$kuA65wnBDjgUCHFfMy19buQv.F/.Vdsq6qYNN/C.cVSaYlInZ7dZ.','utenketere286@gmail.com',1,5,'2024-09-26',NULL,NULL),(23,'Makus Muo','08069919947',25,'Abuja','202461PI00004','$2b$12$oABfQ.xIKVNXVga8c3AWuuFN7gKcM/DMIk1AvtCknIzALBU7eS.HC','utenketere287@gmail.com',1,5,'2024-09-26',NULL,NULL),(25,'Mary Nnedimma','08069919948',26,'Imo','202461PI00005','$2b$12$Hmt.sh7j62wUmsTocH22peDKPMwQMB9Dnf.igRTJHVV5KpP751uv.','utenketere288@gmail.com',1,5,'2024-09-26',4,'2024-09-26'),(26,'Ofodile Ndudi','08069919949',26,'Imo','202462XX00006','$2b$12$tQXi3obFHAZiIwcjttsmO.p0MS7ztZFQg1gImFMWommXUkZsBTeRO','utenketere289@gmail.com',1,5,'2024-09-26',4,'2024-09-26'),(27,'Chukwuemeka Odumegwu Ojukwu','08069919950',26,'Imo','202462XX00007','$2b$12$pDWJC9l1Xc13XrUWoa.9yukfTU4221nVPRbxd/EyaPuHh6OfIhHHm','utenketere290@gmail.com',1,5,'2024-09-26',4,'2024-09-26'),(28,'Nnamdi Kanu','08069919951',26,'Imo','202462XX00008','$2b$12$j.PKRd8n9/REboQ8wkC2CefiAMwfB.F2D.w3d/.euPY9PMYN/oBjq','utenketere291@gmail.com',1,5,'2024-09-26',4,'2024-09-26'),(29,'Tinubu ','08069919952',26,'Imo','202462XX00009','$2b$12$JQTWiKNKdY8EQeNeoY/yqOxnpx9zpRu.sbuPiKo9BN5QnA34A6hrq','utenketere292@gmail.com',1,5,'2024-09-26',4,'2024-09-26'),(30,'Muhamed Buhari','08069919953',26,'Kastina','202427OL00010','$2b$12$2h69UQ/rW8zI0lGRT4Onk.sChDAF/sP0db0hNzzO.TLhWzgY4XlnK','utenketere293@gmail.com',1,5,'2024-09-26',4,'2024-09-26'),(31,'Rochas Okorocha','08069919954',26,'Sokoto','202427OL00011','$2b$12$TDdmrGiRUdP6izfY1/ZAk.gSpX.stMsvN1lNMDJv/b9nvSVnW1VXO','utenketere294@gmail.com',1,5,'2024-09-26',4,'2024-09-26');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-21  0:29:52
