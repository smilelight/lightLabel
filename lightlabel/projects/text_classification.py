# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 12:31
# @Author  : lightsmile
# @FileName: text_classification.py
# @Software: PyCharm

from ..plan import Plan
from ..db.mongodb import project_db


class TextClassification(Plan):
    def __init__(self, title: str, description: str):
        super().__init__(title, description, task_type=self.__class__.__name__)

    def add_classes(self, classes):
        assert type(classes) in (list, set)
        project_db.update(self._meta_data, {'data.classes': classes})

