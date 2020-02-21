# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 12:34
# @Author  : lightsmile
# @FileName: __init__.py.py
# @Software: PyCharm

from abc import ABCMeta, abstractmethod
from ..db.mongodb import MongoDB, DB_NAME, project_db
from ..tasks.base import BaseTask


class Plan(metaclass=ABCMeta):
    def __init__(self, title: str, description: str, task_type: str):
        self._db = MongoDB(DB_NAME, title)
        self._task = BaseTask(title, description, self._db)
        self._meta_data = {
            'title': title,
            'task_type': task_type,
            'description': description,
            'label_status': True
        }
        if not project_db.query(self._meta_data):
            project_db.insert(self._meta_data)
            project_db.update(self._meta_data, {'data': {}})

    def get_project(self):
        projects = project_db.query(self._meta_data)
        assert len(projects) == 1
        project = projects[0]
        return project

    @property
    def project(self):
        return self.get_project()

    def check_data_path(self, data_path):
        if 'data_path' not in self.project:
            return False
        return data_path in self.project['data_path']

    def update_from_csv(self, csv_path, headers=None):
        if not self.check_data_path(csv_path):
            self._task.update_from_csv(csv_path, headers)
            project_db.add_to_set(self._meta_data, {'data_path': csv_path})

    def init_from_csv(self, csv_path, headers=None):
        self._task.init_from_csv(csv_path, headers)
        project_db.add_to_set(self._meta_data, {'data_path': csv_path})

    def update_from_json(self, json_path):
        if not self.check_data_path(json_path):
            self._task.update_from_json(json_path)
            project_db.add_to_set(self._meta_data, {'data_path': json_path})

    def init_from_json(self, json_path):
        self._task.init_from_json(json_path)
        project_db.add_to_set(self._meta_data, {'data_path': json_path})

    @property
    def data(self):
        import flask_restful as restful
        outer = self

        class TaskData(restful.Resource):
            def get(self):
                return outer.project['data']

        return TaskData

    @property
    def items(self):
        from flask import request
        import flask_restful as restful
        import json
        outer = self

        class TaskResource(restful.Resource):
            def get(self):
                return outer._task.get_all_data()

            def post(self):
                res_data = json.loads(bytes.decode(request.data, encoding='utf-8'))
                print(res_data)
                if outer._task.update_item(res_data['data_id'], res_data['new_data']):
                    print('fuck')
                else:
                    print('shit')
        return TaskResource

    @property
    def title(self):
        return self._meta_data['title']

    @classmethod
    def get_projects(cls):
        return project_db.get_all()

    @classmethod
    def project_res(cls):
        import flask_restful as restful

        class ProjectRes(restful.Resource):
            def get(self):
                return project_db.get_all()
        return ProjectRes
