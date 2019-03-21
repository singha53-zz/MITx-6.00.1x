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

# =============================================================================
# In the best case scenario, x is less than or equal to 0. We first 
# execute the assignment total = 0 for one step. Next we execute the for 
# i in range(1000) loop. This loop is executed 1000 times and has three 
# steps (one for the assignment of i each time through the loop, as well 
#        as two for the += operation) on each iteration. We next check if 
#        x > 0 - it is not so we do not enter the loop. Adding one more 
#        step for the return statement, in the best case we execute 
#        1 + 3*1000 + 1 + 1 = 3003 steps.
# 
# In the worst case scenario, x is a large positive number. In this case, 
# we first execute the assignment total = 0 for one step. Next we execute 
# the first loop 1000 times (3000 total steps), then we execute the second 
# loop (while x > 0) n times. This loop has five steps (one for the 
# conditional check, x > 0, and two each for the -= and += operations). 
# When we finally get to the point where x = 0, we execute the 
# conditional check x > 0 one last time - since it is not, we do not 
# enter the loop. Adding one more step for the return statement, in 
# the worst case we execute 1 + 3*1000 + 5*n + 1 + 1 = 5*n + 3003 steps.
# =============================================================================

# Program 2
def program2(x):
    total = 0
    for i in range(1000):
        total = i

    while x > 0:
        x = x//2
        total += x

    return total

# =============================================================================
# In the best case scenario, x is less than or equal to 0. We first 
# execute the assignment total = 0 for one step. Next we execute the 
# for i in range(1000) loop. This loop is executed 1000 times and has 
# two steps (one for the assignment of i each time through the loop, 
# as well as one for the = operation) on each iteration. 
# We next check if x > 0 - it is not so we do not enter the 
# loop. Adding in one step for the return statement, in the 
# best case we execute 1 + 2*1000 + 1 + 1 = 2003 steps.
# 
# In the worst case scenario, x is a large positive number. In this 
# case we first execute the assignment total = 0 for one step, then 
# we execute the first loop 1000 times (2000 total steps). Finally 
# execute the second loop (while x > 0) log2(n) + 1 times. This is 
# tricky! Because we divide x by 2 every time through the loop, we 
# only execute this loop a logarithmic number of times. log2(n) 
# divisions of x by 2 will get us to x = 1; we'll need one more 
# division to get x <= 0 . Don't worry if you couldn't get this 
# fact; we'll go through it a few more times in this unit.
# 
# This while loop has five steps (one for the conditional check, x > 0, 
# and two each for the //= and += operations). When we finally get to 
# the point where x = 0, we execute the conditional check x > 0 one 
# last time - since it is not, we do not enter the loop. Adding in 
# one step for the return statement, in the worst case we execute 
# 1 + 2*1000 + 5*(log2(n) + 1) + 1 + 1 = 5*log2(n) + 2008 steps.
# =============================================================================

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

# =============================================================================
# In the best case scenario, L is an empty list. Thus we execute only the 
# first two assignment statements, then the return statement. Therefore 
# in the best case we execute 3 steps. Note that since the list is empty, 
# no assignments are performed in the for x in L lines.
# 
# In the worst case scenario, L is a list with its elements sorted 
# in increasing order (eg, [1, 3, 5, 7, ...]). In this case we execute 
# the first two assignment statements (2 steps). Next we execute the 
# first loop n times. This first loop has three steps (one for the 
# assignment of x each time through the loop, as well as two for the 
# += operation), adding 3*n steps.
# 
# Finally we execute the second loop n times. The first time we 
# execute this loop, we perform 3 steps - one for the assignment of x; 
# then we run the check if highestFound == None, and finding it to be 
# True, we execute the assignment highestFound = x.
# 
# The next (n-1) times we execute this loop, we perform 4 steps: one 
# for the assignment of x, then we run the check if highestFound == None, 
# and finding it to be False, we run the check elif x > highestFound. 
# Since this is always True (the list is sorted in increasing order), 
# we execute the assignment highestFound = x. Therefore in the second 
# loop we execute 3 + (n-1)*4 = 3 + 4*n - 4 = 4*n - 1 steps.
# 
# Finally we execute the return statement, which is one more step.
# 
# Pulling this all together, we can see that in the worst case we 
# execute 2 + 3*n + 4*n - 1 + 1= 7*n + 2 steps.
# =============================================================================

