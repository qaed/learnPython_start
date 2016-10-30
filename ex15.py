#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
# 获取运行参数
script,filename = argv
# 获取文件
txt = open(filename)

print("Here's your file %r:" % filename)
# 输出文件内容
print(txt.read())
# 关闭，释放内存
txt.close()
print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()