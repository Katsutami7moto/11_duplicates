import os
from os.path import join, getsize, exists
from collections import namedtuple

File = namedtuple('File', 'name size dir_path')
Duplicate = namedtuple('Duplicate', 'name size all_paths')


def find_duplicates(source_path: str) -> list:
    files_to_check = []
    duplicates = []

    for root, dirs, files in os.walk(source_path):
        if files:
            for file in files:
                file_size = getsize(join(root, file))
                new_file = File(file, file_size, root)
                files_to_check.append(new_file)

    return duplicates


def print_duplicates(duplicates: list):
    pass

if __name__ == '__main__':
    pass
