# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department.py
# @Author   : Pluto.
# @Time     : 2021/4/14 16:43
import json

import allure
import pytest
import yaml

from Interfacedemo.api.department import Department


@allure.feature("部门模块")
class TestDepartment:
    def setup_class(self):
        self.department = Department()
        # 通过获取不同的secret，获取不同的权限给不同的测试用例使用
        token_info = yaml.safe_load(open("config.yaml", encoding="utf-8"))
        # corpsecret = token_info["token"]["department_secret"]
        # 解决深层次取值方式
        department_secret = self.department.base_jsonpath(token_info, "$..department_secret")[0]
        self.department.get_token(department_secret)

    @allure.story("添加部门")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("department_name, department_id", [("技术部", 2)], ids={"添加部门"})
    def test_create_department(self, department_name, department_id):
        r = self.department.create_department(department_name, department_id)
        assert r["errcode"] == 0 and r["errmsg"] == "created"
        department_list = self.department.get_department_list()
        departmentname = \
            self.department.base_jsonpath(department_list, f"$..department[?(@.id=={department_id})].name")[0]
        assert departmentname == department_name

    @allure.story("更新部门")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("department_name,department_id", [("技术研发中心", 2)], ids={"更新部门"})
    def test_update_department(self, department_name, department_id):
        r = self.department.update_department(department_name, department_id)
        assert r["errcode"] == 0 and r["errmsg"] == "updated"
        list = self.department.get_department_list()
        departmentname = self.department.base_jsonpath(list, f"$..department[?(@.id=={department_id})].name")[0]
        assert departmentname == department_name

    @allure.story("删除部门")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("department_id", [(2)], ids={"删除部门"})
    def test_delete_department(self, department_id):
        r = self.department.delete_department(department_id)
        assert r["errcode"] == 0 and r["errmsg"] == "deleted"
        list = self.department.get_department_list()
        department_ids = self.department.base_jsonpath(list, "$..id")
        assert department_id not in department_ids

    @allure.story("字段校验")
    @pytest.mark.flaky(reruns=1)
    def test_get_department_list(self):
        list = self.department.get_department_list()
        schemalist = json.load(open("./json_schema/get_department_list_schema.json", encoding="utf-8"))
        self.department.base_jsonschema(list, schemalist)
