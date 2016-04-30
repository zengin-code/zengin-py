# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import  # NOQA

from collections import OrderedDict

import six


class BankMeta(type):

    banks = OrderedDict()

    def __setitem__(cls, code, bank):
        cls.banks[code] = bank

    def __getitem__(cls, code):
        return cls.banks[code]

    @property
    def all(cls):
        return cls.banks


class Bank(six.with_metaclass(BankMeta)):

    def __init__(self, code, name, kana, hira, roma):
        self.code = code
        self.name = name
        self.kana = kana
        self.hira = hira
        self.roma = roma
        self.branches = OrderedDict()
        self.__class__[code] = self
