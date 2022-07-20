#!/usr/bin/python -tt

import sys
from random import randint
import prompt


def random_number():
    for _ in range(3):
        expression_value = randint(1, 10)
    return expression_value

def random_number_secret():
    for _ in range(3):
        expression_secret = randint(0, 3)
    return expression_secret


def brain_progression():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")


    # Start Function
    i = 1

    print('What number is missing in the progression?')

    while i <= 3:
        number = random_number_secret()

        list_numbers = list(range(random_number(), 100, random_number()))
        short_list_numbers = list_numbers[:5]

        secret_number = short_list_numbers[number]
        short_list_numbers[number] = ".."

        print(f'Question: {short_list_numbers} ')
        useranswer = int(input('Your answer: '))

        if useranswer == secret_number:
            print("Correct!")
            i += 1
        else:
            sys.exit(f"{useranswer} is wrong answer ;(. Correct answer was {secret_number}.\n"
                     + f"Let's try again,{name}!")
    print(f"Congratulations, {name}!")


def main():
    brain_progression()


if __name__ == '__main__':
    main()




