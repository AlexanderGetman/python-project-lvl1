from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_check(number):
    if number < 2:
        return False
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1
    return True


def generate_game():
    number = randint(1, 3571)
    question = ('{}'.format(number))
    answer = 'yes' if prime_check(number) == 1 else 'no'
    return question, answer
