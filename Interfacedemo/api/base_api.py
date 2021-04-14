# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : base_api.py
# @Author   : Pluto.
# @Time     : 2021/4/14 17:15
import requests


class BaseApi:
    def send_and_requests(self, req:dict):
        return requests.request(**req)
