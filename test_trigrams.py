""" python -m pytest test_trigrams.py"""
import pytest
import sys
import os.path


def test_invalid_file():
    from trigrams import open_file
    with pytest.raises(TypeError):
        open_file(123)


def test_valid_file():
    from trigrams import open_file
    assert isinstance(open_file("sherlock_small.txt"), list)


def test_dictionary():
    from trigrams import create_dictionary
    assert isinstance(create_dictionary(['a', 'b', 'c', 'd']), dict)
