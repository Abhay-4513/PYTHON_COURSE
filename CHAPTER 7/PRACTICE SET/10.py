# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:49:25 2026

@author: abhay
"""

# Write a program to multiplication table of a given number using for loop in reversed order.

n = int(input("Enter a number : "))

for i in range(1,11):
    a = n * (11-i)
    print(a)