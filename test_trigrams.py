""" python -m pytest test_trigrams.py"""
import pytest
import sys
import os.path


test_vocabulary = {'a b': 'c', 'b c': 'd', 'c d': 'e'}

def test_invalid_file():
    from trigrams import open_file
    with pytest.raises(TypeError):
        open_file(123)


def test_valid_file():
    """Test that open_file returns a list."""
    from trigrams import open_file
    assert isinstance(open_file("sherlock_small.txt"), list)


def test_dictionary():
    """Test that create_dictionary returns a dictionary object."""
    from trigrams import create_dictionary
    assert isinstance(create_dictionary(['a', 'b', 'c', 'd']), dict)


def test_dictionary_keys():
    """Test that expected keys are in dictionary."""
    from trigrams import create_dictionary
    assert 'a b', 'b c' in create_dictionary(['a', 'b', 'c', 'd'])


def test_generate_content_string():
    """Test generate content function returns string"""
    from trigrams import generate_content
    assert isinstance(generate_content(test_vocabulary, 10), str)

def test_find_words():
    from trigrams import find_words
    assert find_words(test_vocabulary) in test_vocabulary