#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
import justpy as jp

class Home:
    path = '/home'

    def server(self):
        wp = jp.QuasarPage(tailwind = True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text = 'This is the home page!', classes='text-4xl m-2')
        jp.Div(a=div, text ='This is a body of home page')
        return wp
