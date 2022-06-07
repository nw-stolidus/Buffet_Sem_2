import random

print("How many random numbers do you want? ")
amount = input()
amount = int(amount)

thislist = []
for i in range(0,amount):
    thislist.append(random.randrange(1,11))

for i in range(0, amount):
    print(thislist[i], end=", ")
