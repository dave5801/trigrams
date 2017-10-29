"""Trigrams."""
import sys
import os.path
import random


def main(file_path, length):
    """Main function.

    Calls functions to generate a new randomized passage using
    words from the document.
    """
    words = get_words(file_path)
    vocab = create_dictionary(words)
    new_content = generate_content(vocab, length)
    return new_content


def get_words(file_path):
    """Read a text document.

    Return a list of each word from the document.
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


def generate_content(vocab, length):
    """Generate a random passage.

    Pass in a dictionary of words from a text document and a specified
    length (number of words) to return a randomized string.
    """
    new_content = []
    pair = find_trigram(vocab)
    while len(new_content) < length:
        third = find_trigram(vocab, pair)
        trigram = (pair + " " + third).split()
        new_content.extend(*[trigram])  # unpack trigrams and add to content
        next_one = find_trigram(vocab, trigram[1] + " " + trigram[2])
        if len(next_one.split()) > 1:
            pair = next_one
        else:
            next_two = find_trigram(vocab, trigram[2] + " " + next_one)
            pair = next_one + " " + next_two
    return " ".join(new_content)


def find_trigram(vocab, pair=False):
    """Find random set of related words in the vocab dictionary.

    If a valid pair is passed, return the third word in the trigram.
    Otherwise, randomly choose and return a key pair from the dictionary.
    """
    if pair in vocab:
        return random.choice(vocab[pair])
    return random.choice(list(vocab))


if __name__ == '__main__':
    """Run app from the console.

    Type 'python trigrams.py' followed by a text file name and the
    desired number of words to generate text and print it to the console.
    """
    print(main(sys.argv[1], int(sys.argv[2])))
