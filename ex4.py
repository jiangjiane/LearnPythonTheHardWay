#! /usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'jianjiang'

cars = 100  # 总的车数量
space_in_a_car = 4.0  # 每个车的空间
drivers = 30  # 司机数量
passengers = 90  # 乘客
cars_not_driven = cars-drivers  # 没用上的车
cars_driven = drivers  # 需要用的车=司机
carpool_capacity = cars_driven * space_in_a_car  # 一次最大载客量
average_passengers_per_car = passengers / cars_driven  # 平均每辆车的载客量

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")
