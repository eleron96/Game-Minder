#!/usr/bin/python -tt
from random import randint
from engine.even_engine import welcome_user, user_lose


def brain_even():
    name = welcome_user()

    i = 1
    while i <= 3:
        for _ in range(10):
            value = randint(0, 10)

        print("Question: " + str(value))
        useranswer = input('Your answer: ')

        if (value % 2) == 0:
            if useranswer == "yes":
                print("Correct!")
                i += 1
            else:
                answer = "yes"
                user_lose(useranswer, answer, name)
        else:
            if useranswer == "no":
                print("Correct!")
                i += 1
            else:
                answer = "no"
                user_lose(useranswer, answer, name)
    print(f"Congratulations, {name}!")


def main():
    brain_even()


if __name__ == '__main__':
    main()
