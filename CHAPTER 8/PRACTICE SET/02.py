# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:58:49 2026

@author: abhay
"""

def celsiusFahrenheit(c):
    f = (c*(9/5))+32
    print(f"The temperature in fahrenheit is : {f}")
c = float(input("Enter the temperature in celsius : "))
celsiusFahrenheit(c)