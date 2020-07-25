from brain_games import engine
from brain_games.games import progression
import logging


logging.basicConfig(format='%(message)s', level=logging.INFO)


def main():
    engine.play(progression)


if __name__ == '__main__':
    main()
