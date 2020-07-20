import random
from random import randint
import operator


DESCRIPTION = 'What is the result of the expression?'


def generate_game():
    number1 = randint(1, 25)
    number2 = randint(1, 25)
    operators = ('+', '-', '*')
    random_operator = random.choice(operators)
    question = ('{} {} {}'.format(number1,
                random_operator, number2))
    if random_operator == '+':
        result = operator.add(number1, number2)
    elif random_operator == '-':
        result = operator.sub(number1, number2)
    else:
        result = operator.mul(number1, number2)
    answer = str(result)
    return (question, answer)
