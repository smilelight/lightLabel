# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 11:50
# @Author  : lightsmile
# @FileName: engine.py
# @Software: PyCharm

from flask import Flask
from flask import send_file
import flask_restful as restful
from flask_cors import CORS
from lightutils import get_free_tcp_port, logger

from ..plan import Plan


class Engine:
    def __init__(self, plans=None):
        app = Flask(__name__)
        api = restful.Api(app)
        CORS(app)

        @app.route("/")
        @app.route("/index")
        def index():
            # return send_file('/root/data/tmp/index.html')
            return send_file(r'C:\Users\Alienware\Desktop\index.html')

        @app.route("/favicon.ico", methods=['GET'])
        def get_icon():
            # return send_file('/root/data/www/hexo/favicon.ico')
            return send_file(r'D:\Resources\Images\favicon.ico')
        self._app = app
        self._api = api
        if plans:
            for plan_item in plans:
                self.add_plan(plan_item)
        self.plan_set = set()

    def add_plan(self, plan):
        assert isinstance(plan, Plan)
        if plan.title not in self.plan_set:
            self._api.add_resource(plan.items, '/' + plan.title + '/items')
            self._api.add_resource(plan.data, '/' + plan.title + '/data')
            self.plan_set.add(plan.title)

    def run(self, host='localhost', port=None):
        # if not port:
        #     port = get_free_tcp_port()
        self._api.add_resource(Plan.project_res(), '/project_lists')
        for plan_item in Plan.get_projects():
            class_name = plan_item['task_type']
            if plan_item['label_status'] and plan_item['title'] not in self.plan_set:
                sub_class = [x for x in Plan.__subclasses__() if x.__name__ == class_name][0]
                plan_obj = sub_class(plan_item['title'], plan_item['description'])
                self.add_plan(plan_obj)
        print(self.plan_set)

        self._app.run(host=host, port=port)
