# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 14:16
# @Author  : lightsmile
# @FileName: info_test.py
# @Software: PyCharm

data_path = r'D:\Data\NLP\corpus\baike_info_1_to_10000\result_100.json'
from lightlabel.web.engine import Engine
from lightlabel.projects.text_classification import TextClassification

# text_cls = TextClassification('baike_info_demo', 'des_demo')
# text_cls.from_json(data_path)
# engine = Engine()
# engine.add_plan(text_cls)
# engine.run()

print(TextClassification.get_projects())
from lightlabel.plan import Plan
print(Plan.__subclasses__())
for sub_cls in Plan.__subclasses__():
    print(sub_cls.__name__)
Plan.__subclasses__()[0]('fuck', 'shit')

