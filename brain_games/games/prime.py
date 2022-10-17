from random import randint
from math import sqrt

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    random_number = randint(0, 100)
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return str(random_number), str(correct_answer)


def is_prime(n):

    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i) == 0:
                return False
        return True
