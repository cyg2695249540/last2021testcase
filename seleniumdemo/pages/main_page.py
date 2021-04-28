# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : main_page.py
# @Author   : Pluto.
# @Time     : 2021/4/27 14:32
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from seleniumdemo.pages.addmember_page import AddmemberPage
from seleniumdemo.pages.base_page import BasePage
from seleniumdemo.pages.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"
    _addmember = (By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")
    _contact_butto = (By.CSS_SELECTOR, "#menu_contacts")

    def goto_addmember_page(self):
        self.find_and_click(self._addmember)
        return AddmemberPage(self.driver)

    def goto_contact_page(self):
        self.find_and_click(self._contact_butto)
        return ContactPage(self.driver)
