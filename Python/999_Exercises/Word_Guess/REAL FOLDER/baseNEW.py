import random
thislist = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        thislist.append(l)

word = random.randrange(12971)

print("Guess a five letter word: ")
guess = str(input())

if guess == word:
    print("That's correct")
else:
    for x in range(0, 5):
        if guess == word:
            print("That's correct")
        else:
            print("Wrong! Guess again.")
            guess = str(input())
print("You failed.")