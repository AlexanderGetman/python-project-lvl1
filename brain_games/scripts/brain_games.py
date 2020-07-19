from brain_games.cli import welcome_user
import logging


logging.basicConfig(format='%(message)s', level=logging.INFO)


def main():
    print("Welcome to the Brain Games!")
    welcome_user()


if __name__ == '__main__':
    main()
