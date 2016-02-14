# -*- coding:utf-8 -*-

class ZenginCode:
    def __init__(self, **kwargs):
        self.code = kwargs.get('code')
        self.name = kwargs.get('name')
        self.kana = kwargs.get('kana')
        self.hira = kwargs.get('hira')
        self.roma = kwargs.get('roma')
