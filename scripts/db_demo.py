# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 19:35
# @Author  : lightsmile
# @FileName: db_demo.py
# @Software: PyCharm
import pymongo
import random
data = [
    '李白',
    '曹操',
    '司马懿',
    '徐晃',
    '张辽'
]
labels = [
    '三国人物',
    '诗人',
    '魏国人物'
]

client = pymongo.MongoClient('mongodb://localhost:27017')

db = client['nlp_corpus']
cls = db['text_classification_demo']
for word in data:
    cls.update_one({'word': word}, {'$set': {'word': word}}, upsert=True)
cls.update_many({}, {'$set': {'status': False, 'fuck': None}})

# for word in data:
#     print(cls.find_one_and_update({'word': word}, {'$set': {'label': random.choice(labels)}}))
# cls.delete_many({})

# for key, value in cls.find_one({}).items():
#     print(key, value, type(value) == str)