# Exercise 3
def program11(L):
    multiples = []
    for x in L:
        for y in L:
            multiples.append(x*y)
    return multiples

# =============================================================================
# In the best case scenario, L is an empty list. So we execute only the 
# first assignment statement, then the return statement. Thus in the best 
# case we execute 2 steps. Note that since the list is empty, no 
# assignments are performed in the for x in L line.
# 
# In the worst case scenario, L is a long list. In this case we go 
# through the loop for x in L n times. Every time through this loop, 
# we execute an assignment of a value to x, and then the inner loop 
# for y in L. The assignment takes 1 step on each iteration; how many 
# steps does the inner loop take on each iteration?
# 
# The inner loop has three operations (assignment of a value to y, x*y, 
# and list appending). So the inner loop executes 3*n times on each 
# iteration of the outer loop. Thus the nested loop structure is executed 
# n * (3*n + 1) = 3*n**2 + n times!
# 
# Adding in two steps (for the first assignment statement, and the 
# return statement) we see that in the worst case, this program 
# executes 3*n**2 + n + 2 steps.
# =============================================================================

def program2(L):
    squares = []
    for x in L:
        for y in L:
            if x == y:
                squares.append(x*y)
    return squares

# =============================================================================
# In the best case scenario, L is an empty list. So we execute only the 
# first assignment statement, then the return statement. Thus in the best 
# case we execute 2 steps. Note that since the list is empty, no 
# assignments are performed in the for x in L line.
# 
# In the worst case scenario, L is a long list of one repeated number 
# (ie [2, 2, 2, 2, ...]. In this case we go through the loop for x in 
#  L n times. Every time through this loop, we perform one assigment 
#  of a value to the variable x, then we execute the inner loop for y 
#  in L n times.
# 
# The inner loop performs one assigment of a value to the variable y. 
# It then has one operation that is checked every time (if x == y). 
# Since the WORST case is when the list is composed of identical elements, 
# this check is always true - so the third and fourth operations (x*y, and 
# list appending) are always performed. So the inner loop executes 4*n 
# times on each iteration of the outer loop. Thus the nested loop 
# structure is executed n * (4*n + 1) = 4*n**2 + n times!
# 
# Adding in two steps (for the first assignment statement, and the 
# return statement) we see that in the worst case, this program executes 
# 4*n**2 + n + 2 steps.
# =============================================================================

def program3(L1, L2):
    intersection = []
    for elt in L1:
        if elt in L2:
            intersection.append(elt)
    return intersection

# =============================================================================
# In the best case scenario, L1 is an empty list. So we execute only the 
# first assignment statement, then the return statement. Thus in the best 
# case we execute 2 steps.
# 
# In the worst case scenario, every element of L1 is the same as the very 
# last element of L2. In this case we go through the loop for elt in L1 
# n times. Every time through this loop, we perform one assigment of a 
# value to the variable elt, then	we execute the check if elt in L2.
# 
# How long does it take to execute this check? Well in the worst case, 
# elt is the very LAST element of L2. In order to check if elt in L2, 
# Python iterates over the elements of L2 until it either finds the one 
# you're looking for, or L2 runs out of elements. Thus in the worst case, 
# the check if elt in L2 takes n steps. After this, we perform one append 
# operation. So the conditional plus the append takes n + 1 steps on each 
# iteration of the loop. Thus the for loop takes n * (n + 2) = n**2 + 2*n 
# steps!
# 
# Adding in two steps (for the first assignment statement, and the return 
# statement) we see that in the worst case, this program executes 
# n**2 + 2*n + 2 steps
# =============================================================================

# Exercise 4
## Determine the complexity of the following tasks.

