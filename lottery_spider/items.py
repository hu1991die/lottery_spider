# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 彩票基本信息类
class LotteryBasicInfoItem(scrapy.Item):
    # 主键ID
    id = scrapy.Field()
    # 期号
    issue = scrapy.Field()
    # 开奖日期
    lottery_date = scrapy.Field()
    # 星期几
    week = scrapy.Field()
    # 本期投注
    current_invest_amount = scrapy.Field()
    # 返奖比
    return_prize_ratio = scrapy.Field()
    # 奖池金额
    jackpot_amount = scrapy.Field()
    # 开奖号码(红球)
    lottery_number_red = scrapy.Field()
    # 开奖号码(蓝球)
    lottery_number_blue = scrapy.Field()


# 彩票详情信息
class LotteryDetailItem(scrapy.Item):
    # 主键ID
    id = scrapy.Field()
    # 期号
    issue = scrapy.Field()
    # 一等奖（注数）
    first_prize_count = scrapy.Field()
    # 一等奖（奖金）
    first_prize_amount = scrapy.Field()
    # 二等奖（注数）
    second_prize_count = scrapy.Field()
    # 二等奖（奖金）
    second_prize_amount = scrapy.Field()
    # 三等奖（注数）
    third_prize_count = scrapy.Field()
    # 三等奖（奖金）
    third_prize_amount = scrapy.Field()
    # 四等奖（注数）
    fourth_prize_count = scrapy.Field()
    # 四等奖（奖金）
    fourth_prize_amount = scrapy.Field()
    # 五等奖（注数）
    fifth_prize_count = scrapy.Field()
    # 五等奖（奖金）
    fifth_prize_amount = scrapy.Field()
    # 六等奖（注数）
    sixth_prize_count = scrapy.Field()
    # 六等奖（奖金）
    sixth_prize_amount = scrapy.Field()
