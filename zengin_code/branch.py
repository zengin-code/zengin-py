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
