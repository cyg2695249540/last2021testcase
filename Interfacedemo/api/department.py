# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : department.py
# @Author   : Pluto.
# @Time     : 2021/4/14 16:22
import requests

from Interfacedemo.api.wework import WeWork


class Department():
    def create_department(self,token,department_id):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token}"
        # 定义请求体
        data = {
            "name": "技术部",
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": department_id
        }
        r = requests.post(url=create_url, json=data)
        return r.json()

    def update_department(self,token):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={token}"
        date = {
            "name": "技术研发中心",
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        r = requests.post(url=update_url, json=date)
        return r.json()

    def delete_department(self,token,department_id):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={token}&id={department_id}"
        r = requests.get(url=delete_url)
        return r.json()

    def get_department_list(self,token):
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}"
        r = requests.get(url=get_department_list_url)
        return r.json()
