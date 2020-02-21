# -*- coding: utf-8 -*-
# @Time    : 2020/2/17 15:23
# @Author  : lightsmile
# @FileName: op_data_test.py
# @Software: PyCharm

from lightlabel.db.mongodb import MongoDB

db = MongoDB('light_label_corpus', 'ttt_demo')
result = db.update({
    'raw_data.word': '李白'
}, {'labeled_data': '诗人'})
print(result)
print(db.query({
    'raw_data.word': '李白'
}))
for item in db.get_all():
    print(item)
