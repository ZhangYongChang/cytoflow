DROP DATABASE IF EXISTS `cytoflow`;
CREATE DATABASE `cytoflow`;
use `cytoflow`;

DROP TABLE IF EXISTS `patientinfo`;
CREATE TABLE `patientinfo` (
  `patientid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `sex` varchar(8) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`patientid`)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `specimen`;
CREATE TABLE `specimen` (
  `specimenid` int(11) NOT NULL AUTO_INCREMENT,
  `patientid` int(11) NOT NULL,
  `sepcimentno` varchar(20) DEFAULT NULL,
  `hospital` varchar(20) DEFAULT NULL,
  `department` varchar(20) DEFAULT NULL,
  `bedno` varchar(20) DEFAULT NULL,
  `doctor` varchar(20) DEFAULT NULL,
  `specimentype` varchar(20) DEFAULT NULL,
  `caseno` varchar(20) DEFAULT NULL,
  `collecttime` datetime DEFAULT NULL,
  `recvtime` datetime DEFAULT NULL,
  `specimendir` varchar(256) DEFAULT NULL,
  PRIMARY KEY(`specimenid`)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `specimentubor`;
CREATE TABLE `specimentubor` (
  `tuborid` int(11) NOT NULL AUTO_INCREMENT,
  `specimenid` int(11) NOT NULL,
  `filename` varchar(100) DEFAULT NULL,
  PRIMARY KEY(`tuborid`)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `specimengate`;
CREATE TABLE `specimengate` (
  `gateid` int(11) NOT NULL,
  `tuborid` int(11) DEFAULT NULL,
  `gate` varchar(256) DEFAULT NULL,
  `xaxis` varchar(20) DEFAULT NULL,
  `yaxis` varchar(20) DEFAULT NULL,  
  PRIMARY KEY(`gateid`)
 ) ENGINE=InnoDB;

DROP TABLE IF EXISTS `specimentreport`;
CREATE TABLE `specimentreport` (
  `reportid` int(11) NOT NULL,
  `specimenid` int(11) NOT NULL,
  `reportpath` varchar(256) DEFAULT NULL,
  `result` varchar(256) DEFAULT NULL,
  PRIMARY KEY(`reportid`)
 ) ENGINE=InnoDB;