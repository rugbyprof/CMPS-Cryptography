from math import log
import time
import os
import sys
import re
import operator

# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open("words-by-frequency1.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        for k,c in candidates:
            print(k,c)
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))

def load_frequency_dictionary(freq_dictionary):
    rootdir = "./books"
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            path =  os.path.join(subdir, file)
            print(path)
            f=open(path,'r')
            for line in f.readlines():
                line = line.split(' ')
                line[-1] = line[-1].strip('\n')
                if len(line) == 1 and line[0] == '':
                    continue
                for word in line:
                    word = word.upper()
                    word = re.sub('[^A-Za-z]+', '', word)
                    if word == '':
                        continue
                    freq_dictionary[word] = freq_dictionary.get(word, 0) + 1
            print(len(freq_dictionary))
            f.close()


if __name__ == '__main__':

    #start = time.time()

    s = 'thethumbgreenappleactiveassignmentweeklymetaphor'
    print(infer_spaces(s))

    #end = time.time()

    #print(end-start)

    frequency_dictionary = {}

    start = time.time()

    #load_frequency_dictionary(frequency_dictionary)

    #sorted_frequency_dictionary = sorted(frequency_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    #print(sorted_frequency_dictionary)
    end = time.time()

    print(end-start)

    print(len(frequency_dictionary))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))
