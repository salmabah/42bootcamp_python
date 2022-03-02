# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 02:34:39 2022

@author: Salma
"""

def text_analyzer(chaine):
    upper_nb = 0
    lower_nb = 0
    pnt = 0
    space = 0
    for i in chaine:
        if i.isupper():
            upper_nb += 1
        elif i.islower():
            lower_nb += 1
        elif i in [',', ';', '.', ':', '!', '?']:
            pnt += 1
        elif i == ' ':
            space += 1
    #affichage
    print('- ',upper_nb,' upper letter(s)')
    print('- ',lower_nb,' lower letter(s)')
    print('- ',pnt,' ponctiation character(s)')
    print('- ',space,' space(s)')