#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/29 9:37
# @Author  : xielinhua
# @Site    : 
# @File    : 04_重新更新删除后的新的原始数据.py
# @Software: PyCharm
import pandas as pd
import os

# 获取指定目录下的所有与评论相关的文件
path = './yelp_review_sentiment/' # 数据读取的文件夹的路径
save_path = './yelp_review/'  # 数据文件保存的路径
listdir = os.listdir(path)

for fileName in listdir:
    print('正在处理：' + fileName + '......')
    df = pd.read_csv(path + fileName)
    # 删除情感所在的那一列，并将原数据重新进行保存
    df = df.drop(labels='sentiment', axis=1)
    df.to_csv(save_path + fileName, index=None, mode='a')   # 保存文件