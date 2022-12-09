from enum import Enum

from advent.utilities import LOGGER, timing


class Dir(Enum):
    U = (0, 1)
    D = (0, -1)
    L = (-1, 0)
    R = (1, 0)


def tail_follow(head, tail):
    diff = tuple(x[0] - x[1] for x in zip(head, tail))
    match diff:
        case (2, 0):
            return tail[0] + 1, tail[1]
        case (-2, 0):
            return tail[0] - 1, tail[1]
        case (0, 2):
            return tail[0], tail[1] + 1
        case (0, -2):
            return tail[0], tail[1] - 1
        case (2, 1) | (1, 2) | (2, 2):
            return tail[0] + 1, tail[1] + 1
        case (-2, -1) | (-1, -2) | (-2, -2):
            return tail[0] - 1, tail[1] - 1
        case (1, -2) | (2, -1) | (2, -2):
            return tail[0] + 1, tail[1] - 1
        case (-1, 2) | (-2, 1) | (-2, 2):
            return tail[0] - 1, tail[1] + 1
        case _:
            return tail


def followers(directions, rope_len=1):
    head_xy = (0, 0)
    head_path = list()
    for dir_, len_ in directions:
        len_ = int(len_)
        for _ in range(len_):
            head_xy = tuple(sum(x) for x in zip(head_xy, Dir[dir_].value))
            head_path.append(head_xy)

    for _ in range(rope_len):
        tail_xy = (0, 0)
        tail_path = list()
        for head_xy in head_path:
            tail_xy = tail_follow(head_xy, tail_xy)
            tail_path.append(tail_xy)
        head_path = tail_path.copy()
    return tail_path


@timing
def part_one(directions):
    return len(set(followers(directions)))


@timing
def part_two(directions):
    return len(set(followers(directions, 9)))


if __name__ == '__main__':
    with open('../resources/day_09.txt', 'r') as f:
        input_ = [x.split() for x in f.read().splitlines()]
    LOGGER.info(part_one(input_))  # 6745
    LOGGER.info(part_two(input_))  # 2793
