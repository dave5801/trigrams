"""Trigram Tests."""
test_vocabulary = {'a b': 'c', 'b c': 'd', 'c d': 'e'}


def test_file_is_valid():
    """Test that get_words returns a list object."""
    from trigrams import get_words
    assert isinstance(get_words("sherlock_small.txt"), list)


def test_dictionary_returns_dictionary_object():
    """Test that create_dictionary returns a dictionary object."""
    from trigrams import create_dictionary
    assert isinstance(create_dictionary(['a', 'b', 'c', 'd']), dict)


def test_dictionary_keys_exist():
    """Test that expected keys are in dictionary."""
    from trigrams import create_dictionary
    assert 'a b', 'b c' in create_dictionary(['a', 'b', 'c', 'd'])


def test_generate_content_string_returns_valid():
    """Test generate content function returns string."""
    from trigrams import generate_content
    assert isinstance(generate_content(test_vocabulary, 10), str)


def test_find_trigram_key_pair():
    """Test find_trigram function selects valid random key from dictionary."""
    from trigrams import find_trigram
    assert find_trigram(test_vocabulary) in test_vocabulary


def test_find_trigram_third_word():
    """Test find_trigram.

    When passed with a pair of words that are a key in the dictionary,
    should select a random value for the key and return it to complete a
    trigram.
    """
    from trigrams import find_trigram
    assert find_trigram(test_vocabulary, 'a b') == 'c'


def test_main_text_length_returns_expected():
    """Test that main function returns meets the requested number of words."""
    from trigrams import main
    assert len((main('sherlock_small.txt', 50).split(" "))) >= 50
