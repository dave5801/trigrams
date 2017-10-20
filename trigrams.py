"""Trigrams."""

import sys
import os.path
import random


def main(file_path, length):
    """Main function."""
    words = open_file(file_path)
    vocab = create_dictionary(words)


def open_file(file_path):
    """Read a text document.

    Calls functions to generate a new randomized passage using
    words from the document.
    """
    if os.path.exists(file_path):
        file = open(file_path, 'r')
        return file.read().lower().split()


def create_dictionary(words):
    """Loop through text document words to create a dictionary.

    The first two words in each trigram make a key and the third
    is their value.
    """
    vocab = {}
    for i in range(len(words) - 2):
        pair = words[i] + " " + words[i + 1]
        third = words[i + 2]
        if pair in vocab:
            vocab[pair].append(third)
        else:
            vocab[pair] = [third]
    return vocab

print(create_dictionary(['a', 'b', 'c', 'd']))
