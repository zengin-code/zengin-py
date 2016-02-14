# -*- coding:utf-8 -*-

import json
from .zengin_code import ZenginCode

class ZenginCodeList(list):
    _list = []

    @staticmethod
    def initialize(path):
        with open(path, 'r') as f:
            codes = json.load(f)

        for k in codes.keys():
            v = codes[k]
            i = dict(
                    code=v['code'],
                    name=v['name'],
                    kana=v['kana'],
                    hira=v['hira'],
                    roma=v['roma']
                )
            ZenginCodeList._list.append(ZenginCode(**i))

    @staticmethod
    def all():
        return ZenginCodeList._list

