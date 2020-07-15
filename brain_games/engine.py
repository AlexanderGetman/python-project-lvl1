import prompt
import logging
from brain_games.cli import welcome_user


NUMBER_OF_TURNS = 3
logging.basicConfig(format='%(message)s', level=logging.INFO)


def game_introduction(game_logic):
    logging.info('Welcome to the Brain Games!')
    welcome_user()
    logging.info(game_logic.DESCRIPTION + '\n')


def user_answer():
    return prompt.string('Your answer: ')


def start_engine(game_logic):
    game_introduction(game_logic)
    i = NUMBER_OF_TURNS
    while i != 0:
        question, answer = game_logic.generate_game()
        logging.info("Question: " + str(question))
        inputed_answer = user_answer()
        if inputed_answer == answer:
            logging.info('Correct!\n')
            i -= 1
        else:
            logging.info(str(inputed_answer)
                         + ' is wrong answer ;(. Correct answer was '
                         + str(answer) + '.\n'
                         + "Let's try again, " + welcome_user.name + '!\n')
        if i == 0:
            logging.info("Congratulations, " + welcome_user.name + "!")
