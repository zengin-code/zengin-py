# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import  # NOQA

import six
import json
import os

from zengin_code.bank import Bank
from zengin_code.branch import Branch

__version__ = '1.1.0'


def _load(*path):
    ret = None
    here = os.path.dirname(__file__)
    data_dir = os.path.join(here, 'source-data', 'data')
    with open(os.path.join(data_dir, *path), 'rb') as fp:
        ret = fp.read()
    ret = six.text_type(ret, 'utf-8')
    return ret


def _load_json(*path):
    ret = _load(*path)
    return json.loads(ret) if ret else None


def load():
    banks = _load_json('banks.json')
    for bank_code, bank_dict in sorted(banks.items(), key=lambda x: x[0]):
        bank = Bank(**bank_dict)

        branches = _load_json('branches', '{0}.json'.format(bank.code))
        branches = sorted(branches.items(), key=lambda x: x[0])
        for branch_code, branch_dict in branches:
            bank.branches[branch_code] = Branch(bank, **branch_dict)


# update version
__version__ = '{0}.{1}'.format(__version__, _load('updated_at').strip())
# preload
load()
