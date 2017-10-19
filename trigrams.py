"""Trigrams.py ."""


import sys
import os.path


def store_file(file_path):

    d = {}

    file = ""
    ''''
    '''
    if os.path.exists(file_path):
        file = open(file_path, 'r')
        tmp1 = file.read()
        tmp2 = tmp1.split()
        for i in tmp2:
            d[i] = []
    print d

store_file("sherlock_small.txt")

'''
def main(file_path):
    """main ethod ."""

if __name__ == '__main__':
    """call main ethod ."""
'''