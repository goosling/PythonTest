__author__ = 'joe'
# -*- coding: utf-8 -*-

import re, os

def get_files(path):
    filepath = os.listdir(path)
    files = []
    for fp in filepath:
        fppath = path+'/'+fp
        if(os.path.isfile(fppath)):
            files.append(fppath)
        # 子文件夹
        elif(os.path.isdir(fppath)):
            files += get_files(fppath)
    return files

def get_important_words(files):
    word_dict = {}
    for filename in files:
        f = open(filename, 'rb')
        s = f.read()
        pattern = r'[A-Za-z0-9]+'
        words = re.findall(pattern, s)
        for word in words:
            # easy and simple way to create the dict
            word_dict[word] = word_dict[word] + 1 if word in word_dict else 1
        f.close()
    wordsort = sorted(word_dict.items(), key=lambda e: e[1], reverse=True)
    return wordsort

if __name__ == '__main__':
    files = get_files('C:/Users/joe/Desktop/diary')
    print files
    wordsort = get_important_words(files)
    # 避免遗漏有多个最大值的情况
    maxnum = 1
    for i in range(len(wordsort) - 1):
        if wordsort[i][1] == wordsort[i+1][1]:
            maxnum += 1
        else:
            break
        for i in range(maxnum):
            print wordsort[i]



