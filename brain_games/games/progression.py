from random import randint

RULES = 'What number is missing in the progression?'


def generate_round():
    random_number_one = randint(1, 10)
    random_number_two = randint(1, 10)
    hidden_number = randint(0, 3)

    roll_numbers = list(range(random_number_one, 100, random_number_two))
    short_list_numbers = roll_numbers[:7]

    secret_number_list = str(short_list_numbers[hidden_number])
    short_list_numbers[hidden_number] = ".."
    short_list_numbers = " ".join(map(str, short_list_numbers))

    return short_list_numbers, secret_number_list
