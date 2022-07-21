#!/usr/bin/python -tt

import sys
from random import randint
import prompt


def random_number():
    for _ in range(3):
        expression_value = randint(0, 100)
    return expression_value


def IsPrime(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return 'no'
                break
        else:
            return 'yes'
    else:
        return 'no'


def brain_prime():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    # Start Function
    i = 1

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while i <= 3:

        r_number = random_number()
        number_is_prime = IsPrime(r_number)

        print(f'Question: {r_number} ')
        useranswer = str(input('Your answer: '))

        if number_is_prime == useranswer.lower():
            print("Correct!")
            i += 1
        else:
            sys.exit(f"{useranswer} is wrong answer ;(. Correct answer was {number_is_prime}.\n"
                     + f"Let's try again,{name}!")

    print(f"Congratulations, {name}!")


def main():
    brain_prime()


if __name__ == '__main__':
    main()
