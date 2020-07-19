from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_game():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = ('{} {}'.format(number1, number2))
    answer = str(gcd(number1, number2))
    return question, answer
