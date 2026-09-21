# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:05:02 2026

@author: abhay
"""

def greatestNumber(num1,num2,num3):
    if num1 > num2 and num1>num3:
        print(f"{num1} is greater")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is greater")
    elif num3 > num1 and num3 > num2:
        print(f"{num3} is greater")
    else:
        print("There is some issue with the numbers...")
        
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

greatestNumber(num1,num2,num3)