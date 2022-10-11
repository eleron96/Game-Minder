from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    random_number = randint(0, 100)
    correct_answer = 'yes' if is_prime(random_number) == True else 'no'
    return random_number, str(correct_answer)


def is_prime(number):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                return False
            return True
        return False
