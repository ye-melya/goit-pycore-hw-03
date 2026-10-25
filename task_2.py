import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > max:
        return []
    if quantity < min or quantity > max:
        return []
    if quantity > max - min + 1:
        return []
    lottery_numbers = random.sample(range(min, max + 1), quantity)
    lottery_numbers.sort()

    return lottery_numbers
