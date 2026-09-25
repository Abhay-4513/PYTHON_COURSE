# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 22:24:22 2026

@author: abhay
"""

def pattern(n):
    
    if n == 0:
        return 
    
    print("*"*n)
    pattern(n-1)

n = int(input("Enter a number : "))
pattern(n)