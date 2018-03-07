# encoding: utf-8
'''
@author: feizi
@file: LotterySpider.py
@time: 2018/3/5 20:33
@Software: PyCharm
@desc:
'''
from scrapy import Request
from scrapy.spiders import Spider

from lottery_spider.items import LotteryBasicInfoItem
from lottery_spider.items import LotteryDetailItem


class LotterySpider(Spider):
    name = "lottery_spider"

    def start_requests(self):
        url = "http://www.17500.cn/ssq/awardlist.php"
        yield Request(url)

    def parse(self, response):
        # 定位内容
        lottery_conent = response.xpath('.//div[@id="sortlist"]')
        # print lottery_conent.extract_first()
        if lottery_conent is None:
            return

        # 定位table列表
        lottery_table = lottery_conent.xpath('.//table[@class="sortable"]')
        if lottery_table is None:
            return

        # 定位tr列表
        lottery_list = lottery_table.xpath('.//tbody/tr')
        # print lottery_list.extract_first()
        if lottery_list is None:
            return

        # 循环迭代table列表
        for lottery in lottery_list:
            # 期号
            issue = lottery.xpath('.//td[1]/text()').extract_first()
            issue = ('' if issue is None else issue.encode('utf-8'))
            # print "期号：", issue

            # 开奖日期
            lottery_date = lottery.xpath('.//td[2]/text()').extract_first()
            lottery_date = ('' if lottery_date is None else lottery_date.encode('utf-8'))
            # print "开奖日期：", lottery_date

            # 星期几
            week = lottery.xpath('.//td[3]/text()').extract_first()
            week = handleWeek(week)
            # print "星期几：", handleWeek(week)

            # 开奖号码
            lottery_number = lottery.xpath('.//td[4]/text()').extract_first()
            if lottery_number is None:
                return

            lottery_number_arr = lottery_number.split('+')
            if not lottery_number_arr:
                return

            # 开奖号码（红球）
            lottery_number_red = lottery_number_arr[0]
            lottery_number_red = ('' if lottery_number_red is None else lottery_number_red.encode('utf-8'))
            # print "开奖号码（红球）：", lottery_number_red

            # 开奖号码（绿球）
            lottery_number_blue = lottery_number_arr[1]
            lottery_number_blue = ('' if lottery_number_blue is None else lottery_number_blue.encode('utf-8'))
            # print "开奖号码（蓝球）：", lottery_number_blue

            # 本期投注
            current_invest_amount = lottery.xpath('.//td[5]/text()').extract_first()
            current_invest_amount = (0 if current_invest_amount is None else current_invest_amount.encode('utf-8'))
            # print "本期投注：", current_invest_amount

            # 返奖比
            return_prize_ratio = lottery.xpath('.//td[6]/text()').extract_first()
            if return_prize_ratio is None:
                # 取标红显示
                return_prize_ratio = lottery.xpath('.//td[6]/span[@class="r"]/text()').extract_first()
                # print "返奖比：", return_prize_ratio
                return_prize_ratio = ('' if return_prize_ratio is None else return_prize_ratio.encode('utf-8'))

            # 奖池金额
            jackpot_amount = lottery.xpath('.//td[7]/text()').extract_first()
            jackpot_amount = (0 if jackpot_amount is None else jackpot_amount.encode('utf-8'))
            # print "奖池金额：", jackpot_amount

            # 彩票基本信息
            lotteryBasicInfoItem = LotteryBasicInfoItem()
            lotteryBasicInfoItem['issue'] = issue
            lotteryBasicInfoItem['lottery_date'] = lottery_date
            lotteryBasicInfoItem['week'] = week
            lotteryBasicInfoItem['lottery_number_red'] = lottery_number_red
            lotteryBasicInfoItem['lottery_number_blue'] = lottery_number_blue
            lotteryBasicInfoItem['current_invest_amount'] = current_invest_amount
            lotteryBasicInfoItem['return_prize_ratio'] = return_prize_ratio
            lotteryBasicInfoItem['jackpot_amount'] = jackpot_amount

            print lotteryBasicInfoItem
            yield lotteryBasicInfoItem


        # 循环迭代table列表
        for lottery in lottery_list:
            # 期号
            issue = lottery.xpath('.//td[1]/text()').extract_first()
            issue = ('' if issue is None else issue.encode('utf-8'))
            # print "期号：", issue

            # 一等奖注数
            first_prize_count = lottery.xpath('.//td[8]/text()').extract_first()
            first_prize_count = (0 if first_prize_count is None else first_prize_count.encode('utf-8'))
            # print "一等奖注数：", first_prize_count

            # 一等奖奖金
            first_prize_amount = lottery.xpath('.//td[9]/text()').extract_first()
            first_prize_amount = (0 if first_prize_amount is None else first_prize_amount.encode('utf-8'))
            # print "一等奖奖金：", first_prize_amount

            # 二等奖注数
            second_prize_count = lottery.xpath('.//td[10]/text()').extract_first()
            second_prize_count = (0 if second_prize_count is None else second_prize_count.encode('utf-8'))
            # print "二等奖注数：", second_prize_count

            # 二等奖奖金
            second_prize_amount = lottery.xpath('.//td[11]/text()').extract_first()
            second_prize_amount = (0 if second_prize_amount is None else second_prize_amount.encode('utf-8'))
            # print "二等奖奖金：", second_prize_amount

            # 三等奖注数
            third_prize_count = lottery.xpath('.//td[12]/text()').extract_first()
            third_prize_count = (0 if third_prize_count is None else third_prize_count.encode('utf-8'))
            # print "三等奖注数：", third_prize_count

            # 三等奖奖金
            third_prize_amount = lottery.xpath('.//td[13]/text()').extract_first()
            third_prize_amount = (0 if third_prize_amount is None else third_prize_amount.encode('utf-8'))
            # print "三等奖奖金：", third_prize_amount

            # 四等奖注数
            fourth_prize_count = lottery.xpath('.//td[14]/text()').extract_first()
            fourth_prize_count = (0 if fourth_prize_count is None else fourth_prize_count.encode('utf-8'))
            # print "四等奖注数：", fourth_prize_count

            # 四等奖奖金
            fourth_prize_amount = lottery.xpath('.//td[15]/text()').extract_first()
            fourth_prize_amount = (0 if fourth_prize_amount is None else fourth_prize_amount.encode('utf-8'))
            # print "四等奖奖金：", fourth_prize_amount

            # 五等奖注数
            fifth_prize_count = lottery.xpath('.//td[16]/text()').extract_first()
            fifth_prize_count = (0 if fifth_prize_count is None else fifth_prize_count.encode('utf-8'))
            # print "五等奖注数：", fifth_prize_count

            # 五等奖奖金
            fifth_prize_amount = lottery.xpath('.//td[17]/text()').extract_first()
            fifth_prize_amount = (0 if fifth_prize_amount is None else fifth_prize_amount.encode('utf-8'))
            # print "五等奖奖金：", fifth_prize_amount

            # 六等奖注数
            sixth_prize_count = lottery.xpath('.//td[18]/text()').extract_first()
            sixth_prize_count = (0 if sixth_prize_count is None else sixth_prize_count.encode('utf-8'))
            # print "六等奖注数：", sixth_prize_count

            # 六等奖奖金
            sixth_prize_amount = lottery.xpath('.//td[19]/text()').extract_first()
            sixth_prize_amount = (0 if sixth_prize_amount is None else sixth_prize_amount.encode('utf-8'))
            # print "六等奖奖金：", sixth_prize_amount

            # 彩票详情信息
            lotteryDetailItem = LotteryDetailItem()
            lotteryDetailItem['issue'] = issue
            lotteryDetailItem['first_prize_count'] = first_prize_count
            lotteryDetailItem['first_prize_amount'] = first_prize_amount
            lotteryDetailItem['second_prize_count'] = second_prize_count
            lotteryDetailItem['second_prize_amount'] = second_prize_amount
            lotteryDetailItem['third_prize_count'] = third_prize_count
            lotteryDetailItem['third_prize_amount'] = third_prize_amount
            lotteryDetailItem['fourth_prize_count'] = fourth_prize_count
            lotteryDetailItem['fourth_prize_amount'] = fourth_prize_amount
            lotteryDetailItem['fifth_prize_count'] = fifth_prize_count
            lotteryDetailItem['fifth_prize_amount'] = fifth_prize_amount
            lotteryDetailItem['sixth_prize_count'] = sixth_prize_count
            lotteryDetailItem['sixth_prize_amount'] = sixth_prize_amount

            print lotteryDetailItem
            yield lotteryDetailItem

        page_url_list = lottery_table.xpath('following-sibling::*')
        if not page_url_list:
            return

        if page_url_list and len(page_url_list) < 4:
            next_url = page_url_list[0].xpath('@href').extract_first()
        else:
            next_url = page_url_list[2].xpath('@href').extract_first()

        # 下一页url
        if next_url:
            next_url = 'http://www.17500.cn/ssq/awardlist.php' + next_url
            print "====>", next_url
            yield Request(next_url)


# 处理日期显示
def handleWeek(str):
    if str is None:
        return ''
    elif str == '日'.decode('utf8'):
        return "星期天"
    elif str == '一'.decode('utf8'):
        return "星期一"
    elif str == '二'.decode('utf8'):
        return "星期二"
    elif str == '三'.decode('utf8'):
        return "星期三"
    elif str == '四'.decode('utf8'):
        return "星期四"
    elif str == '五'.decode('utf8'):
        return "星期五"
    elif str == '六'.decode('utf8'):
        return "星期六"
