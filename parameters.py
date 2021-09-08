# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:46:49 2021

@author: celin
"""
def update(a):
    a[0] = a[0] + 2
    return a

def main():
    b = [5]
    x = update(b)
    print(b)
    print(x)
    
if __name__ == "__main__":
    main()