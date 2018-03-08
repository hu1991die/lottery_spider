/*
Navicat MySQL Data Transfer

Source Server         : loclahost
Source Server Version : 50635
Source Host           : localhost:3306
Source Database       : lotterydb

Target Server Type    : MYSQL
Target Server Version : 50635
File Encoding         : 65001

Date: 2018-03-08 20:28:10
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for lottery_basic_info
-- ----------------------------
DROP TABLE IF EXISTS `lottery_basic_info`;
CREATE TABLE `lottery_basic_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `issue` varchar(10) DEFAULT NULL COMMENT '期号',
  `lottery_date` datetime DEFAULT NULL COMMENT '开奖日期',
  `week` varchar(10) DEFAULT NULL COMMENT '星期几',
  `current_invest_amount` varchar(20) DEFAULT NULL COMMENT '本期投注',
  `return_prize_ratio` varchar(10) DEFAULT NULL COMMENT '返奖比',
  `jackpot_amount` varchar(20) DEFAULT NULL COMMENT '奖池金额',
  `lottery_number_red` varchar(20) DEFAULT NULL COMMENT '开奖号码(红球)',
  `lottery_number_blue` varchar(10) DEFAULT NULL COMMENT '开奖号码(蓝球)',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_issue` (`issue`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2232 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for lottery_detail
-- ----------------------------
DROP TABLE IF EXISTS `lottery_detail`;
CREATE TABLE `lottery_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `issue` varchar(10) DEFAULT NULL COMMENT '期号',
  `first_prize_count` tinyint(3) DEFAULT NULL COMMENT '一等奖（注数）',
  `first_prize_amount` varchar(20) DEFAULT NULL COMMENT '一等奖（奖金）',
  `second_prize_count` smallint(10) DEFAULT NULL COMMENT '二等奖（注数）',
  `second_prize_amount` varchar(20) DEFAULT NULL COMMENT '二等奖（奖金）',
  `third_prize_count` smallint(10) DEFAULT NULL COMMENT '三等奖（注数）',
  `third_prize_amount` varchar(20) DEFAULT NULL COMMENT '三等奖（奖金）',
  `fourth_prize_count` int(10) DEFAULT NULL COMMENT '四等奖（注数）',
  `fourth_prize_amount` varchar(20) DEFAULT NULL COMMENT '四等奖（奖金）',
  `fifth_prize_count` int(10) DEFAULT NULL COMMENT '五等奖（注数）',
  `fifth_prize_amount` varchar(20) DEFAULT NULL COMMENT '五等奖（奖金）',
  `sixth_prize_count` int(10) DEFAULT NULL COMMENT '六等奖（注数）',
  `sixth_prize_amount` varchar(20) DEFAULT NULL COMMENT '六等奖（奖金）',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2232 DEFAULT CHARSET=utf8mb4;
