#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from datetime import datetime
from meijumi import URL, MeiJuMi

class MjMTest(unittest.TestCase):
	def setUp(self):
		self.year = 2014
		self.month = 10
		self.day = 30
		today = datetime(self.year, self.month, self.day)
		self.m = MeiJuMi(URL, today)

	def test_month_end_day(self):
		"""测试获取本月最后一天的号数"""
		self.assertEqual(self.m.month_end_day(), 31)

	def test_get_day(self):
		"""测试获取当天天数"""
		self.assertEqual(self.m.get_day(), self.day)

	def test_set_day_str(self):
		"""根据天数，生成一个含“号”的字符串"""
		self.assertEqual(self.m.set_day_str(), str(self.day)+'号')
		self.assertEqual(self.m.set_day_str(day=25), '25号')

if __name__ == '__main__':
	unittest.main()