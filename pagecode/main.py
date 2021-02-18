#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 20:58
# @Author  : 陈庆云
# @File    : main.py
# @Software: PyCharm
import json
import os

from selenium.webdriver.common.by import By

from pagecode.BasePage import BasePage
from pagecode.index import Index


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/'

    def click_login(self):
        self._cookie_login()
        self.find(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Index(self.driver)

    def _cookie_login(self):
        # 读取cookie
        file_path = os.path.dirname(__file__) + "\\cookies.json"
        with open(file_path, 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            self._driver.add_cookie(cookie)
