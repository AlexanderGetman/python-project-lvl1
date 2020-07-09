from random import randint


DESCRIPTION = 'What number is missing in the progression?.\n'


def generate_question():
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
    question_answer = str(question[position_num])
    question[position_num] = '..'
    return question, question_answer
