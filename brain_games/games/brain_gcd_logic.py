from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_game():
    numbers = (randint(0, 100), randint(0, 100))
    question = ('{} {}'.format(numbers[0], numbers[1]))
    answer = str(gcd(numbers[0], numbers[1]))
    return question, answer
