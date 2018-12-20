# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import


class TestBank(object):

    def _get_target_class(self, *args, **kwargs):
        from zengin_code.bank import Bank
        return Bank

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    def test_load(self):
        cls = self._get_target_class()
        assert 0 < len(cls.all)

    def test_get(self):
        cls = self._get_target_class()
        b1 = cls(9999, u'試験', u'テスト', u'てすと', 'Test')
        assert b1 is cls[9999]

    def test_bank_by_name(self):
        cls = self._get_target_class()
        b1 = cls(9999, u'試験', u'テスト', u'てすと', 'Test')
        assert b1.name == cls.by_name('試験').name

    def test_branch_by_name(self):
        from zengin_code import Branch

        cls = self._get_target_class()
        b1 = cls(9999, u'試験', u'テスト', u'てすと', 'Test')
        branch = Branch(b1, 999, u'試験支店', u'テスト', u'てすと', 'Test')
        b1.add_branch(branch)
        assert branch.code == b1.branch_by_name('試験支店').code

    def test_bank_name(self):
        cls = self._get_target_class()
        bank = cls.all['0001']
        assert bank.name == 'みずほ銀行'
