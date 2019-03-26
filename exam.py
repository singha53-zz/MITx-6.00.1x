#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:20:44 2019

@author: asingh
"""

# =============================================================================
# Exam
# =============================================================================

# Problem 1-1
## In the statement L = [1,2,3], L is a class.
## False; L is an instance of a list class

# Problem 1-2
## The orders of growth of  and  are both polynomial.
##  True: polynomial is n^c where c is a scalar

# Problem 1-3
## The complexity of binary search on a sorted list of n items is .
## True: O(logn) complexity refers to worst case

# Problem 1-4
## A bisection search algorithm always returns the correct answer when 
## searching for an element in a sorted list.

# Problem 1-4
## A bisection search algorithm always returns the correct answer when 
## searching for an element in a sorted list.
## True if list is sorted

# Problem 1-5
## Performing binary search on an unsorted list will always return
## the correct answer in O(n) time where n is the length of the list.
## False because the bounds are meaningless

# Problem 2-1
## You have the following class hierarchy:
class A(object):
    def foo(self):
        print('hi')
class B(A):
    def foo(self):
        print('bye')

## Ans: a is an instance of A, whereas B but not b is a subclass of A

# Problem 2-2
## Consider the function f below. What is its Big O complexity?        
def f(n):
    def g(m):
        print('m='+str(m))
        m = 0
        print('m='+str(m))
        print(list(range(m)))
        for i in range(m):
            print('i='+i)
            print('m='+str(m))
    for i in range(n):
        print('i='+str(i))
        g(n)
f(13)
# Ans: 1 + len(n) + 1 + 1 -> O(n)
## only the for loop for range(n) runs, not range(m)

# Problem 2-3
## A dictionary is an immutable object because its keys are immutable.
## False because a dictionary is mutable

# Problem 2-4
## Consider the following two functions and select the correct choice below:
def foo_one(n):
    """ Assume n is an int >= 0 """
    answer = 1.0
    while n > 1:
        answer *= n
        n -= 1
    return answer

def foo_two(n):
    """ Assume n is an int >= 0 """
    if n <= 1: 
        return 1.0
    else: 
        return n*foo_two(n-1)

## Ans: the complexity of foo_one is O(n) whereas
##      the complexity of foo_two is O(n)

# Problem 2-5
## The complexity of  1^n + n^4 + 4n + 4 is
## Ans:  1^n where n->inf is 1: therefore the complexity if n^c (polynomial)

# Problem 3
# =============================================================================
# Numbers in Mandarin follow 3 simple rules.
# 
# There are words for each of the digits from 0 to 10.
# For numbers 11-19, the number is pronounced as "ten digit", so for
#  example, 16 would be pronounced (using Mandarin) as "ten six".
# For numbers between 20 and 99, the number is pronounced as 
# “digit ten digit”, so for example, 37 would be pronounced 
# (using Mandarin) as "three ten seven". If the digit is a zero, it is 
# not included.
# Here is a simple Python dictionary that captures the 
# numbers between 0 and 10.
# =============================================================================

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

# =============================================================================
# We want to write a procedure that converts an American number 
# (between 0 and 99), written as a string, into the equivalent Mandarin.
# =============================================================================
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    num = int(us_num);
    if num <= 10:
        return trans[us_num]
    elif num <= 19:
        return 'shi ' + trans[us_num[1]]
    else:
        if us_num[1] == '0':
            return trans[us_num[0]] + ' shi'
        else:
            return trans[us_num[0]] + ' shi ' + trans[us_num[1]]
        
convert_to_mandarin('0')
convert_to_mandarin('10')
convert_to_mandarin('11')
convert_to_mandarin('19')
convert_to_mandarin('20')
convert_to_mandarin('99')

# Problem 4
# =============================================================================
# Write a Python function that creates and returns a list of prime numbers
#  between 2 and N, inclusive, sorted in increasing order. A prime number
#  is a number that is divisible only by 1 and itself. This function takes
#  in an integer and returns a list of integers.
# =============================================================================
def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    # functin to check if a number if prime
    def is_prime(n):
        if n == 2:
            return True
        number = n
        while n > 2:
            if number % (n-1) == 0:
                return False
            n -= 1
        return True
    # base case
    if N == 2:
        return [2]
    
    # for N > 2
    L = [2];
    while N > 2:
        if is_prime(N):
            L.append(N)
        N -= 1
    return sorted(L)

primes_list(2)
primes_list(3)
primes_list(5)
primes_list(10)

#Problem 5
# =============================================================================
# Implement a function that meets the specifications below.
# cipher("abcd", "dcba", "dab") returns (order of entries in dictionary
# may not be the same) ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc') 
# =============================================================================
def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    ## create mapping dictionary
    dict = {};
    for i in range(len(map_from)):
        dict[map_from[i]] = map_to[i]
    ## decoded msg
    msg=''
    for i in code:
        msg += dict[i]
        
    return (dict, msg)


cipher("abcd", "dcba", "dab")

# Problem 6
## Consider the following hierarchy of classes:
class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: ' + 'It is obvious that ' + Person.say(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self, stuff)

# =============================================================================
# As written, this code leads to an infinite loop when using the 
# Arrogant Professor class.
# Change the definition of ArrogantProfessor so that the following 
# behavior is achieved:
# =============================================================================


e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

e.say('the sky is blue')
## eric says: the sky is blue

le.say('the sky is blue')
## eric says: the sky is blue

le.lecture('the sky is blue')
## I believe that eric says: the sky is blue

pe.say('the sky is blue')
## eric says: I believe that eric says: the sky is blue

pe.lecture('the sky is blue')
## I believe that eric says: the sky is blue

ae.say('the sky is blue')
##eric says: It is obvious that eric says: the sky is blue

ae.lecture('the sky is blue')
## It is obvious that eric says: the sky is blue

# Problem 7
## You are given the following two classes.
### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)

# Implement a class that meets the specifications below.
class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        self.center_loc = center_loc
        self.tent_loc = [tent_loc]
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        for i in range(len(self.tent_loc)):
            if self.tent_loc[i].dist_from(new_tent_loc) < 0.5:
                return False
        self.tent_loc.append(new_tent_loc)
        return True
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        self.tent_loc.remove(tent_loc)
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        return sorted([i.__str__() for i in self.tent_loc])

c = MITCampus(Location(1,2))
c.add_tent(Location(2,3))
c.add_tent(Location(1,2))
c.add_tent(Location(0,0))
c.add_tent(Location(2,3))
c.get_tents()

c = MITCampus(Location(1,2), Location(0,0))
c.remove_tent(Location(1,1))

c = MITCampus(Location(1,2), Location(0,1))
c.add_tent(Location(-1,2))
c.add_tent(Location(1,-10))
c.add_tent(Location(1,10))
c.add_tent(Location(1,20))
c.add_tent(Location(1,40))
c.get_tents()
print(sorted(c.get_tents()))
print(check_if_x_sorted(c.get_tents()))






