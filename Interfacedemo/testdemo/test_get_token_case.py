# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_get_token_case.py
# @Author   : Pluto.
# @Time     : 2021/4/14 12:42
import pytest
import requests


class TestToken:
    @pytest.mark.parametrize(
        "corpid,corpsecret,errmsg", [("ww0ae123b953d2b956", "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo", "ok"),
                                     ("", "6EnVDtGal3C_RTpEnNbqr4ynHc7AZ--O3MJg-d7E0Bo", "corpid missing"),
                                     ("ww0ae123b953d2b956", "", "corpsecret missing")],
        ids={"正确的corpid和corpsecret","缺少corpid","缺少corpsecret"}
    )
    def test_token(self, corpid, corpsecret, errmsg):
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=token_url)
        print(r.json())
        assert r.json()["errmsg"] == errmsg
