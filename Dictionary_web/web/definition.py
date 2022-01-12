#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import read
from pandas import read_csv
from pprint import pprint
import justpy as jp

class Definition:

    def __init__(self,term:str):
        self.term = term
    
    def get(self):
        df = read_csv('data.csv')
        _definition = tuple(df.loc[df['word']== self.term]['definition'])
        return _definition

if '__main__' == '__name__' :
    my_def = Definition('casing')

    print(my_def.get())