#!/usr/bin/python -tt


from brain_games.engine import welcome_user, ask_name, welcome_user_by_name, round_start, user_answer, \
    user_lose, game_rules
from brain_games.games import game_even


def main():
    welcome_user()
    name = ask_name()
    welcome_user_by_name(name)
    # game_rules("brain_even")
    round_start(game_even)


if __name__ == '__main__':
    main()
