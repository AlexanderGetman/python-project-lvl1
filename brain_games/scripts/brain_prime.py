from brain_games.cli import welcome_user
from brain_games.games.brain_prime_logic import is_prime


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".\n')
    welcome_user()
    is_prime()


if __name__ == '__main__':
    main()
