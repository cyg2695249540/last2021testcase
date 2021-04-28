# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : contact_page.py
# @Author   : Pluto.
# @Time     : 2021/4/27 14:32
from time import sleep

from selenium.webdriver.common.by import By

from seleniumdemo.pages.base_page import BasePage


class ContactPage(BasePage):
    _addmember_butto = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")

    _member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

    _delete_butto = (By.CSS_SELECTOR, ".js_delete")
    _delete_chick = (By.CSS_SELECTOR, "[d_ck='submit']")

    _create_dropdown = (By.CSS_SELECTOR, ".js_create_dropdown")
    _addepartment = (By.CSS_SELECTOR, ".js_create_party")
    _jstree_anchor = (By.CSS_SELECTOR, ".jstree-anchor")

    def goto_addmember_page(self):
        from seleniumdemo.pages.addmember_page import AddmemberPage
        self.wait_for_clickable(self._addmember_butto)
        self.find_and_click(self._addmember_butto)
        return AddmemberPage(self.driver)

    def get_mamberlist(self):
        self.wait_for_clickable(self._member_list)
        eles = self.finds(self._member_list)
        return [name.text for name in eles]

    def delete_member_page(self, username):
        deletename_checkbox = (By.XPATH, f"//*[@title='{username}']/..//*[@class='ww_checkbox']")
        eles = self.finds(self._member_list)
        namelist = [name.text for name in eles]
        if username in namelist:
            self.find_and_click(deletename_checkbox)
            self.find_and_click(self._delete_butto)
            self.find_and_click(self._delete_chick)
        else:
            print(f"不存在成员{username}")
            return self

    def goto_addepartment_page(self):
        from seleniumdemo.pages.department_page import DepartmentPage
        self.find_and_click(self._create_dropdown)
        self.find_and_click(self._addepartment)
        return DepartmentPage()

    def get_department_list(self):
        sleep(1)
        eles = self.finds(self._jstree_anchor)
        return [name.text for name in eles]
