from random import randint
from brain_games.engine import welcome_user, user_lose

name = welcome_user("brain_gcd")


def brain_gcd():
    # Start Function
    i = 1

    while i <= 3:
        answer = 0

        a = expression_value = randint(0, 1000)
        b = expression_value = randint(0, 1000)

        print(f'Question: {a} and {b} ')

        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        answer = a + b

        useranswer = int(input('Your answer: '))

        if useranswer == answer:
            print("Correct!")
            i += 1
        else:
            user_lose(useranswer, answer, name)

    print(f"Congratulations, {name}!")
