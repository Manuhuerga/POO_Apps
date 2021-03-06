#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import justpy as jp
from definition import Definition

class Dicctionary:
    path = '/dic'
    
    @classmethod
    def server(cls, req):
        wp = jp.QuasarPage(tailwind = True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text = 'Instant English dicctionary!', classes='text-4xl m-2')
        jp.Div(a=div, text ='Get the definition of any english word', classes = 'text-lg')

        input_div = jp.Div(a=div, classes='grid grid-cols-2')
        input_box = jp.Input(a=input_div, placeholder= 'Type a word', 
                            classes='m-2 bg-gray-100 border-2 border-gray-200 rounded w-64\
                            focus:bg-white focus:outline-none focus:border-purple-500 py-2 px-4')

        output_div = jp.Div(a=div, classes ='m-2 p-2 text-lg border-2 h-40')
        jp.Button(a=input_div, text='Get definition', classes='border-2 text-gray-500', click = cls.get_definition
        ,outputdiv=output_div, inputbox = input_box)

        print(cls,req)
        return wp
    
    @staticmethod
    def get_definition(widget,msg):
        defined = Definition(widget.inputbox.value).get()
        widget.outputdiv.text = " ".join(defined)

