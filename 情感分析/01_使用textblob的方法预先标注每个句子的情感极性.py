#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/10/28 10:39
# @Author  : xielinhua
# @Site    : 
# @File    : 使用textblob的方法预先标注每个句子的情感极性.py
# @Software: PyCharm
'''
    注意：3,9文件均少了一条数据
'''
import pandas as pd
import os
from textblob import TextBlob
from pandas.core.frame import DataFrame

# 获取指定目录下的所有与评论相关的文件
path = './aaa/' # 数据读取的文件夹的路径
save_path = './yelp_review_sentiment/'
listdir = os.listdir(path)

for fileName in listdir:
    print('正在处理：' + fileName + '......')
    df = pd.read_csv(path + fileName)
    print(df)
    reviewId = []   # 评论编号
    sentimentList = []  # 存放情感极性的列表
    err_review_info = []    # 存放不存在评论信息的空评论
    # 遍历每个 dataform 为每个评论打上情感极性的标签
    for index,row in df.iterrows():
        text = row['text']
        # print('text' + str(index) + '：' + text)
        # print('--------------------')
        # 分析每个句子的情感极性 [-1, 1] 之间，越接近 -1 越代表消极的情绪，越接近 1 越代表积极的情绪
        # print(row['review_id'])
        try:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity  # 情绪的极性
            if polarity >= 0:
                sentiment = 'pos'  # 代表情感极性的情感
            else:
                sentiment = 'neg'
            reviewId.append(row['review_id'])
            sentimentList.append(sentiment)
        except:
            # 如果不存在评价，则删除改行，并对原始的 dataforme 重新赋值
            err_review_info.append(index)
    # 将 sentimentList 转化为 dataforme 以便于进行两个 dataform 的连接
    sentimentDist = {
        "review_id": reviewId,
        "sentiment": sentimentList
    }  # 将列表 sentimentList 转换成字典
    sentimentDataForm = DataFrame(sentimentDist)  # 将字典转换成为数据框
    # 将空评论的行删除
    for item in err_review_info:
        df.drop(df.index[item], inplace=True)
    print(df)
    # 将两个 dataform 进行连接，组合成一个 dataform
    result = pd.merge(df,sentimentDataForm,on='review_id')
    # 将数据重新存储为新的 csv 文件
    result.to_csv(save_path + fileName, index=None, mode='a')



