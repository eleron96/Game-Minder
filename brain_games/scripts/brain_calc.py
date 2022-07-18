#!/usr/bin/python -tt

import sys
from random import randint
import prompt

def random_number():
    for _ in range(3):
        expression_value = randint(0, 100)
    return expression_value

def brain_calc():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    # Start Function

    i=1

    expression = ('+', '-', '*')

    print('What is the result of the expression?')

    while i <= 3:
        x = randint(0, 3)
        number_1 = random_number()
        number_2 = random_number()

        if expression[x] == expression[0]:

            #Выражение сложение

            answer = number_1 + number_2
            print(f'Question: {number_1} + {number_2} ')
            useranswer = int(input('Your answer: '))

            if useranswer == answer:
                print("Correct!")
                i += 1
            else:
                sys.exit(f"{useranswer} is wrong answer ;(. Correct answer was {answer}.\n"
                         + f"Let's try again,{name}!")

        elif expression[x] == expression[1]:

            #Выражение вычитание

            answer = number_1 - number_2
            print(f'Question: {number_1} - {number_2} ')
            useranswer = int(input('Your answer: '))
            print(answer)
            if useranswer == answer:
                print("Correct!")
                i += 1
            else:
                sys.exit(f"{useranswer} is wrong answer ;(. Correct answer was {answer}.\n"
                         + f"Let's try again,{name}!")

        elif expression[x] == expression[2]:

            #Выражение умножение

            answer = number_1 * number_2
            print(f'Question: {number_1} * {number_2} ')
            useranswer = int(input('Your answer: '))
            print(answer)
            if useranswer == answer:
                print("Correct!")
                i += 1
            else:
                sys.exit(f"{useranswer} is wrong answer ;(. Correct answer was {answer}.\n"
                         + f"Let's try again,{name}!")

    print(f"Congratulations, {name}!")







def main():
    brain_calc()


if __name__ == '__main__':
    main()