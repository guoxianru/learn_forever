# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2020-10-01

"""
    鸭子类型：动态类型和某些静态语言的一种对象推断风格。
"""


class Duck:
    def walk(self):  # 走路
        print("I walk like a duck")

    def swim(self):  # 游泳
        print("i swim like a duck")


class Person:
    def walk(self):  # 走路
        print("this one walk like a duck")

    def swim(self):  # 游泳
        print("this man swim like a duck")


def swim(arg):  # 定义对象实现游泳功能
    arg.swim()


p = Person()  # 实例化
d = Duck()

swim(p)  # 功能实习
swim(d)
