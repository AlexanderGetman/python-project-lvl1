from brain_games import engine
from brain_games.games import prime
import logging


logging.basicConfig(format='%(message)s', level=logging.INFO)


def main():
    engine.play(prime)


if __name__ == '__main__':
    main()
