import prompt
import logging
from random import randint
from math import gcd
from brain_games.cli import welcome_user


def gcd_check():
    i = 3
    while i != 0:
        numbers = (randint(0, 100), randint(0, 100))
        question = ('{} {}'.format(numbers[0], numbers[1]))
        logging.info("Question: " + question)
        result = gcd(numbers[0], numbers[1])

        def incorrect_answer():
            logging.info(str(answer)
                         + ' is wrong answer ;(. Correct answer was '
                         + str(result) + '.\n'
                         + "Let's try again, " + welcome_user.name + '!\n')
        answer = prompt.string('Your answer: ')

        if answer.isdigit():
            if int(result) == int(answer):
                logging.info('Correct!\n')
                i -= 1
            else:
                incorrect_answer()
                break
        else:
            incorrect_answer()
            break
        if i == 0:
            logging.info("Congratulations, " + welcome_user.name + "!")
