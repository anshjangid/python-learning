# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:04:58 2026

@author: acer
"""

W=int(input("Enter Weight of the person:"))
H=int(input("Enter Height of the person:"))

bmi=W/(H**2)

if bmi>35:
    print("they are clinically obese")
    
elif bmi>30:
    print("they are obese")
    
elif bmi>18.5:
    print("they have a normal weight")
    
else:
    print("they are under weight")