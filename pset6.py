#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:18:02 2019

@author: asingh
"""

# Problem 1-1
## The ONLY thing we are interested in when designing programs is that 
## it returns the correct answer.
## False, also interesting in many other things (error messages, behaviours)

# Problem 1-2
## When determining asymptotic complexity, we discard all terms 
## except for the one with the largest growth rate.
## True; worst case

# Problem 1-3
## Bisection search is an example of linear time complexity
## False, O(logn) complexity

# Problem 1-4
## For large values of n, an algorithm that takes 20000n^2 steps has better 
## time complexity (takes less time) than one that takes 0.001n^5 steps
## True n^5 > n^2 when n is very large

# Problem 2-1
## Indirection, as talked about in lecture, means you have to 
## traverse the list more than once.
## no its about referencing a given value

# Problem 2-2
## The complexity of binary search on a sorted list of n items is O(logn)
## True; the algorithm still does what it does lol

# Problem 2-3
## The worst case time complexity for selection sort is O(n^2).
## True

# Problem 2-4
## The base case for the recursive version of merge sort from lecture 
## is checking ONLY for the list being empty.
## also checking if there is 1 or 2 elements?

# Problem 3
## For each of the following expressions, select the order of growth 
## class that best describes it from the following list:  
## Assume c is some constant.
## simply look at the term with the highest complexity

# Problem 4-1
## Consider the following Python procedure. Specify its order of growth.
def modten(n):
    return n%10
## Modulo/remainder is a O(1) operation (it's essentially just a 
## variation on division, which takes constant time on fixed-sized numbers). 

# Problem 4-2
## Consider the following Python procedure. Specify its order of growth.
def multlist(m, n):
    '''
    m is the multiplication factor
    n is a list.
    '''
    result = []
    for i in range(len(n)):
        result.append(m*n[i])
    return result 
## 1 + O(len(n)) + 1 ~ O(len(n))

# Problem 4-3
## Consider the following Python procedure. Specify its order of growth.
def foo(n):
    if n <= 1:
        return 1
    return foo(n/2) + 1
## worst case: n is very large number, 1 + O(logn)   

# Problem 4-4
## Consider the following Python procedure. Specify its order of growth.
def recur(n):
    if n <= 0:
        return 1
    else:
        return n*recur(n-1)
## 1 + O(n) -> like going down a list

# Problem 4-5
## Consider the following Python procedure. Specify its order of growth.
def baz(n):
    for i in range(n):
        for j in range(n):
            print( i,j )
## O(n) *  O(n) ~ O(n^2)            

# Problem 5
## Here is code for linear search that uses the fact that a set of 
## elements is sorted in increasing order:
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
## O(n)
## Consider the following code, which is an alternative version of search.
def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False
## Which of the following statements is correct? You may assume that 
## each function is tested with a list L whose elements are sorted in 
## increasing order; for simplicity, assume L is a list of positive integers.

L = [1, 2]
e = 2
search(L, e)
newsearch(L, e)

# Problem 6
## Answer the questions below based on the following sorting function. 
## If it helps, you may paste the code in your programming environment. 
## Study the output to make sure you understand the way it sorts.
def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
L = [3, 2, 1]
swapSort(L)

# Problem 6-2
## What is the worst case time complexity of swapSort? Consider
## different kinds of lists when the length of the list is large.
## O(n^2)

# Problem 6-3
## If we make a small change to the line for j in range(i+1, len(L)): 
## such that the code becomes:
def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            print(j, i)
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
L = [3, 2, 1]
modSwapSort(L)
L = [1, 2, 3]
modSwapSort(L)
L = [1,4,8,2,1,1]
modSwapSort(L)

# Problem 6-4
## What happens to the time complexity of this modSwapSort?
## O(n) * O(n)
## best case: list if the right order
L = [1, 2, 3]
swapSort(L)
L = [3, 2, 1]
modSwapSort(L)
## worst case: list is in the reverse order
L = [3, 2, 1]
swapSort(L)
L = [1, 2, 3]
modSwapSort(L)
## best and worst case changes (WRONG!)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



