# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:09:50 2026

@author: abhay
"""

# Write a program to print the following star pattern 
# *
#***
#*****


n = int(input("Enter a number : "))


for i in range(1,n+1):
    print("*"*(2*i-1))