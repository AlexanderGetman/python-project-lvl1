import prompt
import logging
from brain_games.cli import welcome_user


TURNS = 3
logging.basicConfig(format='%(message)s', level=logging.INFO)


def game_introduction(game_logic):
    logging.info('Welcome to the Brain Games!')
    welcome_user()
    logging.info(game_logic.DESCRIPTION)


def user_answer():
    return prompt.string('Your answer: ')


def start_engine(game_logic):
    game_introduction(game_logic)
    i = TURNS
    while i != 0:
        question, question_answer = game_logic.generate_question()
        logging.info("Question: " + str(question))
        answer = user_answer()
        if answer == question_answer:
            logging.info('Correct!')
            i -= 1
        else:
            logging.info(str(answer)
                         + ' is wrong answer ;(. Correct answer was '
                         + str(question_answer) + '.\n'
                         + "Let's try again, " + welcome_user.name + '!\n')
        if i == 0:
            logging.info("Congratulations, " + welcome_user.name + "!")
