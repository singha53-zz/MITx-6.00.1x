#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:28:07 2019

@author: asingh
"""

# odd tuples
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTup = ()
    for i in range(0,len(aTup),2):
        newTup = newTup + (aTup[i],)
    return newTup

## test case
t = (1, 2, 3, 4)
oddTuples(t)


# Exercise: apply to each 2
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
testList = [1, -4, 8, -9]
def addOne(a):
    return a + 1

applyToEach(testList, addOne)
testList

# Exercise: apply to each 3
testList = [1, -4, 8, -9]
def sqr(a):
    return a**2

applyToEach(testList, sqr)
testList

## dictionaries
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'
animals


# Exercise: how many
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    sum = 0
    for i in aDict:
        sum += len(aDict[i])
    return sum

how_many(animals)

# Exercise: biggest
def biggest(aDict):
    big = {}
    for i in aDict:
        big[i] = len(aDict[i])
    return max(big)

biggest(animals)


