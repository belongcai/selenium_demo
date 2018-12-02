#!/usr/bin/env python
# encoding: utf-8
"""
对unittest 简单封装，实现 setup teardown
@author: cbr
"""

from unittest import TestCase
from driver import get_driver


class BaseUnit(TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

