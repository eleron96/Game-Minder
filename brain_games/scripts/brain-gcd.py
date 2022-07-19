#!/usr/bin/python -tt

import sys
from random import randint
import prompt

def random_number():
    for _ in range(3):
        expression_value = randint(0, 1000)
    return expression_value

def brain_gcd():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    # Start Function
    i = 1

    print('Find the greatest common divisor of given numbers.')

    while i <= 3:
        answer = 0

        a = random_number()
        b = random_number()

        print(f'Question: {a} + {b} ')

        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        answer = a + b

        useranswer = int(input('Your answer: '))

        if useranswer == answer:
            print("Correct!")
            i += 1
        else:
            sys.exit(f"{useranswer} is wrong answer ;(. Correct answer was {answer}.\n"
                     + f"Let's try again,{name}!")

    print(f"Congratulations, {name}!")


def main():
    brain_gcd()


if __name__ == '__main__':
    main()