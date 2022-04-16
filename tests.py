#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Для индивидуального задания лабораторной работы 2.21 добавьте тесты с использованием
"""
import sqlite3
import individual1
import unittest
from pathlib import Path
import tempfile
import shutil


class IndTest(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path_dir = Path(self.tmp.name)
        shutil.copyfile(individual1.load(), self.path_dir / 'test.db')
        self.fullpath = self.path_dir / 'test.db'
        self.conn = sqlite3.connect(self.fullpath)
        self.cursor = self.conn.cursor()
        id = 1
        self.cursor.execute(
            f"""
                        SELECT shop_name.name, shops.product, shops.price
                        FROM shops
                        INNER JOIN shop_name ON shop_name.shop_id = shops.shop_id
                        WHERE shop_name.shop_id == {id}
                        """
        )
        rows = self.cursor.fetchall()
        self.result = [
            {
                "name": row[0],
                "product": row[1],
                "price": row[2],
            }
            for row in rows
        ]

    def test_create_db(self):
        self.cursor.execute(
            """
            SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'shops' OR name = 'shop_name'
            """
        )
        table = self.cursor.fetchall()
        self.assertEqual(table, [('shop_name',), ('shops',)])

    def test_add_shop(self):
        self.assertEqual(individual1.add_shop(self.fullpath, 'text', 'text', 3), [{'name': 'text', 'product': 'text', 'price': 3}])

    def test_select_all(self):
        self.assertRaises(TypeError, individual1.select_all(self.fullpath))

    def test1_select_shop_1(self):
        self.assertListEqual(self.result, [{'name': 'magnit', 'product': 'maslo', 'price': 234}])

    def test1_select_shop_2(self):
        self.assertNotEqual(self.result, [{'name': 'nomagnit', 'product': 'kolbasa', 'price': 1000}])
        self.conn.close()
        self.tmp.cleanup()


if __name__ == '__main__':
    unittest.main()
