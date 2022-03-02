# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:45:55 2022

@author: salma
"""
import sys

string = list(sys.argv)
x = ""
if len(sys.argv) > 1:
    for elm in string[1::]:
        x += elm
    x = x.swapcase()
    x = x[::-1]
    print(x)
else:
    pass
    