# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department.py
# @Author   : Pluto.
# @Time     : 2021/4/24 12:37
import json

import requests
from jsonpath import jsonpath
from jsonschema import validate


class TestDepartment:
    def setup(self):
        corpid = "ww0ae123b953d2b956"
        corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=token_url)
        self.token = r.json()["access_token"]

    def test_create_department(self):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        date = {
            "name": "技术部",
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        r = requests.post(url=create_url, json=date)
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == "created"
        department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        department_list = requests.get(url=department_list_url).json()
        departmentname = department_list["department"][1]["name"]
        assert departmentname == "技术部"

    def test_update_department(self):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        date = {
            "name": "技术研发中心",
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        r = requests.post(url=update_url, json=date)
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == "updated"
        department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        department_list = requests.get(url=department_list_url).json()
        departmentname = department_list["department"][1]["name"]
        assert departmentname == "技术研发中心"


    def test_delete_department(self):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id=2"
        r = requests.get(url=delete_url)
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == "deleted"
        department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        department_list = requests.get(url=department_list_url).json()
        departmentnamelist=jsonpath(department_list,"$..id")
        assert "技术研发中心" not in departmentnamelist

    def test_get_departmentlist(self):
        department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        department_list = requests.get(url=department_list_url).json()
        sechemalist=json.load(open("json_schema/get_department_list_schema.json",encoding="utf-8"))
        validate(department_list,sechemalist)


