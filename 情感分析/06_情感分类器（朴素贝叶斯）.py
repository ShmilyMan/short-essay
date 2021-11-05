#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/10/29 15:18
# @Author  : xielinhua
# @Site    : 
# @File    : 06_情感分类器.py
# @Software: PyCharm
from textblob.classifiers import NaiveBayesClassifier
import pandas as pd
from textblob import TextBlob
from pandas.core.frame import DataFrame
from numpy import *
import os
import random

'''
加载数据并同时进行训练，之后对训练的结果进行保存
'''

train_path = './train/'  # 训练数据的文件存储路径
test_path = './test/'  # 测试数据的文件存储路径

'''
加载数据
path:所加载的数据的文件夹的路径
return:加载数据的（dataforme）列表
'''
def loadData(path):
    dataList = []  # 加载数据所存放的列表
    list_dir = os.listdir(path)
    for fileName in list_dir:
        df = pd.read_csv(path + fileName)
        dataList.append(df)
    return dataList;

# 1.加载训练数据
trainDataList = loadData(train_path)
print('训练集数据加载完毕......')

# 2.加载测试集数据
testDataList = loadData(test_path)
print('测试集数据加载完毕......')

# 3.进行训练
# 3.1 生成训练集
train = []  # 训练集
for index,row in trainDataList[2].iterrows():
    train.append((row['text'], row['sentiment']))
# 3.2 进行训练
print('开始训练---------------->>>>>>>>')
cl = NaiveBayesClassifier(train)
# 3.3 计算准确率
accuracy = []
for item in range(40):
    test = []  # 测试集
    for index, row in testDataList[item].iterrows():
        test.append((row['text'], row['sentiment']))
    accuracy.append(cl.accuracy(test))
    print('准确率为：' + str(cl.accuracy(test)))
print('---------------------')
print(mean(accuracy))