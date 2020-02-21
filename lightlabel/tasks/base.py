# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 22:25
# @Author  : lightsmile
# @FileName: new_base.py
# @Software: PyCharm

import csv
from abc import ABCMeta, abstractmethod

from tqdm import tqdm
from lightutils import read_json_line, logger

from ..db.base import DataBase


class BaseTask(metaclass=ABCMeta):
    def __init__(self, title: str, description: str, db: DataBase):
        self.title = title
        self.description = description
        self.db = db

    def init_from_csv(self, csv_path, headers=None):
        self.from_csv(csv_path, headers, clear=True)

    def update_from_csv(self, csv_path, headers=None):
        self.from_csv(csv_path, headers, clear=False)
        
    def from_csv(self, csv_path, headers=None, clear=False):
        if clear:
            self.clear()
        with open(csv_path, encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            if not headers:
                headers = next(csv_reader)
            for line in tqdm(csv_reader):
                assert len(headers) == len(line)
                self.db.insert({
                    'raw_data': {key: value for key, value in zip(headers, line)},
                    'labeled_status': False,
                    'updated_time': None,
                    'labeled_user': None,
                    'labeled_data': None,
                    'check_status': False
                })
        logger.info("successfully loaded from {}".format(csv_path))

    def init_from_json(self, json_path):
        self.from_json(json_path, clear=True)

    def update_from_json(self, json_path):
        self.from_json(json_path, clear=False)

    def from_json(self, json_path, clear=False):
        if clear:
            self.clear()
        for line in tqdm(read_json_line(json_path)):
            self.db.insert({
                'raw_data': line,
                'labeled_status': False,
                'updated_time': None,
                'labeled_user': None,
                'labeled_data': None,
                'check_status': False
            })
        logger.info("successfully loaded from {}".format(json_path))
            
    def get_all_data(self):
        return self.db.get_all()
    
    def get_all_labeled_data(self):
        return self.db.query({'labeled_status': True})
    
    def get_all_unlabeled_data(self):
        return self.db.query({'labeled_status': False})
    
    def insert_item(self, data):
        return self.db.insert(data)
    
    def update_item(self, data, new_data):
        return self.db.update(data, new_data)
    
    def delete_item(self, data):
        return self.db.delete(data)
    
    def query_item(self, data):
        return self.db.query(data)
    
    def clear(self):
        return self.db.clear()
