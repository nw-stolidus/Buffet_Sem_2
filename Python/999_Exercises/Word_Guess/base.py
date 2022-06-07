import random
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        print(l)


thislist = []
thislist.append(l)
word = random.randrange(12971)

print("Guess a five letter word: ")
guess = str(input())

f.close()
