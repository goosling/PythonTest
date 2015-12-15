__author__ = 'joe'
# -*- coding: utf-8 -*-

from sys import argv
print argv
script, filename = argv

txt = open(filename)

print 'here is your file %r:' % filename
print txt.read()

print 'Type the filename again'
file_again = raw_input("> ")
txt_again = open(file_again)

print txt_again.read()