#!/usr/bin/python -tt

import prompt
import sys


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def run(game):
    name = welcome_user()
    print(game.RULES)

    for _ in range(3):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if str(user_answer) == str(correct_answer):
            print('Correct!')
        else:
            if user_answer == "yes" or user_answer == "no":
                return sys.exit(f'"{str(user_answer)}" is wrong answer ;(. Correct answer was "{str(correct_answer)}".\n'
                                + f"Let's try again,{name}!")
            else:
                return sys.exit(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\n"
                                + f"Let's try again,{name}!")



    print(f"Congratulations, {name}!")
