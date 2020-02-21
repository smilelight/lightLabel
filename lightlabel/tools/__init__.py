# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 16:42
# @Author  : lightsmile
# @FileName: __init__.py.py
# @Software: PyCharm

import json


def check_json(obj):
    try:
        json.dumps(obj, ensure_ascii=False)
        return True
    except Exception as e:
        return False
