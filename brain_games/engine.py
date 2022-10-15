import prompt

GAME_ROUNDS = 3


def run(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.RULES)

    for _ in range(GAME_ROUNDS):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  + f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
