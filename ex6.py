#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# %赋值可以直接写在外面
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)
print(x)
print(y)
# %r保存原本格式输出，x是字符串。自带双引号
print("I said : %r." % x)
# %s输出字符串，y是字符串，相当于“+”操作
print("I also said : '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with right side."

print(w + e)


