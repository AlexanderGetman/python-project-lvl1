from random import randint


DESCRIPTION = 'What number is missing in the progression?.'


def generate_game():
    progression_length = randint(3, 10)
    diff = randint(1, 10)
    initial_number = randint(1, 10)
    position_num = randint(0, progression_length - 1)
    index = 0
    while index != progression_length:
        if index == 0:
            progression = [initial_number, ]
        else:
            progression.append(initial_number + (index * diff))
        index += 1
    answer = str(progression[position_num])
    progression[position_num] = '..'
    question = " ".join(str(x) for x in progression)
    return question, answer
