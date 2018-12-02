#!/usr/bin/env python
# encoding: utf-8
"""
page base
@author: cbr
"""
from selenium.webdriver import Chrome


class Page(object):
    """
        open, find_element, find_elements,
    """
    base_url = "http://www.infoq.cn"

    def __init__(self, selenium_driver, base_url=base_url):
        self.driver = selenium_driver
        self.base_url = base_url

    def open(self, relative_url="/"):
        url = self.base_url + relative_url
        self._open(url)

    def _open(self, url):
        self.driver.get(url)
        return self.on_page(url)

    def on_page(self, url):
        """judge current url"""
        return self.driver.current_url == url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)


if __name__ == '__main__':
    Page(Chrome()).open()