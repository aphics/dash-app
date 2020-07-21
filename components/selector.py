# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 20:28:29 2020

@author: aphics
"""


import dash_core_components as dcc

def crear_selector(options, id, **kwargs):
    
    selector = dcc.Dropdown(options= options, id= id, **kwargs)
    
    return selector