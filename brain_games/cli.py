import prompt
import logging


def welcome_user():
    welcome_user.name = prompt.string('May I have your name? ')
    logging.info("Hello, " + welcome_user.name + "!\n")
