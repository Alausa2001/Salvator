-- MySQL dump 10.13  Distrib 5.7.40, for Linux (x86_64)
--
-- Host: localhost    Database: salvator_db
-- ------------------------------------------------------
-- Server version	5.7.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `biodata`
--

DROP TABLE IF EXISTS `biodata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `biodata` (
  `id` varchar(70) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `med_id` varchar(70) NOT NULL,
  `first_name` varchar(75) NOT NULL,
  `last_name` varchar(75) NOT NULL,
  `genotype` varchar(4) NOT NULL,
  `blood_group` varchar(2) NOT NULL,
  `age` int(11) NOT NULL,
  `height` float DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `allergies` varchar(450) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `med_id` (`med_id`),
  CONSTRAINT `biodata_ibfk_1` FOREIGN KEY (`med_id`) REFERENCES `login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biodata`
--

LOCK TABLES `biodata` WRITE;
/*!40000 ALTER TABLE `biodata` DISABLE KEYS */;
INSERT INTO `biodata` VALUES ('253e70b1-1e00-4d96-8404-f854b9b00001','2023-01-11 19:44:22','2023-01-11 19:44:22','7bae43e3-231f-4494-9452-f98f0306699f','muz','hab','FG','Z-',120,190,200,'petrol, food, cries'),('46eef24f-843b-46a2-8a6f-8e9f0a780797','2022-12-30 16:31:40','2022-12-30 16:31:40','a0d4d276-e441-4cea-87cb-5d5ce7789eb5','Olabamiji','Adesanya','AS','B+',20,177,67.2,''),('4774f247-7d96-4e50-a3cb-87827cb96483','2022-12-28 16:15:33','2022-12-28 16:15:33','ccdf2c5e-3b13-4cb6-8ab1-d35cfcc0d5a2','Olaitan','Sodiq','AA','A+',20,NULL,NULL,NULL),('69e77965-9e11-4beb-b104-f607ef53e55b','2023-01-09 16:06:39','2023-01-09 16:06:39','fe28a99d-404b-4703-a685-1aa354ca1700','Adunola','Adebisi','AS','B+',32,166,73,'Allergic to house dust mites, pollen, animal hair and mould'),('6c10315a-6348-4b2b-98a7-c1fa4e710b7f','2022-12-30 14:54:04','2022-12-30 14:54:04','21027c76-96ee-4c91-8970-50e6f4137b10','Abolaji','Adedeji','AA','A-',20,176,60,''),('77cb6da1-7645-47c8-b3ec-e26bcef38c61','2023-01-04 15:04:14','2023-01-04 15:04:14','ea4fbc88-1251-48ad-b12d-27bad0be765c','Sani','Ibrahim','AS','A+',22,172,59,'Hay Fever'),('7fddf2a5-90e7-4e0a-bd33-22575b444055','2022-12-31 12:02:44','2022-12-31 12:02:44','ccdf2c5e-3b13-4cb6-8ab1-d35cfcc0d5a2','Olaitan','Sodiq','AA','A+',20,NULL,NULL,NULL),('85e5eef5-18e8-4878-ab41-062056a4f134','2022-12-30 14:29:55','2022-12-30 14:29:55','5e24f99d-2883-4813-b309-0e1f013fda0c','Alalabi','Bamidele','AA','A+',25,175,56,'hay fever'),('891fc7e9-1fe2-4f9f-8ccb-68e82ef3b691','2023-01-08 23:02:57','2023-01-08 23:02:57','f42531c3-d850-4f4b-85ef-553828d888c9','Maria','Johnson','AA','O-',29,171,40,'None'),('89d68aae-922f-4e3d-a88a-46ef1631c5da','2023-01-07 08:59:51','2023-01-07 08:59:51','b0081bac-f929-4e27-ba89-4f6f4278c03d','Abiola','Adebayo','AS','A+',32,175,72,'Hay Fever'),('d26d25f4-3d89-475b-80be-dee2165d7378','2023-01-08 22:30:16','2023-01-08 22:30:16','f42531c3-d850-4f4b-85ef-553828d888c9','Maria','Johnson','AA','O-',29,171,40,'None'),('e084f22f-0d55-4d70-89f0-1a2ccddeb128','2023-01-05 17:52:04','2023-01-05 17:52:04','5dd2ec65-5f7c-445f-922c-291b6fcd9229','Lawal','Aisha','SS','B+',25,165,61,'');
/*!40000 ALTER TABLE `biodata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login` (
  `id` varchar(70) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `username` varchar(204) NOT NULL,
  `password` varchar(256) NOT NULL,
  `email` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('02ed75b3-b86d-4c24-b842-96319403571a','2022-12-27 10:49:15','2022-12-27 10:49:15','sulyman','pbkdf2:sha256:260000$xeYXdDl6RY0lJ9jR$e9d89bb88d13a1fb69f913eb21464bfe27d923309d3beebead6cf62ee79dde40','sultan@test.com'),('0e6ffedc-c235-4bb8-b12a-0823b0e1beb6','2022-12-25 15:50:24','2022-12-25 15:50:24','UserTest1','testing','test@test.com'),('103be159-c6d2-4ce5-98fb-7a011b4b3dde','2023-01-08 23:10:43','2023-01-08 23:10:43','susan','pbkdf2:sha256:260000$QQt02XAZA6bAltW5$7457c020b511e0ab4e1d0d308feacbf99f95e6273f995cb8ec9ec21f4019b833','joshua.oguntola@elizadeuniversity.edu.ng'),('14aa7b7d-77bd-4768-b93f-d24ef8bdd6ca','2023-01-01 18:35:27','2023-01-01 18:35:27','Ade','pbkdf2:sha256:260000$qZiKm2hG4vL1Ndft$dfe99b463ec8ee32d14ba04ee433ed4665eb8e6c472e4b9107394c03765f941c','Ade@gmail.com'),('19e2e3c2-7ed9-4597-ac15-3bfeac8ab5f1','2023-01-09 13:48:00','2023-01-09 13:48:00','Blendo','pbkdf2:sha256:260000$hJK8fD6DOKmxz17P$976267f436324e97ea69d9561f936ef0b8948bb33b012f5a057c10130e26cc0f','blendo@hotmail.com'),('21027c76-96ee-4c91-8970-50e6f4137b10','2022-12-30 14:38:05','2022-12-30 14:38:05','newuser','pbkdf2:sha256:260000$mJI0s64S76yKr9md$8e3b70362e72de8decf1d6319da83d77baa141060b86ee17752088904f63c163','newuser@test.com'),('241e071c-9173-44e7-8c2c-c5ba4a50d916','2022-12-26 20:36:33','2022-12-26 20:36:33','usertest7','pbkdf2:sha256:260000$eNhtRbfbzJmfrOR4$b73a8ac604e595c5abacf76291046f48f96a6aa1d1ca548a1fe4fb8eea1d9a41','usertest7@test.com'),('3d1c0ebb-73e7-4023-a84f-e066116d136e','2022-12-26 20:46:29','2022-12-26 20:46:29','usertest8','pbkdf2:sha256:260000$6uFFmH9dZ6ayU7TI$33f52eb16289007fa4bfb2786e1feca546d8950610145c4139e41614c67eee8f','usertest8@gmail.com'),('48d772e4-a019-41e4-9b27-769a4a3aed95','2023-01-04 14:58:40','2023-01-04 14:58:40','Johnny','pbkdf2:sha256:260000$LAm9ZH5CzWfNL5Dp$0d16811c79d5ebec9aba10edc3a7a3736b38c2128486fb30bc877e76497ba70a','john23@gmail.com'),('4add12ea-e8e8-4cbb-baf9-20418b106904','2023-01-03 17:41:45','2023-01-03 17:41:45','Tani','pbkdf2:sha256:260000$J9jLlsuGfcQ4WiD6$da3c44e9559d569feac8bf15266914b1fae1dd604dbbf8df6380122839da9510','Tani@gmail.com'),('4e45d104-55b9-466a-9d7c-4740dcc4b68e','2022-12-26 14:59:39','2022-12-26 14:59:39','UserTest4','testing','user4@test.com'),('553d5890-b539-46ec-bb1c-1b60113066f3','2022-12-26 15:05:46','2022-12-26 15:05:46','usertest6','usertest','usertest6@test.com'),('5dd2ec65-5f7c-445f-922c-291b6fcd9229','2023-01-05 17:50:46','2023-01-05 17:50:46','Aisha','pbkdf2:sha256:260000$X1XiusrSklepotEd$675aa5b2b933b049171b5175000589b2faa6b1c6a92f23d1675c7cfa1e3d0ada','Aisha@gmail.com'),('5e24f99d-2883-4813-b309-0e1f013fda0c','2022-12-30 14:26:33','2022-12-30 14:26:33','Femi','pbkdf2:sha256:260000$WWWZYuUB71DThyq9$89380af168f5a8113d66309c8c7accaeb58cd2fb8a6670a826bfb527c95e3e6d','alausaabdulqoyum@gmail.com'),('6147237e-c6ec-4c96-b6a7-d814f50b965f','2022-12-26 15:03:02','2022-12-26 15:03:02','usertest5','usertest','usertest4@test.com'),('63efd48c-a193-4e6a-ae56-79a3b5779411','2022-12-26 14:56:46','2022-12-26 14:56:46','UserTest3','testing','user3@test.com'),('7bae43e3-231f-4494-9452-f98f0306699f','2023-01-11 19:42:12','2023-01-11 19:42:12','test_user','pbkdf2:sha256:260000$qTLrHn9zO5Ypchc6$92712273da453eca9a2e656cf2b75b95cb348adc8b9a23249e9bd2adf8b91f69','habmuz1@gmail.com'),('95affa30-3ea8-407d-a959-2e3624e222cf','2022-12-27 12:27:20','2022-12-27 12:27:20','maho','pbkdf2:sha256:260000$EG9lW23A2zfkhO0C$69ee05f212ad0074bf1aa52e0d3ce7a59f94a17b6bc520f5da849475003bda82','test2@test.com'),('9dbdc95c-c939-43ec-9a8b-2c6962cc215a','2022-12-26 14:58:17','2022-12-26 14:58:17','Alabi','Alade2001','Aladei@gmail.com'),('a0d4d276-e441-4cea-87cb-5d5ce7789eb5','2022-12-30 16:29:49','2022-12-30 16:29:49','Banji','pbkdf2:sha256:260000$ZJkWANGTVt98fA8R$e3ec5095cd27a404bd48abba47ed960fadfb6b73c1c19967bed70be969071408','banji@gnail.com'),('aacb294a-3c4a-4c19-8e6d-891ce669612d','2022-12-25 21:45:13','2022-12-25 21:45:13','Abdulqoyum','Feranmi','alausaabdulqoyum28@gmail.com'),('ab4f9388-438c-4d45-b3df-67a7fcbd518e','2022-12-27 11:00:36','2022-12-27 11:00:36','ridwan','pbkdf2:sha256:260000$AVptfxnZeuI6wQjW$8ec9b67ca23db046ccbc91070bab37fde6d71bf2628f694c303752551fc6ff06','sulymann@test.com'),('b0081bac-f929-4e27-ba89-4f6f4278c03d','2023-01-07 08:58:32','2023-01-07 08:58:32','Abiola','pbkdf2:sha256:260000$1xL4VX1OwErK73ns$f13bd17d964461948a6095e94c3bf16cb2576ed3eddb8d5e4460bd329724e727','Abiola@gmail.com'),('b5ac76c9-83e6-4500-a46a-2da4bccd1ef9','2023-01-06 10:37:42','2023-01-06 10:37:42','Khalil','pbkdf2:sha256:260000$UKvKqlKreSmpNb3d$0e9241cb87cd61973a17e8be33f6fea1a217fe37c442aa3ae6814fbe3f9f6c5f','muhammadiidiagbon@gmail.com'),('b9834185-da97-475a-a021-33684c7298f5','2022-12-27 09:58:47','2022-12-27 09:58:47','Validtest1','pbkdf2:sha256:260000$7Dlu6bCHJVdsXhrF$18e26431193c3a7c28f00fca17c19380c7da817d6635a95654c0f054c7479b12','valid1@test.com'),('c3a9ccb1-2ea0-470b-839a-42d72ee2afe5','2022-12-30 14:35:56','2022-12-30 14:35:56','Bolaji','pbkdf2:sha256:260000$mo4z2p2Eo8le0wwz$d8ade024fe7ac6c0546cb313036990f18f2ad4b41b306b3fa90e4a2401c976e5','Bolaji@gmail.com'),('c6d8c8bb-938f-4acd-9a51-76030b10450d','2022-12-26 13:52:02','2022-12-26 13:52:02','Aladi','Alade2001','Alade@gmail.com'),('c73dc129-6a6c-4677-a4c5-d908dda708f6','2022-12-26 14:54:45','2022-12-26 14:54:45','UserTest2','testing','user2@test.com'),('cc8ee07a-7d92-4b06-bcd9-72a5624a309b','2022-12-26 14:32:25','2022-12-26 14:32:25','Abdul','Feranmi','abdulqoyum@gmail.com'),('ccdf2c5e-3b13-4cb6-8ab1-d35cfcc0d5a2','2022-12-28 15:45:10','2022-12-28 15:45:10','Ola','pbkdf2:sha256:260000$xqK1WGAHKyi4qq2o$e781c0283a083d4c68fd817504511b8eb9f90bea4cabef3c4200069df70b28d5','olaitan@test.com'),('ce708362-ab5d-4bc8-9178-b99f357b0fc2','2022-12-28 12:26:03','2022-12-28 12:26:03','test','pbkdf2:sha256:260000$g0WI1a294XgRXonF$002e5f3f22628653d700c5ed6df867104b761a19bd081c6895d916262fc59293','testuser@test.com'),('cfa0ca11-96e1-4d0e-b2b6-e862aa08cc45','2022-12-24 18:29:29','2022-12-24 18:29:29','Alade','Alade2001','Alade@gmail.com'),('d713b240-d01c-4dd9-b6fb-bc3a93a01486','2023-01-09 08:41:14','2023-01-09 08:41:14','Adewale','pbkdf2:sha256:260000$Xmx3mWErpxUrF3Cz$ba982580ae2f044d989df1f57f64f6d677b333900b41a1e588ef2f6b45e642cf','Adewale@rmail.com'),('da7b7b03-ba3a-4892-9d6f-f02f1587fa49','2022-12-28 14:58:30','2022-12-28 14:58:30','testuser','pbkdf2:sha256:260000$jckfCKdQDNpuIvUJ$9f6fae5099413d29751e264e23a88e0b48a37516293827d293367680e5dec8fc','testuser1@test.com'),('e9f56eed-5da1-4c57-809a-700187b46457','2022-12-27 12:15:02','2022-12-27 12:15:02','validtest2','pbkdf2:sha256:260000$qk4QlakJOfGMxZjH$e3959e0ac7ba590cc7d0e2a3c8d6a0fad5cf232599af28f5bf6be2a4c785ada5','valid2@test.com'),('ea4fbc88-1251-48ad-b12d-27bad0be765c','2023-01-03 16:12:21','2023-01-03 16:12:21','Sani','pbkdf2:sha256:260000$u0pfbvpmd5kaK4jn$c3185f72f2c70ef83ba187e2e02391daf5790534c9b998e45107594d97a4e312','Sani@gmail.com'),('ed71ae8e-360d-4ab7-a0d8-9009dd882954','2023-01-10 11:18:48','2023-01-10 11:18:48','Aderinsola','pbkdf2:sha256:260000$4DhVIjb3AzjrZiap$4169257ebde2cca7086a53a87b40ba20185f16625b3481399fda6099ef6f6618','Aderinsola2001@gmail.com'),('f42531c3-d850-4f4b-85ef-553828d888c9','2023-01-08 22:21:43','2023-01-08 22:21:43','joshua','pbkdf2:sha256:260000$9KHbnxndANqU34fU$1a8e16b57791a03135705a44cff7195f5a4d05ddb16b1bb91803fa65b03f9dbb','jeomade19@gmail.com'),('fe28a99d-404b-4703-a685-1aa354ca1700','2023-01-09 08:48:25','2023-01-09 08:48:25','Adebisi','pbkdf2:sha256:260000$KtDsybzwNRtMZgaP$0aec987aaef3ba515dac01334b1447d8ea13cd43133ce2523baab49f2f11fdbb','AdebisiAdunola@gmail.com');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `records`
--

DROP TABLE IF EXISTS `records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `records` (
  `id` varchar(70) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `records_id` varchar(70) NOT NULL,
  `date` varchar(40) NOT NULL,
  `diagnosis` varchar(450) NOT NULL,
  `prescription` varchar(450) NOT NULL,
  `hospital` varchar(450) DEFAULT NULL,
  `doctor_name` varchar(450) DEFAULT NULL,
  `doctor_contact` varchar(450) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `records_id` (`records_id`),
  CONSTRAINT `records_ibfk_1` FOREIGN KEY (`records_id`) REFERENCES `login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `records`
--

LOCK TABLES `records` WRITE;
/*!40000 ALTER TABLE `records` DISABLE KEYS */;
INSERT INTO `records` VALUES ('2df13321-9faf-4823-9e23-eb155b498aa4','2023-01-05 17:50:02','2023-01-05 17:50:02','ea4fbc88-1251-48ad-b12d-27bad0be765c','Thu, 05 Jan 2023 18:49:00 GMT','Malaria','Artesunate',NULL,NULL,NULL),('345cd9e2-5eb3-431b-b816-a0bb336397f2','2023-01-05 14:47:21','2023-01-05 14:47:21','48d772e4-a019-41e4-9b27-769a4a3aed95','Fri, 10 Feb 2023 17:47:00 GMT','Headache','Rest well',NULL,NULL,NULL),('4a110210-210a-4333-9e8a-1cbcc41e6b35','2022-12-31 16:59:16','2022-12-31 16:59:16','b9834185-da97-475a-a021-33684c7298f5','Thu, 03 Nov 2022 19:58:00 GMT','Fatigue','Rest well',NULL,NULL,NULL),('4aa2042c-b959-40bb-a8e9-ac529076681f','2022-12-31 16:50:12','2022-12-31 16:50:12','b9834185-da97-475a-a021-33684c7298f5','Sat, 03 Dec 2022 18:50:00 GMT','Cold','Procold',NULL,NULL,NULL),('5dff213f-bba9-479e-8701-d53d20579a7e','2022-12-31 12:25:31','2022-12-31 12:25:31','21027c76-96ee-4c91-8970-50e6f4137b10','Sat, 31 Dec 2022 00:00:00 GMT','Malaria','Amoxyclin 200mg, Paracetamol 200mg',NULL,NULL,NULL),('5f8bfee3-f0ae-4bdf-8c83-ae54a2fd35de','2022-12-31 15:52:23','2022-12-31 15:52:23','21027c76-96ee-4c91-8970-50e6f4137b10','Wed, 30 Nov 2022 17:47:00 GMT','Headache','Rest well',NULL,NULL,NULL),('6bda7fe4-e676-4ec1-a0ce-f43382427038','2022-12-31 14:32:53','2022-12-31 14:32:53','21027c76-96ee-4c91-8970-50e6f4137b10','Thu, 08 Dec 2022 00:00:00 GMT','Fever','Ibuprofen, Aspirin',NULL,NULL,NULL),('6de14817-a63a-4221-ab5e-8944b06e1b15','2022-12-31 14:34:57','2022-12-31 14:34:57','21027c76-96ee-4c91-8970-50e6f4137b10','Mon, 05 Dec 2022 00:00:00 GMT','Pile','Loxagyl 500mg',NULL,NULL,NULL),('71b75665-853d-4721-87d1-c5e951e61fb7','2023-01-05 14:50:32','2023-01-05 14:50:32','48d772e4-a019-41e4-9b27-769a4a3aed95','Fri, 20 Jan 2023 17:50:00 GMT','Carter','Procold',NULL,NULL,NULL),('720e0fbb-b3fa-45d8-b62a-b21a283cc2cd','2023-01-04 15:05:17','2023-01-04 15:05:17','ea4fbc88-1251-48ad-b12d-27bad0be765c','Thu, 04 Jan 2018 18:04:00 GMT','Malaria','Chloramphenicol',NULL,NULL,NULL),('7308044c-7f93-416e-838c-0b53e1d8b337','2023-01-04 16:30:58','2023-01-04 16:30:58','5e24f99d-2883-4813-b309-0e1f013fda0c','Wed, 04 Jan 2023 17:30:00 GMT','Cough','Procold',NULL,NULL,NULL),('7a3a9498-73e5-4c96-9ec9-46782809d507','2022-12-31 14:29:30','2022-12-31 14:29:30','21027c76-96ee-4c91-8970-50e6f4137b10','Fri, 16 Dec 2022 00:00:00 GMT','Pile','Loxagyl 400mg',NULL,NULL,NULL),('7bca0967-4a99-43b1-8bbc-efabcf2d6567','2022-12-31 15:53:25','2022-12-31 15:53:25','21027c76-96ee-4c91-8970-50e6f4137b10','Sat, 17 Dec 2022 18:53:00 GMT','Fever','Ibupofen, Aspirin',NULL,NULL,NULL),('8d0fa39f-c641-4eeb-8e65-0b85ca99a49f','2022-12-31 16:53:03','2022-12-31 16:53:03','b9834185-da97-475a-a021-33684c7298f5','Thu, 22 Dec 2022 18:52:00 GMT','Fever','Amocillin',NULL,NULL,NULL),('8d9627c5-ace4-46b0-a15a-03dcc47c5d7c','2022-12-31 15:58:05','2022-12-31 15:58:05','21027c76-96ee-4c91-8970-50e6f4137b10','Wed, 21 Dec 2022 17:06:00 GMT','Headache','Rest well',NULL,NULL,NULL),('97cd631b-c6de-43d0-9baa-6cc591d2fc60','2023-01-05 12:07:21','2023-01-05 12:07:21','48d772e4-a019-41e4-9b27-769a4a3aed95','Wed, 18 Jan 2023 09:07:00 GMT','Malaria','Artemeter',NULL,NULL,NULL),('ba360016-d5d4-4e08-ba99-b138e97bc5b0','2023-01-09 16:11:40','2023-01-09 16:11:40','fe28a99d-404b-4703-a685-1aa354ca1700','Fri, 09 Sep 2022 16:06:00 GMT','Pulmonary fibrosis','I was placed on Pulmonary rehabilitation and Oxygen therapy',NULL,NULL,NULL),('be7d7cf0-a8dc-4fd9-a3d3-c02dcad8df11','2023-01-05 14:46:10','2023-01-05 14:46:10','48d772e4-a019-41e4-9b27-769a4a3aed95','Wed, 11 Jan 2023 03:47:00 GMT','Malaria','Artemeter',NULL,NULL,NULL),('c7cd3283-f3ad-4a48-8287-307ce3023a33','2022-12-31 14:27:37','2022-12-31 14:27:37','21027c76-96ee-4c91-8970-50e6f4137b10','Thu, 22 Dec 2022 00:00:00 GMT','Ulcer','Mist-mag suspension',NULL,NULL,NULL),('c90546da-41b5-43b0-81f5-d1ae3411bb57','2023-01-05 14:20:41','2023-01-05 14:20:41','48d772e4-a019-41e4-9b27-769a4a3aed95','Wed, 18 Jan 2023 18:21:00 GMT','Malaria','Artemeter',NULL,NULL,NULL),('cb3ffd71-20eb-4502-a831-077a9f023926','2023-01-05 14:52:02','2023-01-05 14:52:02','48d772e4-a019-41e4-9b27-769a4a3aed95','Wed, 25 Jan 2023 12:51:00 GMT','Ulcer','Gestid',NULL,NULL,NULL),('db943ba6-1de8-4478-9d4c-5b364eaa3b55','2023-01-05 17:04:37','2023-01-05 17:04:37','48d772e4-a019-41e4-9b27-769a4a3aed95','Tue, 10 Jan 2023 07:04:00 GMT','Ulcer','Gestid',NULL,NULL,NULL),('fa4a7655-830a-4060-99d1-a51edc40ad0f','2023-01-04 15:06:08','2023-01-04 15:06:08','ea4fbc88-1251-48ad-b12d-27bad0be765c','Sun, 04 Dec 2022 16:05:00 GMT','Cholera','Nothing',NULL,NULL,NULL),('fd38684b-991f-4c61-8c86-cd7e432e53dd','2023-01-05 14:13:36','2023-01-05 14:13:36','48d772e4-a019-41e4-9b27-769a4a3aed95','Tue, 10 Jan 2023 17:12:00 GMT','Headache','Rest well',NULL,NULL,NULL),('fef6257f-5dcf-40d4-9e78-e76ef66e1549','2022-12-31 16:39:33','2022-12-31 16:39:33','b9834185-da97-475a-a021-33684c7298f5','Thu, 01 Dec 2022 09:38:00 GMT','Cough','Tutolin syrup',NULL,NULL,NULL);
/*!40000 ALTER TABLE `records` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-12  0:27:38
