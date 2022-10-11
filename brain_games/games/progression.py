from random import randint

RULES = 'What number is missing in the progression?'


def generate_round():
    start_progression_number = randint(1, 10)
    step_progression = randint(1, 10)
    random_index = randint(0, 5)

    roll_numbers = list(range(start_progression_number, 100, step_progression))
    short_range_numbers = roll_numbers[:7]

    hidden_range_numbers = short_range_numbers[random_index]
    short_range_numbers[random_index] = ".."
    short_range_numbers = " ".join(map(str, short_range_numbers))

    return short_range_numbers, str(hidden_range_numbers)
