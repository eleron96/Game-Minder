import random
from random import randint

RULES = 'What is the result of the expression?'


def generate_round():
    random_number_one = randint(1, 100)
    random_number_two = randint(1, 100)
    expression = ["+", "-", "*"]
    operator = random.choice(expression)

    if operator == '+':
        correct_answer = random_number_one + random_number_two
        question_expression = f"{random_number_one} + {random_number_two}"
    elif operator == '-':
        correct_answer = random_number_one - random_number_two
        question_expression = f"{random_number_one} - {random_number_two}"
    elif operator == '*':
        correct_answer = random_number_one * random_number_two
        question_expression = f"{random_number_one} * {random_number_two}"

    return question_expression, str(correct_answer)
