from random import randint

RULES = 'What number is missing in the progression?'


def generate_round():
    random_number_one = randint(1, 10)
    random_number_two = randint(1, 10)
    secret_number = randint(0, 3)

    list_numbers = list(range(random_number_one, 100, random_number_two))
    short_list_numbers = list_numbers[:5]

    secret_number_list = short_list_numbers[secret_number]
    short_list_numbers[secret_number] = ".."

    return short_list_numbers, secret_number_list
