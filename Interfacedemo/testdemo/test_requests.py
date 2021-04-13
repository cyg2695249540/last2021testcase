# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_requests.py
# @Author   : Pluto.
# @Time     : 2021/4/13 20:47
import requests


class TestToken:
    def test_get_token(self):
        """
        获取token
        """
        corpid="ww0ae123b953d2b956"
        corpsecret="6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r=requests.get(url)
        print(r.json())

    def test_token_param(self):
        """
        获取token第二种形式
         """
        corpid = "ww0ae123b953d2b956"
        corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 定义请求方式
        params={
            "corpid":corpid,
            "corpsecret":corpsecret
        }
        r = requests.get(url,params)
        print(r.json())