from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    random_number = randint(0, 100)
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return random_number, str(correct_answer)


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True
