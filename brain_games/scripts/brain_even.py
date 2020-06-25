from brain_games.cli import welcome_user
from brain_games.game_logic import parity_check


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n')
    welcome_user()
    parity_check()


if __name__ == '__main__':
    main()
