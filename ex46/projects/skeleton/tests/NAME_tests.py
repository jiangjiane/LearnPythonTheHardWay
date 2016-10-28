#! /usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'jianjiang'

from nose.tools import *
import NAME

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWAN!")

def test_basic():
    print("I RAN!")
