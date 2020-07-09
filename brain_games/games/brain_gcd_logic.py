from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.\n'


def generate_question():
    numbers = (randint(0, 100), randint(0, 100))
    question = ('{} {}'.format(numbers[0], numbers[1]))
    question_answer = str(gcd(numbers[0], numbers[1]))
    return question, question_answer
