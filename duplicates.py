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

    for first_file in files_to_check:
        paths = []
        for other_file in files_to_check:
            if first_file.name == other_file.name and \
                            first_file.size == other_file.size and \
                            first_file.dir_path != other_file.dir_path:
                paths.append(other_file.dir_path)
                files_to_check.remove(other_file)
        if paths:
            paths.insert(0, first_file.dir_path)
            new_duplicate = Duplicate(first_file.name, first_file.size, paths)
            duplicates.append(new_duplicate)
        files_to_check.remove(first_file)

    return duplicates


def print_duplicates(duplicates: list):
    if duplicates:
        for duplicate in duplicates:
            file_string = '\nThe file with name "{0}" and size of {1} bytes is found {2} times.'
            print(file_string.format(duplicate.name, duplicate.size, len(duplicate.all_paths)))
            print('These are the paths to all copies of this file:')
            for number, path in enumerate(duplicate.all_paths):
                print('{0}. {1}'.format(number + 1, os.path.join(path, duplicate.name)))
    else:
        print('There are no duplicates in this directory and its sub-directories.')

if __name__ == '__main__':
    pass
