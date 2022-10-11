from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def generate_round():
    random_number_one = randint(0, 1000)
    random_number_two = randint(0, 1000)

    random_number = f'{random_number_one} {random_number_two} '

    correct_answer = str(gcd_finder(random_number_one, random_number_two))

    return random_number, correct_answer


def gcd_finder(number_one, number_two):
    while number_one != 0 and number_two != 0:
        if number_one > number_two:
            number_one = number_one % number_two
        else:
            number_two = number_two % number_one

    return number_one + number_two
