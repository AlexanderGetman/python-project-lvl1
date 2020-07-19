import prompt
import logging
from brain_games.cli import welcome_user


def begin_game(game_logic):
    logging.info('Welcome to the Brain Games!')
    welcome_user()
    logging.info(game_logic.DESCRIPTION + '\n')


def get_user_answer():
    return prompt.string('Your answer: ')


def start_engine(game_logic):
    begin_game(game_logic)
    NUMBER_OF_TURNS = 3
    while NUMBER_OF_TURNS != 0:
        question, answer = game_logic.generate_game()
        logging.info("Question: " + str(question))
        inputed_answer = get_user_answer()
        if inputed_answer == answer:
            logging.info('Correct!\n')
            NUMBER_OF_TURNS -= 1
        else:
            logging.info(str(inputed_answer)
                         + ' is wrong answer ;(. Correct answer was '
                         + str(answer) + '.\n'
                         + "Let's try again, " + welcome_user.name + '!\n')
        if NUMBER_OF_TURNS == 0:
            logging.info("Congratulations, " + welcome_user.name + "!")
