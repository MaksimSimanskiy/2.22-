#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Для индивидуального задания лабораторной работы 2.21 добавьте тесты с использованием
модуля unittest, проверяющие операции по работе с базой данных.
"""

import individual1
import unittest
from pathlib import Path


class IndTest(unittest.TestCase):

    def setUp(self):
        self.args = str(Path.home() / "shops.db")
        self.db_path = Path(self.args)

    def test1_create_db(self):
        self.assertEqual(individual1.create_db(self.db_path), 2)

    def test_add_shop(self):
        self.assertEqual(individual1.add_shop('text', 'text', 3), [{'name': 'text', 'product': 'text', 'price': 3}])
        individual1.delete_shop()

    def test1_select_shop(self):
        self.assertListEqual(individual1.select_shop("magnit"), [{'name': 'magnit', 'product': 'maslo', 'price': 234}])


if __name__ == '__main__':
    unittest.main()
