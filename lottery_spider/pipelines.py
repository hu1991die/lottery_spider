# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import MySQLdb

# 获取数据库连接
from scrapy.exceptions import DropItem

from lottery_spider.items import LotteryBasicInfoItem, LotteryDetailItem


def getDbConn():
    conn = MySQLdb.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='lotterydb',
        charset='utf8'
    )
    return conn

# 关闭数据库资源
def closeConn(cursor, conn):
    if cursor:
        # 关闭游标
        cursor.close()
    if conn:
        # 关闭数据库连接
        conn.close()

class LotterySpiderPipeline(object):
    def __init__(self):
        # 基础item
        self.items_basic_set = set()
        # 详情item
        self.items_detail_set = set()

    def process_item(self, item, spider):
        if item.__class__ == LotteryBasicInfoItem:
            if item['issue'] in self.items_basic_set:
                raise DropItem("Duplicate lotteryBasicInfoItem found: %s" % item)
            else:
                self.items_basic_set.add(item['issue'])
                self.insertLotteryBasicInfoItem(item)
        elif item.__class__ == LotteryDetailItem:
            if item['issue'] in self.items_detail_set:
                raise DropItem("Duplicate LotteryDetailItem found: %s" % item)
            else:
                self.items_detail_set.add(item['issue'])
                self.insertLotteryDeialItem(item)
        return item

    # 插入基础信息
    def insertLotteryBasicInfoItem(self, item):
        try:
            # 获取数据库连接
            conn = getDbConn()
            # 获取游标
            cursor = conn.cursor()
            # 插入数据库
            sql = "INSERT INTO `lottery_basic_info`(`issue`, `lottery_date`, `week`, `current_invest_amount`, " \
                  "`return_prize_ratio`, `jackpot_amount`, `lottery_number_red`, `lottery_number_blue`) " \
                  "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"

            params = (item['issue'], item['lottery_date'],
                      item['week'], item['current_invest_amount'],
                      item['return_prize_ratio'], item['jackpot_amount'],
                      item['lottery_number_red'], item['lottery_number_blue'])
            cursor.execute(sql, params)

            # 事务提交
            conn.commit()
        except Exception, e:
            # 事务回滚
            conn.rollback()
            print 'except:', e
        finally:
            # 关闭游标和数据库连接
            closeConn(cursor, conn)


    # 插入详情信息
    def insertLotteryDeialItem(self, item):
        try:
            # 获取数据库连接
            conn = getDbConn()
            # 获取游标
            cursor = conn.cursor()
            # 插入数据库
            sql = "INSERT INTO `lottery_detail`(`issue`, `first_prize_count`, `first_prize_amount`, " \
                  "`second_prize_count`, `second_prize_amount`, `third_prize_count`, `third_prize_amount`, " \
                  "`fourth_prize_count`, `fourth_prize_amount`, `fifth_prize_count`, `fifth_prize_amount`, " \
                  "`sixth_prize_count`, `sixth_prize_amount`) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            params = (item['issue'],
                      item['first_prize_count'], item['first_prize_amount'],
                      item['second_prize_count'], item['second_prize_amount'],
                      item['third_prize_count'], item['third_prize_amount'],
                      item['fourth_prize_count'], item['fourth_prize_amount'],
                      item['fifth_prize_count'], item['fifth_prize_amount'],
                      item['sixth_prize_count'], item['sixth_prize_amount'])
            cursor.execute(sql, params)

            # 事务提交
            conn.commit()
        except Exception, e:
            # 事务回滚
            conn.rollback()
            print 'except:', e
        finally:
            # 关闭游标和数据库连接
            closeConn(cursor, conn)