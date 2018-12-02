#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""
import unittest, sys
from mztovos.bbs_ui.test_case.common.base_unit import BaseUnit
from mztovos.bbs_ui.test_case.page_obj.login_page import LoginPage


class TestLogin(BaseUnit):
    """
        有几个问题
        1. 过程比较慢，可以发现页面一直在转圈
        2.
    """
    def test_login_empty_cellphone_and_password(self):
        LoginPage(self.driver).user_pw_login()


if __name__ == '__main__':
    unittest.main()