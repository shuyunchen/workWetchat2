#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 22:14
# @Author  : 陈庆云
# @File    : BaseTest.py
# @Software: PyCharm
from time import sleep

from pagecode.main import Main


class BaseTest:
    def setup(self):
        self.main = Main()

    def teardown(self):
        sleep(3)
        self.main.driver.quit()
        pass
