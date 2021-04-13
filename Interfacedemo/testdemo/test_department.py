# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_department.py
# @Author   : Pluto.
# @Time     : 2021/4/13 21:11
import requests


class TestPartment:
    def setup(self):
        """
        获取token
        """
        corpid = "ww0ae123b953d2b956"
        corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 定义请求方式
        params={
            "corpid":corpid,
            "corpsecret":corpsecret
        }
        r = requests.get(url=url,params=params)
        self.token=r.json()["access_token"]
    def test_create_department(self):
        """
        创建部门
        """
        url="https://qyapi.weixin.qq.com/cgi-bin/department/create"
        params={
            "access_token":self.token
        }
        #定义请求体
        data={
            "name": "技术部",
            "name_en": "JSB",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        r=requests.post(url=url,params=params,json=data)
        assert r.json()["errcode"]==0 and r.json()["errmsg"]=="created"