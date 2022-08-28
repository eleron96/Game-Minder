from random import randint
from brain_games.engine import welcome_user, user_lose

name = welcome_user("brain_progression")


def random_number():
    for _ in range(3):
        expression_value = randint(1, 10)
    return expression_value


def random_number_secret():
    for _ in range(3):
        expression_secret = randint(0, 3)
    return expression_secret


def brain_progression():
    i = 1

    while i <= 3:
        number = random_number_secret()

        list_numbers = list(range(random_number(), 100, random_number()))
        short_list_numbers = list_numbers[:5]

        secret_number = short_list_numbers[number]
        short_list_numbers[number] = ".."

        print(f'Question: {short_list_numbers} ')
        useranswer = int(input('Your answer: '))

        if useranswer == secret_number:
            print("Correct!")
            i += 1
        else:
            user_lose(useranswer, secret_number, name)
    print(f"Congratulations, {name}!")
