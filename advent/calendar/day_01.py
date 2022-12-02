from collections import defaultdict
from typing import Iterable

from advent.utilities import LOGGER, timing


def get_elf_dict(elf_food: Iterable) -> dict:
    counter = 0
    elf_dict = defaultdict(lambda: 0)
    for food in elf_food:
        if food == '':
            counter += 1
        else:
            elf_dict[counter] += int(food)
    return elf_dict


@timing
def get_n_elves(elf_food: Iterable, n: int = 3) -> int:
    """
    return the sum of food from the elves with the n most
    :param elf_food: iterable from input
    :param n: number of elves to sum food
    :return: sum of food from n top elves
    """
    return sum(sorted(get_elf_dict(elf_food).values())[-n:])


if __name__ == '__main__':
    with open('../resources/day_01.txt', 'r') as f:
        elf_list = f.read().split('\n')
    LOGGER.info(f'PART ONE ANSWER: {get_n_elves(elf_list, 1)}')  # 67027
    LOGGER.info(f'PART TWO ANSWER: {get_n_elves(elf_list, 3)}')  # 197291
