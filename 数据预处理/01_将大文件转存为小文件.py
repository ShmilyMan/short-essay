#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2021/10/7 17:28
# @Author  : xielinhua
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import json
import pandas as pd

result = []
index = 0
count = 0
with open(r'yelp_academic_dataset_review.json', 'r', encoding='utf-8')as f:
    for ff in f:
        if index >= 500000:
            print('以及处理' + str(count * 500000) + '条啦')
            df = pd.json_normalize(result)
            df.to_csv('./yelp_review/yelp_academic_dataset_review' + str(count) + '.csv', index=None, mode='a')
            count += 1
            index = 0
            result = []
        data = json.loads(ff)
        data['text'] = data['text'].replace('\n','')
        result.append(data)
        index += 1



# df = pd.read_csv('./yelp_review/yelp_academic_dataset_review0.csv')
# for index,row in df.iterrows():
#     print(row['text'])
#     print('-------------')