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




