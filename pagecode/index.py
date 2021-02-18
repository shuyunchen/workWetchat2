#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 21:00
# @Author  : 陈庆云
# @File    : index.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from pagecode.BasePage import BasePage
from pagecode.contact import Contact


class Index(BasePage):
    def click_contact(self):
        self.find(By.ID, 'menu_contacts').click()
        return Contact(self.driver)
