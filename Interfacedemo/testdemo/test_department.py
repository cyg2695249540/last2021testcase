# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department.py
# @Author   : Pluto.
# @Time     : 2021/4/13 21:11
import requests
from jsonpath import jsonpath

"""
创建部门>>更新部门>>删除部门
"""


class TestPartment:
    def setup(self):
        """
        获取token
        """
        corpid = "ww0ae123b953d2b956"
        corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=token_url)
        self.token = r.json()["access_token"]

    def test_create_department(self):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        # 定义请求体
        data = {
            "name": "技术部",
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        r = requests.post(url=create_url, json=data)
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == "created"
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_department_list_url).json()
        departmentname = jsonpath(list, "$..department[?(@.id==2)].name")[0]
        # departmentname=list["department"][1]["name"]
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
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_department_list_url).json()
        departmentname = jsonpath(list, "$..department[?(@.id==2)].name")[0]
        assert departmentname == "技术研发中心"

    def test_delete_department(self):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id=2"
        r = requests.get(url=delete_url)
        assert r.json()["errcode"] == 0 and r.json()["errmsg"] == "deleted"
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        list = requests.get(url=get_department_list_url).json()
        departmentlist=jsonpath(list,"$..id")
        assert 2 not in departmentlist

