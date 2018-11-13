# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import  # NOQA

from collections import OrderedDict

import six


class BankMeta(type):

    banks = OrderedDict()
    named_banks = {}

    def __setitem__(cls, code, bank):
        cls.banks[code] = bank
        cls.named_banks[bank.name] = bank

    def __getitem__(cls, code):
        return cls.banks[code]

    @property
    def all(cls):
        return cls.banks

    def by_name(cls, name):
        return cls.named_banks.get(name)


class Bank(six.with_metaclass(BankMeta)):

    def __init__(self, code, name, kana, hira, roma):
        self.code = code
        self.name = name
        self.kana = kana
        self.hira = hira
        self.roma = roma
        self.branches = OrderedDict()
        self.named_branches = {}
        self.__class__[code] = self

    def branch_by_name(self, name):
        return self.named_branches.get(name)

    def add_branch(self, branch):
        self.branches[branch.code] = branch
        self.named_branches[branch.name] = branch
