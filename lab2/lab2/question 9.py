# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 23:12:10 2026

@author: Ansh
"""

widgets = int(input("Enter the number of widgets ordered: "))
if widgets >= 100:
    cost = widgets * 0.20
else:
    cost = widgets * 0.25
print("Total cost =", cost, "dollars")