# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from collections import OrderedDict


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
        b1 = cls('9999', u'試験', u'テスト', u'てすと', 'Test')
        assert b1 is cls['9999']

    def test_to_dict(self):
        from zengin_code.branch import Branch

        cls = self._get_target_class()
        cls['9999'].branches['999'] = Branch(cls['9999'], '999', u'試験1', u'テスト1', u'てすと1', 'Test1')
        cls['9999'].branches['998'] = Branch(cls['9999'], '998', u'試験2', u'テスト2', u'てすと2', 'Test2')

        assert cls['9999'].to_dict() == {
            'code': '9999',
            'name': u'試験',
            'kana': u'テスト',
            'hira': u'てすと',
            'roma': 'Test',
            'branches': (OrderedDict([
                ('999', {
                    'bank': {
                        'code': '9999',
                        'name': u'試験',
                        'kana': u'テスト',
                        'hira': u'てすと',
                        'roma': 'Test',
                    },
                    'code': '999',
                    'name': u'試験1',
                    'kana': u'テスト1',
                    'hira': u'てすと1',
                    'roma': 'Test1',
                }),
                ('998', {
                    'bank': {
                        'code': '9999',
                        'name': u'試験',
                        'kana': u'テスト',
                        'hira': u'てすと',
                        'roma': 'Test',
                    },
                    'code': '998',
                    'name': u'試験2',
                    'kana': u'テスト2',
                    'hira': u'てすと2',
                    'roma': 'Test2',
                }),
            ]),),
        }
