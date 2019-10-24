DROP DATABASE IF EXISTS `cytoflow`;
CREATE DATABASE `cytoflow`;
use `cytoflow`;

DROP TABLE IF EXISTS `specimen`;
CREATE TABLE `specimen` (
  `specimenid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) DEFAULT NULL,
  `sex` varchar(8) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `specimenno` varchar(64) DEFAULT NULL,
  `hospital` varchar(64) DEFAULT NULL,
  `department` varchar(64) DEFAULT NULL,
  `bedno` varchar(64) DEFAULT NULL,
  `doctor` varchar(64) DEFAULT NULL,
  `specimentype` varchar(64) DEFAULT NULL,
  `caseno` varchar(64) DEFAULT NULL,
  `collecttime` date DEFAULT NULL,
  `recvtime` date DEFAULT NULL,
  `specimendir` varchar(256) DEFAULT NULL,
  PRIMARY KEY(`specimenid`)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `specimengate`;
CREATE TABLE `specimengate` (
  `specimengateid` int(11) NOT NULL AUTO_INCREMENT,
  `specimenid` int(11) NOT NULL,
  `fcsfilename` varchar(256) DEFAULT NULL,
  `gates` varchar(4096) DEFAULT NULL,
  `gatetype` int(11) NOT NULL,
  `createtime` datetime DEFAULT NULL,
  `modifytime` datetime DEFAULT NULL,
  PRIMARY KEY(`specimengateid`)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `gatetemplate`;
CREATE TABLE `gatetemplate` (
  `gatetemplateid` int(11) NOT NULL AUTO_INCREMENT,
  `templatename` varchar(256) DEFAULT NULL,
  `gates` varchar(1024) DEFAULT NULL,
  `gatetype` int(11) NOT NULL,
  `createtime` datetime DEFAULT NULL,
  `modifytime` datetime DEFAULT NULL,
  PRIMARY KEY(`gatetemplateid`)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS `specimenreport`;
CREATE TABLE `specimenreport` (
  `sepcimenreportid` int(11) NOT NULL AUTO_INCREMENT,
  `specimenid` int(11) NOT NULL,
  `specimenreportpath` varchar(1024) DEFAULT NULL,
  `createtime` datetime DEFAULT NULL,
  PRIMARY KEY(`sepcimenreportid`)
) ENGINE=InnoDB;