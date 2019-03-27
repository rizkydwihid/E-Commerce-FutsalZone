-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: portofolio
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

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
-- Table structure for table `Cart`
--

DROP TABLE IF EXISTS `Cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cart` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `produk_id` int(11) NOT NULL,
  `cust_id` int(11) NOT NULL,
  `nama_cust` varchar(100) NOT NULL,
  `nama_barang` varchar(100) NOT NULL,
  `kategori` varchar(100) NOT NULL,
  `qty` float NOT NULL,
  `total_byr` float NOT NULL,
  `transaksi_id` int(11) NOT NULL,
  `status` varchar(20) NOT NULL,
  `gambar` varchar(255) NOT NULL,
  PRIMARY KEY (`cart_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cart`
--

LOCK TABLES `Cart` WRITE;
/*!40000 ALTER TABLE `Cart` DISABLE KEYS */;
INSERT INTO `Cart` VALUES (10,1,4,'Bakri','DYNAMITE','sepatu futsal',1,350000,0,'Belum di bayar','https://i.postimg.cc/pyCfvSNc/swervo-dynamite.jpg'),(11,7,10,'deny','CATALYS MISTIQUE','sepatu futsal',1,420000,0,'Belum di bayar','https://i.postimg.cc/Y2mdL2f8/catalys-mistique2.jpg'),(12,2,10,'deny','APACHE ARTIC','sepatu futsal',1,255000,0,'Belum di bayar','https://i.postimg.cc/nCwqjQhv/apache-merah.png'),(13,2,10,'deny','APACHE ARTIC','sepatu futsal',1,255000,0,'Belum di bayar','https://i.postimg.cc/nCwqjQhv/apache-merah.png'),(14,22,10,'deny','JERSEY SPECS #2','jersey',1,80000,0,'Belum di bayar','https://i.postimg.cc/9f9qtFbY/jersey2.png'),(15,26,10,'deny','KAOS KAKI SPECS','aksesoris',1,20000,0,'Belum di bayar','https://i.postimg.cc/2yQwH7xT/kaos-kaki3.jpg'),(16,3,4,'Bakri','CATALYS MISTIQUE','sepatu futsal',1,420000,0,'Belum di bayar','https://i.postimg.cc/MvGypYq6/catalys-mistique.jpg'),(17,27,5,'Sandy','BOLA MITRE','aksesoris',2,300000,0,'Belum di bayar','https://i.postimg.cc/7ZfzhNTc/bola.jpg'),(18,8,9,'indah','APACHE ARTIC','sepatu futsal',1,255000,0,'Belum di bayar','https://i.postimg.cc/4xpt9gZ9/apache.jpg'),(19,23,13,'rizal','JERSEY SPECS #3','jersey',1,80000,0,'Belum di bayar','https://i.postimg.cc/L8w11Zts/jersey3.png'),(20,7,13,'rizal','CATALYS MISTIQUE','sepatu futsal',2,840000,0,'Belum di bayar','https://i.postimg.cc/Y2mdL2f8/catalys-mistique2.jpg'),(21,16,13,'rizal','ACC INFINITY','sepatu futsal',2,840000,0,'Belum di bayar','https://i.postimg.cc/3J3C8p15/acc-infinity.jpg'),(22,29,13,'rizal','Tas Serut Futsal','Aksesoris',1,50000,0,'Belum di bayar','https://i.postimg.cc/g07NrJJy/tas-serut-umbro.jpg');
/*!40000 ALTER TABLE `Cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Customer` (
  `cust_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(50) NOT NULL,
  `role` varchar(25) NOT NULL,
  PRIMARY KEY (`cust_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (4,'Bakri','bakriboy','08215568943','muhbakri@gmail.com','customer'),(5,'Sandy','sandytower','082155667123','sandykeceng@@gmail.com','customer'),(9,'indah','indahbet','08751111426','indahayu@gmail.com','customer'),(10,'deny','denytong','08343861123','den_deny@gmail.com','customer'),(12,'rani','rani123','08122231456','rani@gmail.com','customer'),(13,'rizal','rizal1','0897654123','rizal@gmail.com','customer'),(14,'indra','indra1','08743312256','indra@gmail.com','customer'),(16,'anton','anton1','0821114342','anton@gmail.com','customer'),(18,'tias','tias','0812234888','tias@gmail.com','customer');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pelapak`
--

DROP TABLE IF EXISTS `Pelapak`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Pelapak` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(50) NOT NULL,
  `role` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pelapak`
--

LOCK TABLES `Pelapak` WRITE;
/*!40000 ALTER TABLE `Pelapak` DISABLE KEYS */;
INSERT INTO `Pelapak` VALUES (1,'rizky dwi','adminnew','0895411114371','rizky@gmail.com','pelapak'),(2,'rizky dh','admin','rizky@gmial.com','083347213554','pelapak');
/*!40000 ALTER TABLE `Pelapak` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Produk`
--

DROP TABLE IF EXISTS `Produk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Produk` (
  `produk_id` int(11) NOT NULL AUTO_INCREMENT,
  `nama_produk` varchar(100) NOT NULL,
  `kategori` varchar(50) NOT NULL,
  `merk` varchar(50) NOT NULL,
  `stok` int(11) NOT NULL,
  `harga_distri` float NOT NULL,
  `harga_bandrol` float NOT NULL,
  `warna` varchar(100) NOT NULL,
  `ukuran` int(11) NOT NULL,
  `gambar` varchar(100) NOT NULL,
  `deskripsi` text,
  PRIMARY KEY (`produk_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Produk`
--

LOCK TABLES `Produk` WRITE;
/*!40000 ALTER TABLE `Produk` DISABLE KEYS */;
INSERT INTO `Produk` VALUES (21,'JERSEY SPECS #1','jersey','Specs',50,125000,80000,'Putih Merah',49,'https://i.postimg.cc/G2J8V7ZB/jersey1.png','Jersey futsal merk Specs terbuat dari bahan yang ringan, nyaman di tubuh dan tidak mudah rusak. Ukuran jersey - M -.'),(22,'JERSEY SPECS #2','jersey','Specs',49,125000,80000,'Putih Biru',50,'https://i.postimg.cc/9f9qtFbY/jersey2.png','Jersey futsal merk Specs terbuat dari bahan yang ringan, nyaman di tubuh dan tidak mudah rusak. Ukuran jersey - L -.'),(23,'JERSEY SPECS #3','jersey','Specs',49,125000,80000,'Merah Hitam',50,'https://i.postimg.cc/L8w11Zts/jersey3.png','Jersey futsal merk Specs terbuat dari bahan yang ringan, nyaman di tubuh dan tidak mudah rusak. Ukuran jersey - L -.'),(24,'KAOS KAKI SPECS','aksesoris','Specs',20,45000,25000,'Hitam',43,'https://i.postimg.cc/j2f0bYLs/kaos-kaki1.png','Kaos kaki panjang merk Specs terbuat dari bahan yang halus, kuat dan nyaman digunakan.'),(25,'KAOS KAKI SPECS','aksesoris','Specs',20,45000,25000,'Hitam',43,'https://i.postimg.cc/3Nm6qjcN/kaos-kaki2.png','Kaos kaki panjang merk Specs terbuat dari bahan yang halus, kuat dan nyaman digunakan.'),(26,'KAOS KAKI SPECS','aksesoris','Specs',19,35000,20000,'Hit15',33,'https://i.postimg.cc/2yQwH7xT/kaos-kaki3.jpg','Kaos kaki panjang merk Specs terbuat dari bahan yang halus, kuat dan nyaman digunakan.'),(27,'bola','Aksesoris','Mitre',3,300000,200000,'Orange',4,'https://i.postimg.cc/j2f0bYLs/kaos-kaki1.png','Bola sepak untuk futsal, merk Mitre.'),(28,'Kaos kaki specs','Aksesoris','specs',50,50000,30000,'hitam',5,'https://i.postimg.cc/j2f0bYLs/kaos-kaki1.png','Kaos kaki panjang merk Specs terbuat dari bahan yang halus, kuat dan nyaman digunakan.');
/*!40000 ALTER TABLE `Produk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transaksi`
--

DROP TABLE IF EXISTS `Transaksi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Transaksi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cust_id` int(11) NOT NULL,
  `nama_cust` varchar(255) NOT NULL,
  `total_bayar` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transaksi`
--

LOCK TABLES `Transaksi` WRITE;
/*!40000 ALTER TABLE `Transaksi` DISABLE KEYS */;
/*!40000 ALTER TABLE `Transaksi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transaksis`
--

DROP TABLE IF EXISTS `Transaksis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Transaksis` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cust_id` int(11) NOT NULL,
  `nama_custom` varchar(255) NOT NULL,
  `total_bayar` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transaksis`
--

LOCK TABLES `Transaksis` WRITE;
/*!40000 ALTER TABLE `Transaksis` DISABLE KEYS */;
INSERT INTO `Transaksis` VALUES (1,4,'Bakri',255000),(2,4,'Bakri',255000),(3,4,'Bakri',255000),(4,4,'Bakri',605000);
/*!40000 ALTER TABLE `Transaksis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-27 18:22:27
