import os.path
from collections import defaultdict

from advent.utilities import LOGGER, timing


class FileStruct:
    def __init__(self):
        self.paths = defaultdict(lambda: 0)

    def add_path(self, filename, size):
        filename = os.path.dirname(filename)
        self.paths[filename] += size
        if filename != '/':
            self.add_path(filename, size)

    def get_dir_by_max_size(self, max_size=0.):
        return {k: v for k, v in self.paths.items() if v <= max_size and '.' not in k}

    def get_total_size(self):
        return self.paths['/']

    def get_smallest_dir_gt_m(self, m):
        sorted_paths = sorted(self.paths.items(), key=lambda x: x[1])
        for k, v in sorted_paths:
            if v > m:
                return k, v


def navigate_file_structure(navigation):
    navigation = iter(navigation)
    fs = FileStruct()
    dir_node = next(navigation)[5:]
    for cmd in navigation:
        if cmd == '$ cd ..':
            # navigate to the directory parent
            dir_node = os.path.dirname(dir_node)
        elif cmd.startswith('$ cd'):
            # navigate to the subdirectory
            dir_node = os.path.join(dir_node, cmd[5:])
        elif not cmd.startswith('$ ls') and not cmd.startswith('dir'):
                size, name = cmd.split()
                fs.add_path(os.path.join(dir_node, name), float(size))
    return fs


@timing
def part_one(navigation):
    fs = navigate_file_structure(navigation)
    return sum(fs.get_dir_by_max_size(100_000).values())


@timing
def part_two(navigation):
    used_space_req = 40_000_000
    fs = navigate_file_structure(navigation)
    return fs.get_smallest_dir_gt_m(fs.get_total_size() - used_space_req)[1]


if __name__ == '__main__':
    with open('../resources/day_07.txt', 'r') as f:
        input_ = f.read().splitlines()
    LOGGER.info(part_one(input_))  # 1307902
    LOGGER.info(part_two(input_))  # 7068748