# =============================================================================
# 6.00.1x staff decide to hold an online chess tournament, and n 6.00.1x 
# students respond to participate in it. If the tournament is a 
# single-elimination tournament (this means you are eliminated when 
# you lose once), how many games do we need to decide the winner, in 
# terms of n? Assume there will be no draws or byes.
# =============================================================================
O(n)

# =============================================================================
# You are asked to write an n page research paper. You've written plenty 
# of research papers in your time, and you know it always takes you 
# 30 minutes to write one page of a research paper. In terms of n, what 
# is the complexity order that describes the amount of time this 
# research paper will take to write?
# =============================================================================
O(n) 

# =============================================================================
# You are asked to write an n page personal essay. You've written plenty of 
# personal essays in your time, and you know it always takes you two hours 
# to write a personal essay, no matter the length. In terms of n, what is 
# the complexity order that describes the amount of time this personal essay 
# will take to write?
# =============================================================================
O(1)

# =============================================================================
# You just dropped a box of glass toys and n toys in the box broke in half. 
# You'd like to match the halves of the toys so that you could glue them 
# together, but the only way to tell whether two halves belonged to one 
# toy is to physically pick up the two pieces and try to fit them together. 
# Express how long this matching process will take in terms of n.
# 
# =============================================================================
O(n)

# Exercise 6
## Consider the following Python procedures. For each one, specify its 
## order of growth.

# Assume n has been previously bound to some value
# =============================================================================
# i = 0
# while i < 5:
#    n *= 2
#    i += 1
# 
# print(n)
# =============================================================================
O(1) ## since n is bounded

# =============================================================================
# def iterPower(a, b):
#    result = 1
#    while b > 0:
#       result *= a
#       b -= 1
#    return result
# =============================================================================
O(b)

# =============================================================================
# def recurPower(a, b):
#    print(a, b)
#    if b == 0:
#       return 1
#    else:
#       return a * recurPower(a, b-1)
# =============================================================================
O(b)

# =============================================================================
# def recurPowerNew(a, b):
#    print(a, b)
#    if b == 0:
#       return 1
#    elif b%2 == 0:
#       return recurPowerNew(a*a, b/2)
#    else:
#       return a * recurPowerNew(a, b-1)
# =============================================================================
O(logb)

# Exercise 7
## Consider the following Python procedures. For each one, 
## specify its order of growth.

def lenRecur(s):
   if s == '':
      return 0
   else:
      return 1 + lenRecur(s[1:])
# O(len(s))

