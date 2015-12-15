__author__ = 'joe'
# -*- coding: utf-8 -*-

print('Please think of a number between 0 and 100!')
low = 0
high = 100
correct = False
while not correct:
    guess = (low + high)/2
    print('Is your secret number '+str(guess)+'?')
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if user_input == 'c':
        correct = True
    elif user_input == 'h':
        high = guess
    elif user_input == 'l':
        low = guess
    else:
        print("sorry, i do not understand what do you mean")

print("game over! The number you guess is "+str(guess))