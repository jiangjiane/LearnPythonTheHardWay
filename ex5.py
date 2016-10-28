#! /usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'jianjiang'

name = 'Zed A.Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# round()  四舍五入函数 如 round(1.7333)

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %d pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %r hair." % (eyes, hair))  # 注意%s和%r的区别
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
print("if I add %d, %d, and %d I get %d." % (age, height, age + height, weight))
