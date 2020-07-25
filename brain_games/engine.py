import prompt
import logging


def get_user_answer():
    return prompt.string('Your answer: ')


def welcome_user():
    welcome_user.name = prompt.string('May I have your name? ')
    logging.info("Hello, " + welcome_user.name + "!\n")


def play(game):
    logging.info('Welcome to the Brain Games!')
    welcome_user()
    logging.info(game.DESCRIPTION + '\n')
    number_of_turns = 3
    while number_of_turns != 0:
        question, answer = game.generate_game()
        logging.info("Question: " + str(question))
        inputed_answer = get_user_answer()
        if inputed_answer == answer:
            logging.info('Correct!\n')
            number_of_turns -= 1
        else:
            return logging.info(str(inputed_answer)
                                + ' is wrong answer ;(. Correct answer was '
                                + str(answer) + '.\n'
                                + "Let's try again, "
                                + welcome_user.name + '!\n')
        logging.info("Congratulations, " + welcome_user.name + "!")
