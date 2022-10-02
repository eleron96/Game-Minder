#!/usr/bin/python -tt

import prompt
import sys


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def run(game):
    name = welcome_user()
    print(game.RULES)

    for _ in range(3):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.\n"
                  + f"Let's try again,{name}!")
            break

    print(f"Congratulations, {name}!")



# def ask_name():
#     name = prompt.string('May I have your name? ')
#     return name
#
#
# def welcome_user_by_name(ask_name):
#     print(f"Hello, {ask_name}!")


# def game_rules(name_game):
#     # if name_game == "brain_calc":
#     #     print("'What is the result of the expression?'")
#     # elif name_game == "brain_even":
#     #     print('Answer "yes" if the number is even, otherwise answer "no".')
#     # elif name_game == "brain_gcd":
#     #     print('Find the greatest common divisor of given numbers.')
#     # elif name_game == "brain_prime":
#     #     print('Answer "yes" if given number is prime. Otherwise answer "no".')
#     # elif name_game == "brain_progression":
#     #     print('What number is missing in the progression?')
#     return


# i = 1
# while i <= 3:
#     game_answer = brain_even()
#     print("Question: " + str(game_answer))
#     is_number_even = is_even(game_answer)
#     is_user_right = user_answer()
#     if is_number_even == is_user_right:
#         print("Correct!")
#         i += 1
#     else:
#         user_lose(is_user_right, is_number_even, name)


# def question_for_user(game_answer):
#     print("Question: " + str(game_answer))
#
#
# def user_answer():
#     useranswer = input('Your answer: ')
#     return useranswer
#
#
# def user_lose(useranswer, answer, name):
#     return sys.exit(f"{useranswer} is wrong answer ;(. Correct answer was {answer}.\n"
#                     + f"Let's try again,{name}!")
