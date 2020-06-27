from brain_games.cli import welcome_user
from brain_games.games.brain_calc_logic import calc_check


def main():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?.\n')
    welcome_user()
    calc_check()


if __name__ == '__main__':
    main()
