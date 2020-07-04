import prompt
import logging
from random import randint
from brain_games.cli import welcome_user


def progression_check():
    i = 3
    while i != 0:
        progression_length = randint(3, 10)
        prog_sequence = randint(1, 10)
        initial_number = randint(1, 10)
        position_num = randint(0, progression_length - 1)
        i_progression = progression_length
        n = 0
        question = []
        while i_progression != 0:
            n += 1
            if progression_length == i_progression:
                question.append(initial_number)
                i_progression -= 1
            else:
                question.append(initial_number + (n - 1) * prog_sequence)
                i_progression -= 1
        puzzle = question[position_num]
        question[position_num] = '..'
        logging.info("Question: " + " ".join(str(x) for x in question))

        def incorrect_answer():
            logging.info(str(answer)
                         + ' is wrong answer ;(. Correct answer was '
                         + str(puzzle) + '.\n'
                         + "Let's try again, " + welcome_user.name + '!\n')
        answer = prompt.string('Your answer: ')

        if answer.isdigit():
            if int(puzzle) == int(answer):
                logging.info('Correct!\n')
                i -= 1
            else:
                incorrect_answer()
                break
        else:
            incorrect_answer()
            break
        if i == 0:
            logging.info("Congratulations, " + welcome_user.name + "!")
