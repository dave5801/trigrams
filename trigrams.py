import sys
import os.path

def create_dictionary(words):
    new_content = {}
    for i in range(len(words) - 2):
        new_content[words[i] + " " + words[i + 1]] = words[i + 2]

    return new_content


def store_file(file_path):
    new_content = {}

    if os.path.exists(file_path):
        file = open(file_path, 'r')
        words = file.read().split()
        new_content = create_dictionary(words)
    print new_content

store_file("sherlock_small.txt")
