#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 汽车的总数
cars = 100
# 一辆汽车的可载客数
space_in_a_car = 4.0
# 司机总数
drivers = 30
# 乘客数
passengers = 90
# 没有被开走的汽车数
cars_not_driven = cars - drivers
# 被开走的汽车数
cars_driven = drivers
# 可用汽车的单次总载客量
carpool_capacity = cars_driven * space_in_a_car
# 平均每辆车上的乘客数
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")