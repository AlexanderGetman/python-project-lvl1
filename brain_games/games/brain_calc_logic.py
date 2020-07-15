import random
from random import randint


DESCRIPTION = 'What is the result of the expression?'


def generate_game():
    number1 = randint(1, 25)
    number2 = randint(1, 25)
    operators = ('+', '-', '*')
    operator = random.choice(operators)
    question = ('{} {} {}'.format(number1,
                operator, number2))
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2
    answer = str(result)
    return (question, answer)
