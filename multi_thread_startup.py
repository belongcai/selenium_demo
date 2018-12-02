#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""
from threading import Thread
from selenium.webdriver import Remote
from selenium.webdriver.common.by import By


def open_url(host, browser):
    dc = {"browserName": browser}
    driver = Remote(command_executor=host, desired_capabilities=dc)
    driver.get("https://www.baidu.com/")
    driver.find_element(By.CSS_SELECTOR, ".s_ipt").send_keys("selenium")
    driver.find_element(By.CSS_SELECTOR, "span>input#su").click()
    driver.close()


if __name__ == '__main__':
    threads = []
    names = {
        "http://127.0.0.1:4444/wd/hub": "chrome",
        "http://127.0.0.1:5555/wd/hub": "chrome",
    }

    for k, v in names.iteritems():
        t = Thread(target=open_url, args=(k, v))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("end")

