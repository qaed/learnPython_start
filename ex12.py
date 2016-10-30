#!/usr/bin/env python3
# -*- coding: utf-8 -*-


age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weight?")
# 即使输入的是数字，输出的也是字符串
print("So,you're %r old, %r tall and %r heavy." % (age, height, weight))

# 命令行下python -m pydoc <方法名> 可以查看方法说明文档