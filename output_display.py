# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 12:04:06 2021

@author: celin
"""
weight = 20 / 2.205
dosage = weight * 30

print("CORRECT DOSAGE")
print("For a patient weighing {} kg,".format(round(weight)))
print("  the correct dosage is {} mg the first day".format(round(dosage,2)))
