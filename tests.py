#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Для индивидуального задания лабораторной работы 2.21 добавьте тесты с использованием
"""
import sqlite3
import individual1
import unittest
from pathlib import Path


class IndTest(unittest.TestCase):

    def setUp(self):
        self.args = str(Path.home() / "shops.db")
        self.db_path = Path(self.args)

    def test1_add_shop(self):
        with self.assertRaises(TypeError):
            individual1.add_shop('text', 'text')

    def test2_add_shop(self):
        with self.assertRaises(sqlite3.IntegrityError):
            individual1.add_shop(3, 3, 3)

    def test3_add_shop(self):
        with self.assertRaises(sqlite3.IntegrityError):
            individual1.add_shop('text', 3, 3)

    def test4_add_shop(self):
        with self.assertRaises(sqlite3.IntegrityError):
            individual1.add_shop('text', 3, 'text')

    def test_create_db(self):
        self.assertRaises(TypeError, individual1.create_db(self.db_path))

    def test_select_all(self):
        self.assertRaises(TypeError, individual1.select_all())

    def test1_select_shop(self):
        self.assertListEqual(individual1.select_shop("magnit"), [{'name': 'magnit', 'product': 'maslo', 'price': 234}])

    def test2_select_shop(self):
        self.assertNotEqual(individual1.select_shop("magnit"), [{'name': 'magnit', 'product': 'maslo', 'price': '234'}])

    def test3_select_shop(self):
        self.assertNotEqual(individual1.select_shop("magnit"), [{'name': 'Nomagnit', 'product': 'maslo', 'price': '234'}])


if __name__ == '__main__':
    unittest.main()
