from random import randint


DESCRIPTION = 'What number is missing in the progression?.'


def generate_game():
    progression_length = randint(3, 10)
    diff = randint(1, 10)
    initial_number = randint(1, 10)
    position_num = randint(0, progression_length - 1)
    i_progression = progression_length
    n = 0
    question = []
    while i_progression != 0:
        if progression_length == i_progression:
            question.append(initial_number)
            i_progression -= 1
        else:
            question.append(initial_number + n * diff)
            i_progression -= 1
        n += 1
    answer = str(question[position_num])
    question[position_num] = '..'
    question = " ".join(str(x) for x in question)
    return question, answer
