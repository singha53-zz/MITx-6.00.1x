#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:28:59 2019

@author: asingh
"""

# Object oriented programming

# Exercise 2

class Clock(object):
    def __init__(self, time):
	    self.time = time
    def print_time(self):
	    time = '6:30'
	    print(self.time)

clock = Clock('5:30')
clock.print_time()   
## answer is 5:30 with no quotes (dont put quotes for any answer)

# Exercise 3
class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

w1 = Weird(X, Y)
print(w1.getX())  # NoneType, error
print(w1.getY())  # NoneType, error
w2 = Wild(X, Y)
print(w2.getX()) # int, 7
print(w2.getY()) # int, 8
w3 = Wild(17, 18)
print(w3.getX()) # int, 17
print(w3.getY()) # int, 18
w4 = Wild(X, 18) 
print(w4.getX()) # int, 7
print(w4.getY()) # int, 18
X = w4.getX() + w3.getX() + w2.getX()
print(X) # int, 31
print(w4.getX()) # int, 7
Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print(Y) # int, 44
print(w2.getY()) # int, 8

# Exercise: coordinate
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return 'Coordinate(' + str(self.x) + ',' + str(self.y) + ')' 

c = Coordinate(2,-8)
b = Coordinate(2,-8)
print(c)
eval(repr(c))
c == b

# Exercise: int set
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        """Return a new intSet containing the common elements"""
        self.com = []
        for e in self.vals:
            if e in other.vals:
                self.com.append(e)
        return '{' + ','.join([str(i) for i in self.com]) + '}' 
        
    def __len__(self):
        return len(self.vals)

e = intSet()
e.insert(1)
e.insert(2)
e.insert(3)
print(e)
len(e)
f = intSet()
f.insert(4)
f.insert(2)
f.insert(1)
e.intersect(f)

# Exercise: spell

class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
        
    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'

print(Accio())

# Exercise 4
class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")

obj = D()
print(obj.a)










