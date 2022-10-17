from random import randint

RULES = 'What number is missing in the progression?'


def generate_round():
    start_progression_number = randint(1, 10)
    step_progression = randint(1, 10)
    random_index = randint(0, 5)

    progression = list(range(start_progression_number, 100, step_progression))
    short_range_number = progression[:7]

    hidden_range_number = short_range_number[random_index]
    short_range_number[random_index] = ".."
    short_range_number = " ".join(map(str, short_range_number))

    return short_range_number, str(hidden_range_number)
