#!/usr/bin/python -tt

from random import randint
from engine.prime_engine import welcome_user, user_lose, IsPrime


def brain_prime():
    name = welcome_user()
    i = 1

    while i <= 3:

        r_number = randint(0, 100)
        number_is_prime = IsPrime(r_number)

        print(f'Question: {r_number} ')
        useranswer = str(input('Your answer: '))

        if number_is_prime == useranswer.lower():
            print("Correct!")
            i += 1
        else:
            user_lose(useranswer, number_is_prime, name)

    print(f"Congratulations, {name}!")


def main():
    brain_prime()


if __name__ == '__main__':
    main()
