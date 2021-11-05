#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/10/28 9:18
# @Author  : xielinhua
# @Site    : 
# @File    : 情感分类器.py
# @Software: PyCharm
from textblob.classifiers import NaiveBayesClassifier
import pandas as pd
from textblob import TextBlob
from pandas.core.frame import DataFrame
import os
import random

pos_path = './yelp_review_sentiment_pos/' # 存放积极情绪的文件夹路径
neg_path = './yelp_review_sentiment_neg/' # 存放消极情绪的文件夹路径
save_path_train = './train2/' # 结果的保存路径 -->  train
save_path_test = 'test2/'  # 结果的保存路径 -->  test

'''
加载数据
path:数据存储的文件夹的路径
return:所有数据合并后的 dataforme
'''
def loadData(path):
    # 加载情绪数据
    list_df = []  # 存放所有的 dataforme 的列表
    list_dir = os.listdir(path)
    for fileName in list_dir:
        print('正在处理：' + fileName)
        df = pd.read_csv(path + fileName)
        list_df.append(df)
    # 将所有的 dataforme 进行合并
    dfs = pd.concat(list_df, axis=0, ignore_index=True)
    return dfs

'''
生成随机的dataforme，并返回
train: 2500
text:500
'''
def randomData(pos_dfs, neg_dfs):
    # 1.生成随机数据
    pos_random = random.sample(range(0, pos_dfs.shape[0]), 500)  # 积极情绪
    neg_random = random.sample(range(0, neg_dfs.shape[0]), 500)  # 消极情绪
    pos_random_data = pos_dfs.iloc[pos_random]  # 积极情绪的数据
    neg_random_data = neg_dfs.iloc[neg_random]  # 消极情绪的数据


    # 2.生成训练数据和测试数据 (dataforme)
    train_neg_random_data = neg_random_data[0:400]
    train_pos_random_data = pos_random_data[0:400]
    trainData = pd.concat([train_neg_random_data, train_pos_random_data], axis=0, ignore_index=True)  # 训练数据

    test_neg_random_data = neg_random_data[400:]
    test_pos_random_data = pos_random_data[400:]
    testData = pd.concat([test_neg_random_data, test_pos_random_data], axis=0, ignore_index=True)  # 测试数据
    return trainData,testData


# 1.加载积极情绪数据
# pos_dfs = loadData(pos_path)
# print('1.1 积极情绪数据加载完毕......')
# print(pos_dfs)
pos_dfs = pd.read_csv('yelp_review_sentiment_pos/yelp_academic_dataset_review0.csv')

# 2.加载消极情绪数据
# neg_dfs = loadData(neg_path)
# print('1.2 消极数据加载完毕......')
# print(neg_dfs)
neg_dfs = pd.read_csv('yelp_review_sentiment_neg/yelp_academic_dataset_review0.csv')

# 3.获取随机生成的训练集和测试集的数据 (dataforme),将结果重新存储为新的 csv 文件
# result.to_csv(save_path + fileName, index=None, mode='a')
for item in range(1):
    print('正在生成第' + str(item + 1) + '训练测试数据')
    # 3.1 获取随机生成的数据
    result = randomData(pos_dfs, neg_dfs)
    trainData = result[0]
    testData = result[1]
    # 3.2 保存文件
    trainData.to_csv(save_path_train + 'train' + str(item + 1) + '.csv', index=None, mode='a')
    testData.to_csv(save_path_test + 'test' + str(item + 1) + '.csv', index=None, mode='a')
