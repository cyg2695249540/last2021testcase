# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : wework.py
# @Author   : Pluto.
# @Time     : 2021/4/14 16:21
import requests


class WeWork():
    def get_token(self):
        corpid = "ww0ae123b953d2b956"
        corpsecret = "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=token_url)
        return r.json()["access_token"]
