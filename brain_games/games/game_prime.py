from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    random_number = randint(0, 100)
    correct_answer = ''
    if random_number > 1:
        for i in range(2, int(random_number / 2) + 1):
            if (random_number % i) == 0:
                correct_answer = 'no'
                break
        else:
            correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return random_number, correct_answer
