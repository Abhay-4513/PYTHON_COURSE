# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:00:47 2026

@author: abhay
"""

# Write a program to calculate the factorial of given number using for loop
n = int(input("Enter the number : "))
fact = 1
for i in range(1,n+1):
    
    fact = fact * i
    
print(fact)