import random


def gen_list() -> list:
    #Генератор списка
    return list(random.randint(-9, 99) for _ in range(random.randint(1, 50)))