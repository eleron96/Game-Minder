#!/usr/bin/python -tt

from random import randint
from engine.gcd_engine import welcome_user, user_lose



def brain_gcd():
    name = welcome_user()

    # Start Function
    i = 1

    while i <= 3:
        answer = 0

        a = expression_value = randint(0, 1000)
        b = expression_value = randint(0, 1000)

        print(f'Question: {a} and {b} ')

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
            user_lose(useranswer, answer, name)

    print(f"Congratulations, {name}!")


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
