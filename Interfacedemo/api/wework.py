# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : wework.py
# @Author   : Pluto.
# @Time     : 2021/4/14 16:21
import requests

from Interfacedemo.api.base_api import BaseApi


class WeWork(BaseApi):
    def get_token(self):
        corpid = "ww0ae123b953d2b956"
        corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        req = {
            "method": "get",
            "url": token_url
        }
        r=self.send_and_requests(req)
        self.token = r.json()["access_token"]
        return self.token
