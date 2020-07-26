import prompt
import logging


def play(game):
    logging.info('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    logging.info("Hello, " + user_name + "!\n")
    logging.info(game.DESCRIPTION + '\n')
    number_of_turns = 3
    while number_of_turns != 0:
        question, answer = game.generate_game()
        logging.info("Question: " + str(question))
        inputed_answer = prompt.string('Your answer: ')
        if inputed_answer == answer:
            logging.info('Correct!\n')
            number_of_turns -= 1
        else:
            return logging.info(str(inputed_answer)
                                + ' is wrong answer ;(. Correct answer was '
                                + str(answer) + '.\n'
                                + "Let's try again, "
                                + user_name + '!\n')
        logging.info("Congratulations, " + user_name + "!")
