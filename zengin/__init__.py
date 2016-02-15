# -*- coding:utf-8 -*-

import os
from .zengin_code import ZenginCode
from .zengin_code_list import ZenginCodeList

json_dir = os.path.join(os.path.dirname(__file__), './source-data/data/banks.json')
json_path = os.path.abspath(json_dir)

ZenginCodeList.initialize(json_path)
