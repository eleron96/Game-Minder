#!/usr/bin/python -tt

from random import randint
from brain_games.engine import welcome_user, user_lose

name = welcome_user("brain_calc")

def brain_calc():

    # Start Function
    i = 1

    expression = ('+', '-', '*')

    while i <= 3:
        x = randint(0, 2)
        number_1 = randint(0, 100)
        number_2 = randint(0, 100)

        if expression[x] == expression[0]:

            # Выражение сложение

            answer = number_1 + number_2
            print(f'Question: {number_1} + {number_2} ')
            useranswer = int(input('Your answer: '))

            if useranswer == answer:
                print("Correct!")
                i += 1
            else:
                user_lose(useranswer, answer, name)

        elif expression[x] == expression[1]:

            # Выражение вычитание

            answer = number_1 - number_2
            print(f'Question: {number_1} - {number_2} ')
            useranswer = int(input('Your answer: '))
            if useranswer == answer:
                print("Correct!")
                i += 1
            else:
                user_lose(useranswer, answer, name)

        elif expression[x] == expression[2]:

            # Выражение умножение

            answer = number_1 * number_2
            print(f'Question: {number_1} * {number_2} ')
            useranswer = int(input('Your answer: '))
            print(answer)
            if useranswer == answer:
                print("Correct!")
                i += 1
            else:
                user_lose(useranswer, answer, name)

    print(f"Congratulations, {name}!")