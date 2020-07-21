# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 20:15:34 2020

@author: aphics
"""


from pandas import read_csv

def leer_datos(path, *columns):
    
    datos = read_csv(path, usecols=columns)
    
    return datos