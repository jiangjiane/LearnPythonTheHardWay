#! /usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'jianjiang'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)

# 转义字符练习
I = ["/", "-", "|", "\\", "|"]
while True:
    for i in I:
        print("%s\r" % i)

