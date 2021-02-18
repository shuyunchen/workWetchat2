#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 21:02
# @Author  : 陈庆云
# @File    : test_add_department.py
# @Software: PyCharm
import random
from time import sleep

import pytest

from pagecode.contact import Contact
from testcode.BaseTest import BaseTest


def get_test_datas(k):
    datas = []
    for i in range(k):
        m = random.randint(10000, 99999)
        datas.append("test" + str(m))
    return datas


class TestAddDepartment(BaseTest):

    @pytest.mark.parametrize("department_name", get_test_datas(1))
    def test_add_department(self, department_name):
        assert department_name in self.main.click_login().click_contact().click_add_department().add_department(
            department_name).get_depatment_list()
        sleep(3)
        contact = Contact(self.main.driver)
        contact.del_department(department_name)
        # assert department_name ==
