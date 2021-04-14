# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : department.py
# @Author   : Pluto.
# @Time     : 2021/4/14 16:22
import requests

from Interfacedemo.api.wework import WeWork


class Department(WeWork):
    def create_department(self,department_id):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        # 定义请求体
        date = {
            "name": "技术部",
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": department_id
        }
        req={
            "method":"post",
            "url":create_url,
            "json":date
        }
        r = self.send_and_requests(req)
        return r.json()

    def update_department(self):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        date = {
            "name": "技术研发中心",
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        req = {
            "method": "post",
            "url": update_url,
            "json": date
        }
        r = self.send_and_requests(req)
        return r.json()

    def delete_department(self,department_id):
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}"
        req={
            "method":"get",
            "url":delete_url
        }
        r = self.send_and_requests(req)
        return r.json()

    def get_department_list(self):
        get_department_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        req = {
            "method": "get",
            "url": get_department_list_url
        }
        r = self.send_and_requests(req)
        return r.json()
