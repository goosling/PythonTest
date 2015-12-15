__author__ = 'joe'

lst = []
words = ['abcde','fghij','klm','dhadhjhjhd']

for word in words:
    lst.append((len(word),word))
lst.sort(reverse = True)
print lst

res = []

for length, word in lst:
    res.append(word)
print res

words.sort(key = lambda x : len(x),reverse = True)
print words