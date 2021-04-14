# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department.py
# @Author   : Pluto.
# @Time     : 2021/4/14 16:43
from Interfacedemo.api.department import Department
from Interfacedemo.api.wework import WeWork


class TestDepartment:
    def setup(self):
        wework = WeWork()
        self.department = Department()
        self.token = wework.get_token()

    def test_create_department(self):
        self.department.create_department(self.token, 2)
        list = self.department.get_department_list(self.token)
        assert list["department"][1]["name"] == "技术部"

    def test_update_department(self):
        self.department.update_department(self.token)
        list = self.department.get_department_list(self.token)
        assert list["department"][1]["name"]  == "技术研发中心"

    def test_delete_department(self):
        self.department.delete_department(self.token, 2)
        list = self.department.get_department_list(self.token)
        assert len(list["department"]) == 1

    def test_get_department_list(self):
        list = self.department.get_department_list(self.token)