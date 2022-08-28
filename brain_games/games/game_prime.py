from random import randint
from brain_games.engine import welcome_user, user_lose

name = welcome_user("brain_prime")


def brain_prime():
    i = 1

    while i <= 3:

        r_number = randint(0, 100)
        number_is_prime = IsPrime(r_number)

        print(f'Question: {r_number} ')
        useranswer = str(input('Your answer: '))

        if number_is_prime == useranswer.lower():
            print("Correct!")
            i += 1
        else:
            user_lose(useranswer, number_is_prime, name)

    print(f"Congratulations, {name}!")


def IsPrime(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return 'no'
                break
        else:
            return 'yes'
    else:
        return 'no'
