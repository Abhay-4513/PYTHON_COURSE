# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 22:46:37 2026

@author: abhay
"""

# Write a function to print multiplication table of a given number 

def table(n):
    for i in range(1,11):
        print(f"{n} X {i} : {n*i}")

n = int(input("Enter a number : "))
table(n)