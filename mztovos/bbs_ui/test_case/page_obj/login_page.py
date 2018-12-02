#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""
from base import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    """infoQ
        登陆界面
        1. 点击右上角登陆字样
        2. 连接跳转到登陆页面
        3. 点击密码登陆，跳转
        4. 输入用户名，密码，确认

        待确认：
            1. 如何判断跳转成功？ 如果以接下来的操作，比如定位元素是否成功为判断，这样觉得不妥
    """

    url = "/"
    login_entry_loc = (By.CSS_SELECTOR, "span.route")
    password_entry_loc = (By.CSS_SELECTOR, "p.signin")
    phone_num_loc = (By.CSS_SELECTOR, "[name='cellphone']")
    password_loc = (By.CSS_SELECTOR, "[name='password']")
    button_loc = (By.CSS_SELECTOR, "div.gkui-btn.gkui-big-btn.blue-btn")

    # login page entry
    def enter_login_page(self):
        self.find_element(*self.login_entry_loc).click()

    def change_pw_login(self):
        self.find_element(*self.password_entry_loc).click()

    def login_phone_num(self, phone_num_loc):
        self.find_element(*self.phone_num_loc).send_keys(phone_num_loc)

    def login_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def login_button(self):
        # 多个class属性？ gkui-btn gkui-big-btn blue-btn
        self.find_element(*self.button_loc).click()

    def user_pw_login(self, user_name="", password=""):
        self.open(relative_url=self.url)
        self.enter_login_page()
        self.change_pw_login()
        self.login_phone_num(user_name)
        self.login_password(password)
        self.login_button()

    # hint


