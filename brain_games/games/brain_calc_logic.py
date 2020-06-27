import prompt
import logging
import operator
import random
from random import randint
from brain_games.cli import welcome_user


def calc_check():
    i = 3
    while i != 0:
      numbers = (randint(1, 25), randint(1, 25))
      operators = ('+', '-', '*')
      question = ('{} {} {}'.format(numbers[0], random.choice(operators), numbers[1]))
      logging.info("Question: " + question)
      answer = prompt.string('Your answer: ')
      if int(eval(question)) == int(answer):
        logging.info('Correct!\n')
        i -= 1
      else:
          logging.info(str(answer) + ' is wrong answer ;(. Correct answer was ' + str(eval  (question)) + '.\n')
      if i == 0:
          logging.info("Congratulations, " + welcome_user.name + "!")