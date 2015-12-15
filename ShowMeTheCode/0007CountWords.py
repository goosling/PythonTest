__author__ = 'joe'
# -*- coding: utf-8 -*-

import os
import glob
# get all files in a designated path
def get_files(path):
    return glob.glob(path+r'/*.py')

# count lines and blank lines and note lines in designated files
def count_lines(files):
    line, blank, note = 0, 0, 0
    for filename in files:
        f = open(filename, 'rb')
        for l in f:
            l = l.strip()
            line += 1
            if l == '':
                blank += 1
            elif l[0] == '#' or l[0] == '/':
                note += 1
        f.close()
    return (line,blank,note)
if __name__ == '__main__':
    files = get_files('.')
    print files
    lines = count_lines(files)
    print 'Lines(s): %d, black lines(s): %d, note line(s): %d' % (lines[0], lines[1], lines[2])

