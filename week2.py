#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:39:54 2019

@author: asingh
"""

# Guess the number

low = 0
high = 100
numGuesses = 0
guess = (low + high)//2

print("Please think of a number between 0 and 100!")

while guess < high:
    print('Is your secret number ', guess, '?')
    userinput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if userinput == 'h':
        high = guess
        guess = (low + high)//2
    elif userinput == 'l':
        low = guess
        guess = (low + high)//2
    elif userinput == 'c':
        print('Game over. Your secret number was: ', guess)
        break
    else:
        print('Sorry, I did not understand your input.')


# Convert integer into binary
num = 19

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result == '0'
while num > 0:
    print(num, num % 2, num // 2)
    result = str(num % 2) + result
    num = num//2
if isNeg:
    result = '-' + result
print(result)

# Convert decimal to binary

x = float(input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num // 2

for i in range(p - len(result)):
    result = '0' + result
    
result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))

# square a number
def square( num ):
    '''
    num: is an int or float
    output: num * num
    '''
    num * num

square(2)

# SCOPE
a = 10
def f(x):
    return x + a
a = 3
f(1)

## OBJECTTS
str2 = 'number one - the larch'
str2 = str2.capitalize() 
str2
str2.swapcase()

str1 = 'exterminate!'
str1.index('e')

str2.index('!')
str2.find('!')

# Exercise: iter power
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    ## when exp is 0
    if exp == 0:
        result = 1
    else:
    ## computation of base^exp
        while exp > 0:
            result = result * base
            exp -= 1
    return result

## Test cases:
iterPower(5.71, 0)
iterPower(-6.46, 5)
iterPower(-1.67, 2)
iterPower(-9.92, 10)

# Exercise: power recur

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)

recurPower(5.71, 0)
recurPower(-6.46, 5)

# Exercise: gcd iter
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    divisor = min(a, b)
    while divisor > 1:
        if (a % divisor == 0) and (b % divisor == 0):
            return divisor
        else:
            divisor -= 1
        if divisor == 1:
            return 1

gcdIter(2, 12)
gcdIter(6, 12)
gcdIter(9, 12)
gcdIter(17, 12)

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)

gcdRecur(2, 12)
gcdRecur(6, 12)
gcdRecur(9, 12)
gcdRecur(17, 12)

# Exercise: is in
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    ## What happens when the string is empty?
    ## What happens when the string is of length 1?
    if len(aStr) <= 1:
        return char == aStr
    ## What happens when the test character equals the middle character?
    mid = len(aStr)//2
    if char == aStr[mid]:
        return True
    if char < aStr[mid]:
        return isIn(char, aStr[:mid])
    else:
        return isIn(char, aStr[mid:])
    
isIn('q', 'bchkkmoqttuvv')






