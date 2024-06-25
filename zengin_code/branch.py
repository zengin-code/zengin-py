# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import  # NOQA


class Branch(object):

    def __init__(self, bank, code, name, kana, hira, roma):
        self.bank = bank
        self.code = code
        self.name = name
        self.kana = kana
        self.hira = hira
        self.roma = roma

    def to_dict(self):
        return {
            'bank': self.bank.to_dict(without_branches=True), # no transforming itself due to infinite stack consuming
            'code': self.code,
            'name': self.name,
            'kana': self.kana,
            'hira': self.hira,
            'roma': self.roma,
        }