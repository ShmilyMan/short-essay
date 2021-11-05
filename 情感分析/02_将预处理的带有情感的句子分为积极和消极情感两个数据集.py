#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/10/28 17:10
# @Author  : xielinhua
# @Site    : 
# @File    : 02_将预处理的带有情感的句子分为积极和消极情感两个数据集.py
# @Software: PyCharm
import pandas as pd
import os

# 读取指定文件夹下的所有数据
path = './yelp_review_sentiment/' # 数据读取的文件夹的路径
posPath = './yelp_review_sentiment_pos/'
negPath = './yelp_review_sentiment_neg/'

listdir = os.listdir(path)
for fileName in listdir:
    posList = []  # 存取正向极性数据的列表
    negList = []  # 存取负向极性数据的列表

    print('正在处理：' + fileName + '......')
    df = pd.read_csv(path + fileName)
    # 遍历数据，并将数据中的不同情感极性分别进行存取
    for index,row in df.iterrows():
        sentiment = row['sentiment']
        if sentiment == 'pos':
            # 积极
            posListItem = []
            posListItem.append(row['review_id'])
            posListItem.append(row['user_id'])
            posListItem.append(row['business_id'])
            posListItem.append(row['stars'])
            posListItem.append(row['useful'])
            posListItem.append(row['funny'])
            posListItem.append(row['cool'])
            posListItem.append(row['text'])
            posListItem.append(row['date'])
            posListItem.append(row['sentiment'])
            posList.append(posListItem)
        else:
            # 消极
            negListItem = []
            negListItem.append(row['review_id'])
            negListItem.append(row['user_id'])
            negListItem.append(row['business_id'])
            negListItem.append(row['stars'])
            negListItem.append(row['useful'])
            negListItem.append(row['funny'])
            negListItem.append(row['cool'])
            negListItem.append(row['text'])
            negListItem.append(row['date'])
            negListItem.append(row['sentiment'])
            negList.append(negListItem)
    # 将不同极性的数据分别存取到不同的文件夹中
    save_name = ['review_id', 'user_id', 'business_id', 'stars', 'useful', 'funny', 'cool', 'text', 'date', 'sentiment']

    # print(posList)
    # print(negList)

    pd_save_pos = pd.DataFrame(columns=save_name, data=posList)
    pd_save_pos.to_csv(posPath + fileName, index=False)

    pd_saves_neg = pd.DataFrame(columns=save_name, data=negList)
    pd_saves_neg.to_csv(negPath + fileName, index=False)