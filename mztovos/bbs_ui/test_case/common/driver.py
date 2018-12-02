#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""
from selenium.webdriver import Remote


def get_driver():
    host = "http://127.0.0.1:4444/wd/hub"
    browser = "chrome"
    driver = Remote(command_executor=host, desired_capabilities={"browserName": browser})
    return driver


if __name__ == '__main__':
    get_driver().get("https://www.infoq.cn/")


