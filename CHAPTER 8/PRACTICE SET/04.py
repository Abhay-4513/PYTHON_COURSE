# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 23:17:21 2026

@author: abhay
"""

# Write a recursive function to calculate the sum of first n natural number 

def sum(n):
    if n == 1:
        return 1
    
    return sum(n-1) + n


n = int(input("Enter a number : "))
print(f"The sum of firts {n} number is : {sum(n)}")
