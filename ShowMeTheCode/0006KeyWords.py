__author__ = 'joe'
# -*- coding: utf-8 -*-

import re
import os

diaries_path = 'C:/Users/joe/Desktop/diary'
diaries = os.listdir(diaries_path)

# set stop words to make informative keywords
stop_words = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 's', 'is', 'are', 'a', 'with', 'as', 'an']
# stop_words = open('stop_words.txt', 'r').read()
stop_words_list = stop_words.split(' ')

# find 5 keywords in a txt
def find_keywords(words):
    words_dictionary = {}
    for word in words:
        if word.lower() not in words_dictionary and word.lower() not in stop_words_list:
            words_dictionary[word] = 0
            for item in words:
                if item == word:
                    words_dictionary[word] += 1
    keywords = sorted(words_dictionary, key=words_dictionary.__getitem__(), reverse=True)[0:5]
    return keywords

for diary in diaries:
    # with open(diaries_path + diary, 'r',  errors='ignore') as content:
    content = open(diaries_path+'/'+diary, 'r')

    diary_words_list = re.findall(r'[\w]+', content.read())
    print('The keywords of diary'+diary+'is:')
    print(find_keywords(diary_words_list))