# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : test_web.py
# @Author   : Pluto.
# @Time     : 2021/4/26 20:01
import time

from selenium import webdriver


class TestDriber():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_web(self):
        self.driver.maximize_window()
        self.driver.get(url="https://ceshiren.com")
        self.driver.find_element_by_xpath("//*[@title='所有分类']").click()
        time.sleep(3)
