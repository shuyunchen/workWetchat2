#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 20:56
# @Author  : 陈庆云
# @File    : BasePage.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ''

    def __init__(self, web_driver: WebDriver = None):
        self._driver = ''
        if web_driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = web_driver
        if self._base_url != '':
            self._driver.get(self._base_url)
        self._driver.implicitly_wait(3)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    @property
    def driver(self):
        return self._driver
