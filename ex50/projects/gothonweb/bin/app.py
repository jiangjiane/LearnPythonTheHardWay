#! /usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'jianjiang'

import web

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        greeting = "Hello World"
        return greeting

if __name__ == "__main__":
    app.run()
