#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:32:07 2019

@author: asingh
"""

def balanceAfterOneyear( balance, annualInterestRate, monthlyPaymentRate):
    """
        balance: monthly balance, int or float
        annualInterestRate: yearly interest rate, float
        monthlyPaymentRate: minimum payment rate, float
    """
    monthlyInterestRate = annualInterestRate/12
    print('Month 1 Remaining balance: ' + str(round(balance, 2)))
    
    for i in range(1,13,1):
        minimumMonthlyPayment = monthlyPaymentRate * balance
        balance = balance - minimumMonthlyPayment
        balance = balance + monthlyInterestRate * balance
        print('Month ' + str(i) + ' Remaining balance: ' + str(round(balance, 2)))
    return print('Remaining balance: ' + str(round(balance, 2)))

## Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
balanceAfterOneyear( balance, annualInterestRate, monthlyPaymentRate)

## Test Case 2:
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
balanceAfterOneyear( balance, annualInterestRate, monthlyPaymentRate)

# Problem 2 - Paying Debt Off in a Year
def endBalance(balance, monthlyInterestRate, monthlyPayment):
    """
        balance: unpaid montly balance, int or float
        monthlyInterestRate: monthly interest rate
        monthlyPayment: montly payment
    """
    for i in range(0,12):
        balance = (balance-monthlyPayment)+monthlyInterestRate*(balance-monthlyPayment)
    return balance

def fixedPayment(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate/12
    remainingBalance = balance
    payment = 0
    while remainingBalance > 0:
        remainingBalance = endBalance(balance, monthlyInterestRate, monthlyPayment = payment)
        if remainingBalance > 0:
            payment += 10
        elif remainingBalance <= 0:
            break
            
        print('Lowest Payment: ' + str(payment))
    return payment
    

## Test Case 1:
fixedPayment(balance = 3329, annualInterestRate = 0.2)
## Test Case 2:
fixedPayment(balance = 4773, annualInterestRate = 0.2)
## Test Case 3:
fixedPayment(balance = 3926, annualInterestRate = 0.2)

# Problem 3 - Using Bisection Search to Make the Program Faster

def fixedPayment_BS(balance, annualInterestRate):
    remainingBalance = balance
    monthlyInterestRate = annualInterestRate/12
    low = balance/12
    upper = (balance * (1 + monthlyInterestRate)**12) / 12.0
    epsilon = 0.01
    
    while abs(remainingBalance) > epsilon:
        payment = (low+upper)/2
        remainingBalance = endBalance(balance, monthlyInterestRate, monthlyPayment = payment)
        if remainingBalance > epsilon:
            low = payment
        elif remainingBalance < -epsilon:
            upper = payment
        else:
            break
    return print('Lowest Payment: ', round(payment, 2))

## Test Case 1:
fixedPayment_BS(balance = 320000, annualInterestRate = 0.2)
## Test Case 2:
fixedPayment(balance = 999999, annualInterestRate = 0.18)
