#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 11:57:56 2019

@author: asingh
"""

# vowel checker
s = 'azcbobobegghakl'
vowels = 0
for letter in s:
    if 'a' in letter or 'e' in letter or 'i' in letter or \
    'o' in letter or 'u' in letter:
            vowels += 1
print('Number of vowels: ', vowels)

# number of time bob occurs
s = 'bobobobobobobobobobobobob'
nBob = 0
index1=0
index2=3
while index2 <= len(s):
    if 'bob' in s[index1:index2]:
        nBob += 1
    index1 +=1
    index2 +=1
print('Number of times bob occurs is: ', nBob)

# longest substring of s
s = 'azcbobobegghakl'
i=0
while i < len(s)-1:
    substr = s[i]
    i +=1
    if s[i] > s[i-1]:
        substr += s[i]
    else:
        substr = s[i]
    print(substr)
    