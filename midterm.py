#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:20:56 2019

@author: asingh
"""

# Problem 1-1
x = "pi"
y = "pie"
x, y = y, x

## Problem 1-2
def f1(x):
    while x > 3:
        f(x+1)

# For any value of x, all calls to f1 are guaranteed to never terminate. (False)

# Problem 1-3
## A Python program always executes every line of code written at least once. (False)

# Problem 1-4
## Suppose you have two different functions that each assign a variable called x. Modifying x in one function means you always modify x in the other function for any x. (False)
        
# Problem 1-5
## The following code will enter an infinite loop for all values of i and j.
while i >= 0:
    while j >= 0:
        print(i, j)
# False
        
# Problem 1-6
## It is always possible and feasible for a programmer to come up with test cases that run through every possible path in a program. (False)
        
# Problem 1-7
# Assume f() is defined. In the statement a = f(), a is always a function. (False, it will return a value)
        
# Problem 1-8
## A program that keeps running and does not stop is an example of a syntax error. (False, no because then you should get an error)
        
# Problem 1-9
def f(x):
    a = []
    while x > 0:
        a.append(x)
        print(a)
        f(x-1)    
        
# A new object of type list is created for each recursive invocation of f. (True)  

# Problem 1-10
# A tuple can contain a list as an element. (True)
a = (1, [1,2,3], 3)

# Problem 2-1
## Consider the statement: L = {'1':1, '2':2, '3':3}. Which is correct?
## Ans: L maps strings to integers

# Problem 2-2  
## Assume a break statement is executed inside a loop and that the loop is inside a function. Which of the following is correct?      
## Ans: The function might immediately terminate.  (got it Wrong) 
## maybe  The loop will always immediately terminate. ?

# Problem 2-3
## In Python, which of the following is a mutable object? (a list)     

# Problem 2-4
## Assume the statement s[1024] = 3 does not produce an error message. This implies:
# ans (all of the above) WRONG! it cant be a string because the return would be a str not int
## type(s) can be str
## type(s) can be tuple
## type(s) can be list
s = 'str'
s1 = (1, 2, 3)
s2 = [1, 2, 3]
s[0]; s1[0]; s2[0]
        
# Problem 2-5
L = [1,2,3]
d = {'a': 'b'}
def f3(x):
    return 3     
## Which of the following does NOT cause an exception to be thrown?
# Ans: for i in range(1000001, -1, -2):
#          print(f)

# Problem 2-6
stuff  = "iQ"
for thing in stuff:
    if thing == 'iQ':
        print("Found it")  

#Answers: 
## ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
## ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
## ["iQ"]

# Problem 2-7
## The following Python code is supposed to compute the square of an integer by using successive additions.
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

Square(-9)

#Not considering recursion depth limitations, what is wrong with this implementation of procedure Square? Check all that apply.
# Answer: Nothing is wrong; the code is fine as-is.
    
# Problem 3
# Write a Python function, twoQuadratics, that takes in two sets of coefficients and x-values and prints the sum of the results of evaluating two quadratic equations. It does not do anything else. That is, you should evaluate and print the result of the following equation:
# You are given the following function, evalQuadratic
def evalQuadratic(a, b, c, x):
   '''
   a, b, c: numerical values for the coefficients of a quadratic equation
   x: numerical value at which to evaluate the quadratic.
   '''
   return a*x*x + b*x + c

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    return print(evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2))

a1 = 4.04
b1 = 3.07
c1 = 1.25
x1 = 8.29
a2 = -2.61
b2 = 0.39
c2 = -4.48
x2 = -2.4
twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2)

# Problem 4
## Implement a function that meets the specifications below.
def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    L.reverse()
    for i in L:
        i.reverse()
    print(L)

L = [1, 2, 3]
L.reverse()
L
L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L)

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L) 
print(L)

# Problem 5
## Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)
## This function takes in a dictionary and returns a list.
def rmUniqueVals(aDict):
    '''
    aDict: a dictionary
    '''
    a = {}
    for val in set(aDict.values()):
        if list(aDict.values()).count(val) == 1:
            a[val] = list(aDict.values()).count(val)
    return a
        

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    rmDuplicates = {}
    values = list(rmUniqueVals(aDict).keys())
    for i in aDict:
        if aDict[i] in values:
            rmDuplicates[i] = aDict[i]
    return sorted(rmDuplicates.keys())


aDict = {'amrit': 9, 'kenza': 7, 'loubna': 3}
uniqueValues(aDict)
dict = {2: 0, 3: 3, 6: 1}

a = rmUniqueVals(aDict)


dict = {5: 1, 7: 1}
uniqueValues(dict)

# Problem 6
# Write a recursive Python function, given a non-negative integer N, to calculate and return the sum of its digits.
# Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 10 removes the rightmost digit (126 // 10 is 12).
# This function has to be recursive; you may not use loops!
# This function takes in one integer and returns one integer.
def sumDigits(N):
    """
    N: non-negative integer
    """
    if N < 9:
        return N
    else:
        return (N % 10) + sumDigits(N//10)

sumDigits(0)
sumDigits(1)
sumDigits(11)
sumDigits(126)

# Problem 7
# Write a function called general_poly, that meets the specifications below. For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because .
# closure
def ff(x):
    x = x + 2
    def fff(y):
        return x + y
    return fff

ff(1)(2)

def general_poly0(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    L.sort()
    orgL = L[:]
    L[:] = [x - 1 for x in L]
    L.reverse()
    
    def mult_sum(base):
        """
        base: base integer
        """
        pwr = [base ** x for x in L]
        return sum([a*b for a,b in zip(orgL, pwr)])

    return mult_sum

def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def mult_sum(base):
        """
        base: base integer
        """
        add = 0
        for i in L:
            add = base*add + i
        return add

    return mult_sum

general_poly0([1, 2, 3, 4])(10)
general_poly([1, 2, 3, 4])(10)














