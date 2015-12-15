__author__ = 'joe'
# -*- coding: utf-8 -*-
import re

def read_file(filename):
    l = []
    with open(filename, 'r') as fp:
        for line in fp.readlines():
            l.append(line.strip())
    return l
# generate the pattern
def gene_pattern(l):
    pattern = ''
    for string in l:
        pattern += string + '|'

    return pattern[:-1]

def input_replace(pattern, filename):
    sentence = raw_input('please enter a sentence:')
    with open(filename, 'r'):

        print re.sub(pattern, '**', sentence)

def main():
    filename = 'filtered_words.txt'
    l = read_file(filename)
    pattern = gene_pattern(l)
    print pattern
    input_replace(pattern)

if __name__ == '__main__':
    main()