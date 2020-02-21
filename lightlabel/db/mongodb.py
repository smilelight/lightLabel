# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 16:27
# @Author  : lightsmile
# @FileName: mongodb.py
# @Software: PyCharm
import json

import pymongo
from bson import json_util
from lightutils import logger

from .base import DataBase

DB_NAME = 'light_label_corpus'
PRO_CLS_NAME = 'projects'


def input_format(data):
    # 将可序列化的不含ObjectId对象的数据转换为含ObjectId对象的数据，用于操纵MongoDB
    return json_util.loads(json_util.dumps(data))


def output_format(data):
    # 将含ObjectId对象的不能序列化的数据转换成可序列化的，用于json传输
    return json.loads(json_util.dumps(data))


class MongoDB(DataBase):
    def __init__(self, database, cls, host='localhost', port=27017):
        super().__init__()
        self.database_name = database
        self.cls_name = cls
        self.client = pymongo.MongoClient(host=host, port=port)
        self.database = self.client[database]
        self.cls = self.database[cls]

    def clear(self):
        result = self.cls.delete_many({})
        logger.info("has successfully clear the {} collection of {} database".format(self.cls_name, self.database_name))
        return result

    def insert(self, data):
        if self.cls.update_one(input_format(data), {'$set': input_format(data)}, upsert=True):
            return True
        return False

    def update(self, data, new_data):
        if self.cls.update_many(input_format(data), {'$set': input_format(new_data)}):
            return True
        return False

    def delete(self, data):
        if self.cls.delete_many(input_format(data)):
            return True
        return False

    def query(self, data):
        return output_format(self.cls.find(input_format(data)))

    def get_all(self):
        return output_format(self.cls.find({}))

    def push(self, data, new_data):
        if self.cls.update_many(input_format(data), {'$push': input_format(new_data)}):
            return True
        return False

    def add_to_set(self, data, new_data):
        if self.cls.update_many(input_format(data), {'$addToSet': input_format(new_data)}):
            return True
        return False


project_db = MongoDB(DB_NAME, PRO_CLS_NAME)
