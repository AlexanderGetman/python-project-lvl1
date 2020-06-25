import prompt
import logging
from random import randint
from brain_games.cli import welcome_user


def parity_check():
    question = randint(0, 100)
    i = 3
    while i != 0:
        question = randint(0, 100)
        logging.info("Question: " + str(question))
        answer = prompt.string('Your answer: ')
        if question % 2 == 0 and answer == 'yes':
            logging.info('Correct!')
            i -= 1
        elif question % 2 != 0 and answer == 'no':
            logging.info('Correct!')
            i -= 1
        elif answer != 'yes' or answer != 'no':
            logging.info("Let's try again, " + welcome_user.name)
        if i == 0:
            logging.info("Congratulations, " + welcome_user.name + "!")