def isIn(a, s):
   '''
   a is a character, or, singleton string.
   s is a string, sorted in alphabetical order.
   '''
   if len(s) == 0:
      return False
   elif len(s) == 1:
      return a == s
   else:
      test = s[len(s)//2]
      if test == a:
         return True
      elif a < test:
         return isIn(a, s[:len(s)//2])
      else:
         return isIn(a, s[len(s)//2+1:])
# O(log(len(s)))

def union(L1, L2):
   '''
   L1 & L2 are lists of the same length, n
   '''
   temp = L1[:]
   for e2 in L2:
      flag = False
      for check in temp:
         if e2 == check:
            flag = True
            break
      if not flag:
         temp.append(e2)
   return temp
# n^2

def unionNew(L1, L2):
   '''
   L1 & L2 are lists of the same length, n
   '''
   temp = []
   for e1 in L1:
      flag = False
      for e2 in L2:
         if e1 == e2:
            flag = True
            break
      if not flag:
         temp.append(e1)
   return temp + L2
# n^2

# Searching and Sorting Algorithms
## Exercise 1
# =============================================================================
# In computer programming, indirection (also called "dereferencing") 
# is the ability to reference something using a name, reference, 
# or container instead of the value itself. The most common form 
# of indirection is the act of manipulating a value through its 
# memory address.
# =============================================================================
a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]

# =============================================================================
# What is the value of the following expressions? 
# If you think there will be an error, please type in 'error' 
# (without quotes) in the input box.
# =============================================================================
a[0] ## 1
b[1] ## 0
a[a[1]] ## 3
b[b[2]] ## 2
a[b[2]] ## 3
c[a[b[3]]] ## 3
a[c[a[b[0]]]] ## error
a[c[a[b[3]]]] ## 4

def foo(L):
    val = L[0]
    while (True):
        val = L[val]
# Which of the following statement(s) will result in an infinite loop?
## val changes depending on L[val];
## foo(a) and foo(b) keep going whereas foo(c) results in an error

num = ???
L = [5, 0, 2, 4, 6, 3, 1]
val = 0
for i in range(0, num):
    val = L[L[val]]

print(val)
# What is the smallest value that num can be such that the number 3 is printed?
# value of val is being changed inside a for loop
# L[0] = 5
## L[5] = 5
# num should be 0

L = [2, 0, 1, 5, 3, 4]
# same as above

# Exercise 2
## assuming L is sorted:
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

## alternative version of search
def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False

## do the same thing
   
# Exercise 3
def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False
## do the same thing
    
# Exercise 4
def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)
# search and search3 return the same answers provided 
# L is non-empty and e is in L.

# Exercise 5
## Here is the code for selection sort. For simplicity, assume L is a list of integers:
def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
            
def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1

L = [23, 0, 74, 652, 3]
selSort(L); L
L = [23, 0, 74, 652, 3]
newSort(L); L

## Do these two functions result in the same sorted lists? Yes
## Do these two functions execute the same number of assignments of 
## values into entries of the lists?
## No. newSort may use more - but never fewer - inserts than selSort. 
## Is the worst-case order of growth of these functions the same?
## Yes. newSort and selSort have the same complexity.

# Exercise 6
def mySort(L):
    """ L, list with unique elements """
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

def newSort(L):
    """ L, list with unique elements """
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1

L = [23, 0, 74, 652, 3]
mySort(L); L
L = [23, 0, 74, 652, 3]
newSort(L); L

## Do these two functions result in the same sorted lists? Yes
## Do these two functions execute the same number of assignments of 
## values into entries of the lists?
## Yes. They execute the same number of assignments.
## Is the worst-case order of growth of these functions the same?
## Yes. newSort and mySort have the same complexity.
## Do these two functions examine the same number of entries in the list?
## No. mySort and newSort examine different numbers of entries, but 
## one cannot always say which function will examine the most entries. 

# Exercise 7
## L is a list with n items
## Application A: Every time it's asked to, it performs a linear search 
##                through list L to find whether it contains x.
## Application B: Sort list L once before doing anything else 
##                (using mergeSort). Whenever it's asked to find x in L, 
##                it performs a binary search on L.

## 1. If the application is asked to find x in L exactly one time, 
## what is the worst case time complexity for Application A?
## O(n)
## 2. If the application is asked to find x in L exactly one time, 
## what is the worst case time complexity for Application B?
## mergesort + binary ~ O(nlogn) + O(logn) ~ O(nlogn)
## 3. If the application is asked to find x in L k times, what is the worst 
## case time complexity for Application A?
## O(kn)
## 4. If the application is asked to find x in L k times, what is the 
## worst case time complexity for Application B?
## mergesort + k*binary ~ O(nlogn) + k*O(logn)
## 5. What value(s) of k would make Application A be faster 
## (i.e., asymptotically grow slower than) Application B?
## O(nlogn) + k*O(logn) < k*O(n) ; k = 1
## When k = 1, Application A's complexity is O(kn)=O(n), 
## and Application B's complexity is O(nlogn + klogn) = O(nlogn + logn).
## Setting k at any value greater than 1 makes O(kn) asymptotically grow 
## faster than O(nlogn + klogn).
## What value(s) of k would make Application A grow at the same rate 
## as Application B?
## O(nlogn) + k*O(logn) < k*O(n) ; k = logn
## When k=logn, Application A's complexity is O(kn)=O(nlogn), 
## and Application B's complexity is O(nlogn + klogn) = O(nlogn + lognlogn).
## lognlogn  grows slower than nlogn, so in this case Application B's time 
## complexity is O(nlogn). So, when , the order of time complexity of 
## Applications A and B are equal.
## Which application should you choose if you know that there are going 
## to be requests to find x in L?
## for many searches sorting first wins! Application B (amortization cost)












