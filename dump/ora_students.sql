-- MySQL dump 10.13  Distrib 5.5.62, for Linux (x86_64)
--
-- Host: localhost    Database: novsu
-- ------------------------------------------------------
-- Server version	5.5.62-log

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
-- Table structure for table `ora_students`
--

DROP TABLE IF EXISTS `ora_students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ora_students` (
  `STD_ID` bigint(20) DEFAULT NULL,
  `MAN_ID` bigint(20) DEFAULT NULL,
  `SURNAME` varchar(60) NOT NULL DEFAULT '',
  `NAME` varchar(60) NOT NULL DEFAULT '',
  `PATRON` varchar(60) NOT NULL DEFAULT '',
  `SEX` varchar(10) DEFAULT NULL,
  `STATE_NAME_SH` varchar(10) DEFAULT NULL,
  `PHONE` varchar(80) DEFAULT NULL,
  `S_GRP_ID` bigint(20) DEFAULT NULL,
  `STATUS` varchar(50) DEFAULT NULL,
  `KATEG_ST` varchar(50) DEFAULT NULL,
  `NEUD` varchar(10) DEFAULT NULL,
  `DIFF_PLAN` varchar(10) DEFAULT NULL,
  `GRAFIK` varchar(10) DEFAULT NULL,
  `DOCUMENT` varchar(10) DEFAULT NULL,
  `MIL_KAF` varchar(10) DEFAULT NULL,
  `D_BEGIN` date DEFAULT NULL,
  `D_END` date DEFAULT NULL,
  `CHIEF` varchar(10) DEFAULT NULL,
  `KATEGOR` varchar(50) DEFAULT NULL,
  `DATA_PO` date DEFAULT NULL,
  `BASE` varchar(50) DEFAULT NULL,
  `DATA_S` date DEFAULT NULL,
  `COURCE` bigint(20) DEFAULT NULL,
  `DSPE_ID` bigint(20) DEFAULT NULL,
  `GRP_NAME` varchar(20) DEFAULT NULL,
  `GOD_POST` date DEFAULT NULL,
  `FS_ID` bigint(20) DEFAULT NULL,
  `LOCATION` varchar(100) DEFAULT NULL,
  `SHORT_NAME` varchar(20) DEFAULT NULL,
  `FS_NAME` varchar(100) DEFAULT NULL,
  `FORM_STUDY` varchar(10) DEFAULT NULL,
  `SPEED` varchar(10) DEFAULT NULL,
  `LENGTH` float DEFAULT NULL,
  `BASEO` varchar(10) DEFAULT NULL,
  `SPE_SHIFR` varchar(20) DEFAULT NULL,
  `SPE_SHIFR7` varchar(20) DEFAULT NULL,
  `FAK_ID` bigint(20) DEFAULT NULL,
  `SHIFR_SP_UNI` varchar(30) DEFAULT NULL,
  `NAME_SP_UNI` varchar(30) DEFAULT NULL,
  `FAC_NAME_SH` varchar(30) DEFAULT NULL,
  `INST_NAME` varchar(30) DEFAULT NULL,
  `FAC_NAME` varchar(200) DEFAULT NULL,
  `SPEC_NAME` varchar(8000) DEFAULT NULL,
  `SPZ_NAME` varchar(8000) DEFAULT NULL,
  `QUALIF` varchar(200) DEFAULT NULL,
  `CODE_SPEC` varchar(20) DEFAULT NULL,
  `MARITAL` varchar(20) DEFAULT NULL,
  `BIRTHDAY` date DEFAULT NULL,
  `DOPUSK_DIP` bigint(20) DEFAULT NULL,
  `AC_STEP` varchar(30) DEFAULT NULL,
  `LAST_CO_ID` bigint(20) DEFAULT NULL,
  `ENTER_YEAR` bigint(20) DEFAULT NULL,
  `FSDS_ID` bigint(20) DEFAULT NULL,
  `STIP_1K` varchar(10) DEFAULT NULL,
  `LEV` varchar(20) DEFAULT NULL,
  `VIRT_GRP` int(11) DEFAULT NULL,
  `snils4` varchar(4) DEFAULT NULL,
  `birthday_day` int(11) DEFAULT NULL,
  `birthday_month` int(11) DEFAULT NULL,
  KEY `MAN_ID` (`MAN_ID`),
  KEY `STD_ID` (`STD_ID`),
  KEY `S_GRP_ID` (`S_GRP_ID`),
  KEY `GRP_NAME` (`GRP_NAME`),
  KEY `BIRTHDAY` (`BIRTHDAY`),
  KEY `SURNAME` (`SURNAME`,`NAME`,`PATRON`),
  KEY `birthday_month` (`birthday_month`,`birthday_day`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ora_students`
--
-- WHERE:  STD_ID=217942

LOCK TABLES `ora_students` WRITE;
/*!40000 ALTER TABLE `ora_students` DISABLE KEYS */;
INSERT INTO `ora_students` VALUES (217942,245091,'БОГДАНОВ','МИХАИЛ','МИХАЙЛОВИЧ','М','RUS','+79524829183 79116233486',39208,'СТ','БП','','Н','Н','Н','','2023-09-01','1999-11-30','Н','КОНКУРС','3000-01-01','СП','2023-09-29',1,3178,'3094','2023-09-01',106,'','ду','очная ускоренная','Д','Д',2,'СП','09.03.01','',63,'01','','ОИНФ','ИЭИС','Отделение информатики','Информатика и вычислительная техника','Программное обеспечение вычислительной техники и автоматизированных систем','','09','','2003-04-14',0,'БАК',-105,2023,24912,'Д','64',432,'9474',14,4);
/*!40000 ALTER TABLE `ora_students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-25 11:27:10
