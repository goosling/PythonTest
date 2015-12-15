__author__ = 'joe'
# -*- coding: utf-8 -*-

x = 12345
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (low + high)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low ='+str(low)+' high='+str(high)+' ans='+str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (low + high)/2.0
print('num of guesses'+str(numGuesses))
print(str(ans)+ ' is nearly the root of '+ str(x))