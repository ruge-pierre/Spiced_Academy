#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 11:33:32 2021

@author: pierre-ru
"""

def FizzBuzz_Test(n):
    for i in range(1, n+1):
        if (i % 3) == 0 and (i % 5) == 0:
            print("FizzBuzz")
        elif (i % 3) == 0:
            print("Fizz")
        elif (i % 5) == 0:
            print("Buzz")
        else:
            print(i)

FizzBuzz_Test(100)