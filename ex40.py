#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 这是列表
things = ['a', 'b', 'c', 'd']
print(things[1])

things[1] = 'z'
print(things[1])
print(things)

# 这是字典dict
stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
print(stuff['name'])

stuff['city'] = "San Francisco"
print(stuff['city'])

# 还可以这样
stuff[1] = ['Wow']
stuff[2] = ['Neato']
print(stuff[1])
print(stuff)

# 删除用del
del stuff['city']
del stuff[1]
print(stuff)

# 练习
# 注意使用的是大括号{}
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap,state):
    if state in themap:
        return themap[state]
    else:
        return "Not Found."

# ok pay attention!
# 字典中可以保存函数
cities['_find'] = find_city

while True:
    print("State?(ENTER to quit)")
    state = input("> ")

    if not state:break

    # this line is the most important ever! study!
    city_found = cities['_find'](cities, state)
    print(city_found)
