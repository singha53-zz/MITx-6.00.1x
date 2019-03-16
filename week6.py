#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:13:03 2019

@author: asingh
"""

# Program 1
def program1(x):
    total = 0
    for i in range(1000):
        total += i

    while x > 0:
        x -= 1
        total += x

    return total

# best case
x = 0
program1(x)
# set total = 0; 1 step
# assign i to 0-999: 1000 steps
# add to total: 1000 steps
# return statment: 1 step
2002

# worst case
# set total = 0; 1 step
# assign i to 0-999: 1000 steps
# add to total: 1000 steps
# while x >0: x steps
# substract 1 from x: x steps
# add to total: x steps
# return statment: 1 step
3*x+2*1000+2
3*x+2002

# Program 2
def program2(x):
    total = 0
    for i in range(1000):
        total = i

    while x > 0:
        x = x//2
        total += x

    return total

# best case
2002

# worst case
3*x+2002

# Program 3
def program3(L):
    totalSum = 0
    highestFound = None
    for x in L:
        totalSum += x

    for x in L:
        if highestFound == None:
            highestFound = x
        elif x > highestFound:
            highestFound = x

    return (totalSum, highestFound)

# best case
L = [5, 1, 2, 3]
program3(L)

# set totalSum: 1 step
# set highestFound: 1 step
# for x in L: n steps
# add to totalSum: n steps
# for x i L; n steps
# if statement: 4*n steps
# return statement
7*n+3

# worst case


















