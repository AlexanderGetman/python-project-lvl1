from brain_games.cli import welcome_user
from brain_games.games.brain_gcd_logic import gcd_check


def main():
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.\n')
    welcome_user()
    gcd_check()


if __name__ == '__main__':
    main()