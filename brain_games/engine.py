#!/usr/bin/python -tt

import prompt
import sys

def welcome_user(name_game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    if name_game == "brain_calc":
        print("'What is the result of the expression?'")
    elif name_game == "brain_even":
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif name_game == "brain_gcd":
        print('Find the greatest common divisor of given numbers.')
    elif name_game == "brain_prime":
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    elif name_game == "brain_progression":
        print('What number is missing in the progression?')


    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def user_lose(useranswer, answer, name):
    return sys.exit(f"{useranswer} is wrong answer ;(. Correct answer was {answer}.\n"
                    + f"Let's try again,{name}!")