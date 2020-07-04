import prompt
import logging
from random import randint
from brain_games.cli import welcome_user


def is_prime():
    i = 3
    while i != 0:
        number = randint(1, 3571)
        question = ('{}'.format(number))
        logging.info("Question: " + question)

        def prime_check(number):
            if number < 2:
                return False
            divider = 2
            while divider <= number / 2:
                if number % divider == 0:
                    return False
                divider += 1
            return True
        result = prime_check(number)
        result_answer = 'yes' if result == 1 else 'no'

        def incorrect_answer():
            logging.info(str(answer)
                         + ' is wrong answer ;(. Correct answer was '
                         + result_answer + '.\n'
                         + "Let's try again, " + welcome_user.name + '!\n')
        answer = prompt.string('Your answer: ')

        if result_answer == answer:
            logging.info('Correct!\n')
            i -= 1
        else:
            incorrect_answer()
            break
        if i == 0:
            logging.info("Congratulations, " + welcome_user.name + "!")
