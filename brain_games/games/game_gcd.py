from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def generate_round():

    random_number_one = randint(0, 1000)
    random_number_two = randint(0, 1000)

    random_number = f'{random_number_one} and {random_number_two} '

    while random_number_one != 0 and random_number_two != 0:
        if random_number_one > random_number_two:
            random_number_one = random_number_one % random_number_two
        else:
            random_number_two = random_number_two % random_number_one

    correct_answer = random_number_one + random_number_two

    return random_number, correct_answer
