""" python -m pytest test_trigrams.py"""
import pytest

def test_file_exists():
    from trigrams import open_file
    assert open_file("sherlock_small.txt") == True

   