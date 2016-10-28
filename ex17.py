#! /usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'jianjiang'

from sys import argv
from os.path import exists
# $ python ex17.py test.txt copied.txt
script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()  # indata = open(from_file).read()
print("from_file:\n", indata)

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()  # 输入是继续还是取消
out_file = open(to_file, 'w')
out_file.write(indata)
print("Alright, all done.")

out_file.close()
in_file.close()

# 验证
target = open(to_file)
print("to_file:\n", target.read())
target.close()
