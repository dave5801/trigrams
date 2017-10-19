""" python -m pytest test_trigrams.py"""
import pytest

def test_file_exists():
    from trigrams import main
    assert main("sherlock_small.txt") == True
    #assert main("") == True
   