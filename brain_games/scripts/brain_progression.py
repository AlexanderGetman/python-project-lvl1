from brain_games.cli import welcome_user
from brain_games.games.brain_progression_logic import progression


def main():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?.\n')
    welcome_user()
    progression()


if __name__ == '__main__':
    main()
