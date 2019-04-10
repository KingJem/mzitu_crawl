#!/usr/bin/env python 
# encoding: utf-8    
"""
@version: v1.0
@author: King
@contact: qqqqivy@gmail.com
@file: start.py
@time: 2019/4/10 9:16
"""

from scrapy import cmdline

# cmdline.execute("scrapy crawl fangjia -o info.csv -t csv".split())
cmdline.execute('scrapy crawl fangjia'.split())

#  把这个项目的数据放到mysql数据库中，
# 搭建一个动态代理池，抓取免费代理，无效从池中移除
# 对抓取的数据进行数据可视化，利用模块
# 对这个项目抓取增量式爬虫
# 进行分布式爬虫编写
# 上传到服务器中
# 利用爬虫可视化进行爬虫数据管理
