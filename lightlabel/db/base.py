# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 22:11
# @Author  : lightsmile
# @FileName: base.py
# @Software: PyCharm

from abc import ABCMeta, abstractmethod


class DataBase(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def __init__(cls, *args, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def clear(cls):
        pass

    @classmethod
    @abstractmethod
    def insert(cls, data):
        pass

    @classmethod
    @abstractmethod
    def update(cls, data, new_data):
        pass

    @classmethod
    @abstractmethod
    def delete(cls, data):
        pass

    @classmethod
    @abstractmethod
    def query(cls, data):
        pass

    @classmethod
    @abstractmethod
    def get_all(cls):
        pass
