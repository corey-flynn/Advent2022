from collections import defaultdict

from advent.utilities import LOGGER, timing


def get_elf_dict(elf_food) -> dict:
    counter = 0
    elf_dict = defaultdict(lambda: 0)
    for food in elf_food:
        if food == '':
            counter += 1
        else:
            elf_dict[counter] += int(food)
    return elf_dict


@timing
def get_n_elves(elf_food, n: int = 3):
    """return the value of the three elves with the most food"""
    return sum(sorted(get_elf_dict(elf_food).values())[-n:])


if __name__ == '__main__':
    with open('../resources/day_01.txt', 'r') as f:
        elf_list = f.read().split('\n')
    LOGGER.info(f'PART ONE ANSWER: {get_n_elves(elf_list, 1)}')  # 67027
    LOGGER.info(f'PART TWO ANSWER: {get_n_elves(elf_list, 3)}')  # 197291
