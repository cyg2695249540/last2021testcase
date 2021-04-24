# !/usr/bin/env Python3
# -*- coding: utf-8 -*-
# @FILE     : ip2.py
# @Author   : Pluto.
# @Time     : 2021/4/24 9:16
a = "192.0.0.1?!289.0.0.1!0.0.0.0!192.163.10.28?192.0.0.1"


def ip():
    a = "192.0.0.1?!289.0.0.1!0.0.0.0!192.163.10.28?192.0.0.1"
    b = a.replace("?", "!").split("!")
    b=set(b)
    listb = []
    for i in b:
        if i != "":
            listb.append(i)
    # listb.sort(key=lambda x: x[-1])
    listb = sorted(listb, key=lambda x: x[-1])
    print(a)
    print(listb)
    for i in listb:
        print(i)


if __name__ == '__main__':
    ip()
