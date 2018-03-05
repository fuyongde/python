/*
SQLyog Ultimate v12.4.3 (64 bit)
MySQL - 5.7.21 : Database - quickstart
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`quickstart` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `quickstart`;

/*Table structure for table `website` */

DROP TABLE IF EXISTS `website`;

CREATE TABLE `website` (
  `id` int(11) NOT NULL COMMENT 'id',
  `name` varchar(16) DEFAULT NULL COMMENT '名称',
  `url` varchar(192) DEFAULT NULL COMMENT '网址',
  `alexa` int(11) DEFAULT NULL COMMENT '点击量',
  `country` varchar(8) DEFAULT NULL COMMENT '国籍',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `website` */

insert  into `website`(`id`,`name`,`url`,`alexa`,`country`) values 
(1,'Google','https://www.google.com/',1,'USA'),
(2,'淘宝','https://www.taobao.com/',13,'CN'),
(3,'菜鸟教程','https://www.runoob.com/',1689,'CN'),
(4,'微博','http://www.weibo.com',20,'CN'),
(5,'Facebook','https://www.facebook.com/',3,'USA');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
