#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 21:01
# @Author  : 陈庆云
# @File    : add_department.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pagecode.BasePage import BasePage


class AddDepartment(BasePage):
    def add_department(self, department_name):
        self.find(By.NAME, 'name').send_keys(department_name)
        self.find(By.CSS_SELECTOR, '.js_parent_party_name').click()
        self.find(By.CSS_SELECTOR, '.member_tag_dialog [id="1688850811907410_anchor"]').click()
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        wait = WebDriverWait(self.driver, 5, 0.5)
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ww_commonCntHead_title_inner_text [id='party_name']")),
            message="")

        return AddDepartment(self.driver)

    def get_depatment_list(self):
        print('_____________________')
        self.driver.refresh()
        print(self.find(By.CSS_SELECTOR, '.jstree-default').text)
        return self.find(By.CSS_SELECTOR, '.jstree-default').text

