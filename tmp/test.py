import os.path

file_path = 'sherlock_smaller.txt'


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
    try:
        file = open(file_path, 'r')
        return file.read().lower().split()
    except OSError:
        print("Wrong file or file path")

def create_dictionary(words):
    print(words)
    return "getting words"

def generate_content(vocab, length):
    return "generating content"

main(file_path, 500)

