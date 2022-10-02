#!/usr/bin/python -tt

from random import randint

RULES = 'What is the result of the expression?'


def generate_round():
    random_number_one = randint(1, 100)
    random_number_two = randint(1, 100)
    expression = ('+', '-', '*')
    random_expression = randint(0, 2)

    if expression[random_expression] == expression[0]:

        # Выражение сложение
        correct_answer = random_number_one + random_number_two
        question_expression = f"{random_number_one} + {random_number_two}"

    elif expression[random_expression] == expression[1]:

        # Выражение вычитание
        correct_answer = random_number_one - random_number_two
        question_expression = f"{random_number_one} - {random_number_two}"


    elif expression[random_expression] == expression[2]:

        # Выражение умножение
        correct_answer = random_number_one * random_number_two
        question_expression = f"{random_number_one} * {random_number_two}"

    else:
        print("Wrong expression")

    return question_expression, correct_answer
