import prompt
import sys


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Find the greatest common divisor of given numbers.')
    return name


def user_lose(useranswer, answer, name):
    return sys.exit(f"{useranswer} is wrong answer ;(. Correct answer was {answer}.\n"
                    + f"Let's try again,{name}!")