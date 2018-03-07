# encoding: utf-8
'''
@author: feizi
@file: main.py
@time: 2018/3/5 22:35
@Software: PyCharm
@desc:
'''


from scrapy import cmdline
name = "lottery_spider"
cmd = "scrapy crawl {0}".format(name)
cmdline.execute(cmd.split())