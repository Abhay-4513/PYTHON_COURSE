# -*- coding: utf-8 -*-
# Write a program using a function to convert temperature in Celsius to Fahrenheit. The formula is F = (C * 9/5) + 32
"""
Created on Tue Sep 22 17:58:49 2026

@author: abhay
"""

def celsiusFahrenheit(c):
    f = (c*(9/5))+32
    print(f"The temperature in fahrenheit is : {f}")

c = float(input("Enter the temperature in celsius : "))
celsiusFahrenheit(c)