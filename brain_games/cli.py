import prompt
import logging


def welcome_user():
    name = prompt.string('May I have your name? ')
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    logging.warning("Hello, " + name + "!")
