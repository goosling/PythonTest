__author__ = 'joe'
# -*- coding: utf-8 -*-

x = 25
epsilon = 1
step = epsilon**2
numGuess = 0
ans = 0.0
while(abs(ans**2-x)) >= epsilon and ans <= x:
    ans += step
    numGuess += 1
    print('numGuesses = '+str(numGuess))
    if abs(ans**2-x) >= epsilon:
        print("Failed on square root of "+ str(x))
    else:
        print(str(ans)+' is close to the square root of '+str(x))