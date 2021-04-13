# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_requestdemo.py
# @Author   : Pluto.
# @Time     : 2021/4/13 16:14
import requests


class TestDemo:
    def test_get(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    #构造参数
    def test_querey(self):
        payload = {
            "level": "1",
            "name": "seveniruby"
        }
        r = requests.get("https://httpbin.testing-studio.com/get",params=payload)
        print(r.text)
        assert r.status_code==200

    def test_post(self):
        payload = {
            "level": "1",
            "name": "seveniruby"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", params=payload)
        print(r.text)
        assert r.status_code == 200