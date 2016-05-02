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
