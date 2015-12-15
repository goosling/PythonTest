__author__ = 'joe'
# -*- coding: utf-8 -*-

epsilon = 0.01
y = 24.0
guess = y/2
while abs(guess*guess-y) >= epsilon:
    guess = guess - (((guess**2) - y) / (2*guess))
    print(guess)
a = 'string'
print(a.upper)