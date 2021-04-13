import os
import collections


def get_file_stat(dir):
    stat = collections.defaultdict(int)
    for root, _, files in os.walk(dir):
        for file in files:
            limit = get_limit_size(os.path.join(root, file))
            stat[limit] += 1
    return stat


def get_limit_size(file):
    """получить границу размера файла"""
    size = os.stat(file).st_size
    test_size = 10
    while True:
        if size < test_size:
            return test_size
        test_size *= 10


dir_for_stat = r"Lesson7_4\data"
for item_key, item_value in get_file_stat(dir_for_stat).items():
    print(item_key, item_value)