# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 21:35
# @Author  : lightsmile
# @FileName: db_script.py
# @Software: PyCharm
import pymongo
import tqdm
from bson.objectid import ObjectId
from lightutils import read_json_line
from bson import json_util

client = pymongo.MongoClient('mongodb://localhost:27017')

label_db = client['baidu_baike']
text_cls_demo = label_db["info"]

# insert data to mongodb
# for item in tqdm.tqdm(read_json_line(r'D:\Data\NLP\corpus\baike_info_1_to_10000\result.json')):
#     if item['type'] not in ['none', 'ambiguous']:
#         text_cls_demo.insert_one(item)

# query data from mongodb
# query_result = text_cls_demo.find().limit(10)
# for item in query_result:
#     print(item)

print(list(text_cls_demo.find({'_id': ObjectId('5e48f8eb098cd79cc6c11981')})))
print(json_util.loads(json_util.dumps(text_cls_demo.find_one({'info.word': '电子竞技'}))))
