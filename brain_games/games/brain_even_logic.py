from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".\n'


def generate_question():
    question = randint(1, 100)
    if question % 2 == 0:
        question_answer = 'yes'
    elif question % 2 != 0:
        question_answer = 'no'
    return question, question_answer
