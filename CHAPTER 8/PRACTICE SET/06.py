# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:34:34 2026

@author: abhay
"""

# Write a python function which converts inches into cms

def converter():
    n = int(input("Enter the inch value : "))
    Inch = n * 2.54
    print(f"The {n} inch in cm is equal to : {Inch}")
    
converter()