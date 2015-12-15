__author__ = 'joe'

f = open('emma.txt')

word_freq = {}

for line in f:
    words = line.strip().split()
    for word in words:
        if word in word_freq:
            word_freq += 1
        else:
            word_freq = 1

freq_word = []

for word,freq in word_freq.items():
    freq_word.append((freq,word))

freq_word.sort(reverse = True)
for freq,word in freq_word[:10]:
    print word

f.close()