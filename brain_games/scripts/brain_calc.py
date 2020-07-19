from brain_games import engine
from brain_games.games import calc
import logging


logging.basicConfig(format='%(message)s', level=logging.INFO)


def main():
    engine.start_engine(calc)


if __name__ == '__main__':
    main()
