#!/usr/bin/python -tt

from brain_games.engine import run
from brain_games.games import game_gcd


def main():
    run(game_gcd)


if __name__ == '__main__':
    main()
