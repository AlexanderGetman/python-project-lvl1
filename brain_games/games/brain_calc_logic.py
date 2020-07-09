import random
from random import randint


DESCRIPTION = 'What is the result of the expression?\n'


def generate_question():
    numbers = (randint(1, 25), randint(1, 25))
    operators = ('+', '-', '*')
    question = ('{} {} {}'.format(numbers[0],
                random.choice(operators), numbers[1]))
    question_answer = str(eval(question))
    return (question, question_answer)
