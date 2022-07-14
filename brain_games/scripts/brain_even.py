#!/usr/bin/python -tt
from random import randint
from brain_games.cli import name_user, welcome_user



def brain_even():
    i = 1
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i <= 3:
        for _ in range(10):
	        value = randint(0, 10)

        print("Question: "+str(value))
        useranswer = input('Your answer: ')  

        if (value % 2) == 0:
            if useranswer == "yes":
                print("Correct!")
                i+=1
            else:
                print(f"Let's try again,!")
        else:
            if useranswer == "no":
                print("Correct!")
                i+=1
            else:                
                print(f"Let's try again,!")
    print(f"Congratulations, {name_user()}!")

brain_even()
