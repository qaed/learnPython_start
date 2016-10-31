#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数定义注意事项:
# 函数定义是以 def 开始的吗？
# 函数名称是以字符和下划线 _ 组成的吗？
# 函数名称是不是紧跟着括号 ( ？
# 括号里是否包含参数？多个参数是否以逗号隔开？
# 参数名称是否有重复？（不能使用重复的参数名）
# 紧跟着参数的是不是括号和冒号 ): ？
# 紧跟着函数定义的代码是否使用了 4 个空格的缩进 (indent)？
# 函数结束的位置是否取消了缩进 (“dedent”)？

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# ok,that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print("arg1: %r" % arg1)

#this one takes no argument
def print_none():
    print("I got nothing.")

# 函数使用注意事项
# 调运函数时是否使用了函数的名称？
# 函数名称是否紧跟着 ( ？
# 括号后有无参数？多个参数是否以逗号隔开？
# 函数是否以 ) 结尾？

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# 运行函数(run)’、‘调用函数(call)’、和 ‘使用函数(use)’是同一个意思