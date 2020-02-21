# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 12:42
# @Author  : lightsmile
# @FileName: label_test.py
# @Software: PyCharm

from lightlabel import Engine, TextClassification

text_cls = TextClassification('ttt_demo', 'des_demo')
text_cls.add_classes(['唐朝人物', '虚拟人物', '三国人物'])
text_cls.update_from_csv(r'C:\Users\Alienware\Desktop\text_classification_demo.csv', headers=['word'])
engine = Engine()
engine.add_plan(text_cls)
engine.run()
