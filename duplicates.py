import os
from os.path import join, getsize, exists
from collections import namedtuple

File = namedtuple('File', 'name size dir_path')
Duplicate = namedtuple('Duplicate', 'name size all_paths')


def find_duplicates(source_path: str) -> list:
    pass


def print_duplicates(duplicates: list):
    pass

if __name__ == '__main__':
    pass
