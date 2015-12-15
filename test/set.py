__author__ = 'joe'

#encoding = utf-8

def load_dict(filename):
    word_dict = set()
    max_len = 1
    f = open(filename)
    for line in f:
        word = unicode(line.strip(),'utf-8')
        word_dict.add(word)
        if len(word) > max_len:
            max_len = len(word)

    return max_len,word_dict

def fmm_max_seg(sent, max_len, word_dict):
    begin = 0
    words = []
    sent = unicode(sent, 'utf-8')

    while begin < len(sent):
        for end in range(begin+max_len, begin, -1):
            if sent[begin:end] in word_dict:
                words.append(sent[begin:end])
                break
        begin = end

    return words

def f1 (my_dict):
    temp = 0
    for value in my_dict.values():
        temp = temp + value
    return temp

a_dict={'bill':1,'rich':2,'fred':10,'walter':20}
print f1(a_dict)

for thief in ['a', 'b', 'c', 'd']:
    sum = (thief != 'a') + (thief == 'c') + (thief == 'd') + (thief != 'd')
    if sum == 3:
        print 'thief is:',thief