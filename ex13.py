#! /usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'jianjiang'

from sys import argv

# argv结合input使用
# $ python3 ex13.py first 2nd 3rd
script, first, second, third = argv  # 解包

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

fourth = input("Your fourth variable is:")
print("Your fourth variable is:", fourth)
