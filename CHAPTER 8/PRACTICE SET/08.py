# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:13:48 2026

@author: abhay
"""

# Write a python function to remove a given word from a list ad strip it at same time.

def rev(l,word):
    n = []
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
    return n

l = ["abhay","banner","tony","is"]

print(rev(l,"abhay"))