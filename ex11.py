#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print("How old are you?",end="")
# python3没有raw_input()
age = input()
print("How tall are you?",end="")
height = input()
print("How much do you weight?",end="")
weight = input()
# 即使输入的是数字，输出的也是字符串
print("So,you're %r old, %r tall and %r heavy." % (age, height, weight))