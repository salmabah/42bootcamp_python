# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 01:26:12 2022

@author: salma
"""

import sys

if len(sys.argv) == 1:
    pass
elif len(sys.argv) == 2:
    if isinstance(sys.argv[1], int):
        entier = int(sys.argv[1])
        if entier % 2 == 0 and entier != 0:
            print("I'm Even")
        elif entier == 0:
            print("I'm Zero")
        else:
            print("I'm Odd")
    else:
        print("ValueError: invalid literal for int")
else:
    print("AssertionError: more than one argument are provided")
