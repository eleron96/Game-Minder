import prompt
import sys


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return name


def user_lose(useranswer, number_is_prime, name):
    return sys.exit(f"{useranswer} is wrong answer ;(. Correct answer was {number_is_prime}.\n"
                    + f"Let's try again,{name}!")


def IsPrime(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return 'no'
                break
        else:
            return 'yes'
    else:
        return 'no'