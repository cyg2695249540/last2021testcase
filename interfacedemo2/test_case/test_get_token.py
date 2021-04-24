# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_get_token.py
# @Author   : Pluto.
# @Time     : 2021/4/24 13:30
import allure
import pytest
import yaml

from interfacedemo2.api.base_api import BaseApi

def getdatas():
    datas=yaml.safe_load(open("../datas/datas.yaml",encoding="utf-8"))
    demo = datas["demo"]
    case = datas["case"]
    return demo, case

@allure.feature("获取get_token模块")
class TestGetToken:
    def setup(self):
        self.token = BaseApi()

    @allure.story("geteoken测试")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("corpid,corpsecret,errmsg",getdatas()[0],ids=getdatas()[1])
    def test_get_token(self,corpid,corpsecret,errmsg):
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        req = {
            "method": "get",
            "url": token_url
        }
        r = self.token.send_and_requests(req)
        assert r.status_code == 200 and r.json()["errmsg"] == errmsg
