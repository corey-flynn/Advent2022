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
def part_one(elf_food):
    """return the value of the elf with the most food"""
    return max(get_elf_dict(elf_food).values())


@timing
def part_two(elf_food):
    """return the value of the three elves with the most food"""
    return sum(sorted(get_elf_dict(elf_food).values())[-3:])


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        elf_list = f.read().split('\n')
    LOGGER.info(f'PART ONE ANSWER: {part_one(elf_list)}')  # 67027
    LOGGER.info(f'PART TWO ANSWER: {part_two(elf_list)}')  # 197291
