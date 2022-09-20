#!/usr/bin/python -tt

from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even():
    for _ in range(10):
        value = randint(0, 10)
    return value


def is_even(number):
    if (number % 2) == 0:
        return "yes"
    else:
        return "no"

# def brain_even():
#     i = 1
#     while i <= 3:
#         for _ in range(10):
#             value = randint(0, 10)
#
#         print("Question: " + str(value))
#         useranswer = input('Your answer: ')
#
#         if (value % 2) == 0:
#             if useranswer == "yes":
#                 print("Correct!")
#                 i += 1
#             else:
#                 answer = "yes"
#                 user_lose(useranswer, answer, name)
#         else:
#             if useranswer == "no":
#                 print("Correct!")
#                 i += 1
#             else:
#                 answer = "no"
#                 user_lose(useranswer, answer, name)
#     print(f"Congratulations, {name}!")
