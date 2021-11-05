#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/10/28 19:46
# @Author  : xielinhua
# @Site    : 
# @File    : 03_统计数据.py
# @Software: PyCharm
import pandas as pd
import os

totalPath = './yelp_review_sentiment/'
negPath = './yelp_review_sentiment_neg/'
posPath = './yelp_review_sentiment_pos/'
# 1、统计评论的总数
# listdir = os.listdir(totalPath)
# totalCount = 0
# for fileName in listdir:
#     print('正在处理：' + fileName + '......')
#     total_df = pd.read_csv(totalPath + fileName)
#     print(total_df)
#     totalCount += total_df.shape[0]
# print('评论的总数为：' + str(totalCount))

# 2.统计消极评论的个数
listdir = os.listdir(negPath)
negCount = 0
for fileName in listdir:
    print('正在处理：' + fileName + '......')
    neg_df = pd.read_csv(negPath + fileName)
    # print(neg_df)
    negCount += neg_df.shape[0]
print('消极评论的总数为：' + str(negCount))

# 3.统计积极评论的个数
listdir = os.listdir(posPath)
posCount = 0
for fileName in listdir:
    print('正在处理：' + fileName + '......')
    pos_df = pd.read_csv(posPath + fileName)
    posCount += pos_df.shape[0]
print('积极评论的总数为：' + str(posCount))