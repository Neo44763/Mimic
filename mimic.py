import random
import sys


def mimic(dic, words):
    r = random.randint(0, len(words))
    print(words[r]),
    pivot = words[r]
    for i in range(0, 100):
        listOfWords = dic[pivot]
        x = random.randint(0, len(listOfWords) - 1)
        print listOfWords[x],
        pivot = listOfWords[x]


dic = {}
words = open(sys.argv[1]).read().split()
for i in range(len(words)):
    dic[words[i]] = [words[x+1] for x in range(len(words) - 1)
                     if words[x] == words[i]]

mimic(dic, words)
