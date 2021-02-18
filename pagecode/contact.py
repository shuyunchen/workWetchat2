#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 21:00
# @Author  : 陈庆云
# @File    : contact.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pagecode.BasePage import BasePage
from pagecode.add_department import AddDepartment


class Contact(BasePage):
    def click_add_department(self):
        self.find(By.CSS_SELECTOR, '.js_create_dropdown').click()
        self.find(By.CSS_SELECTOR, '.js_create_party').click()
        return AddDepartment(self._driver)

    def del_department(self, name):
        print('del_department')
        self.find(By.LINK_TEXT, name).click()
        self.find(By.XPATH, f'//*[text()="{name}"]/span').click()
        self.find(By.XPATH, '/html/body/ul/li[7]/a').click()
        wait = WebDriverWait(self.driver, 5, 0.5)
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[text()="确定"]')),
            message="没有确定按钮")

        self.find(By.XPATH, '//*[text()="确定"]').click()
