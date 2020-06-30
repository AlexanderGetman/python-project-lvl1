import prompt
import logging
import random
from random import randint
from brain_games.cli import welcome_user


def calc_check():
    i = 3
    while i != 0:
        numbers = (randint(1, 25), randint(1, 25))
        operators = ('+', '-', '*')
        question = ('{} {} {}'.format(numbers[0],
                    random.choice(operators), numbers[1]))
        logging.info("Question: " + question)

        def incorrect_answer():
            logging.info(str(answer)
                         + ' is wrong answer ;(. Correct answer was '
                         + str(eval(question)) + '.\n'
                         + "Let's try again, " + welcome_user.name + '!\n')
        answer = prompt.string('Your answer: ')
        if answer.isdigit():
            if abs(int(eval(question))) == int(answer):
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
