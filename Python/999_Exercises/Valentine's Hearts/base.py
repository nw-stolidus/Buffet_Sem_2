import random

people_list = ["Noah", "Mom", "Dad", "Sister"]
comp_list = ["is smart", "has a great personality", "is fun","rocks!" ]

with open('People.txt') as f:
    for line in f:
        l = line.strip()
        people_list.append(l)

with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        comp_list.append(l)


peoplenum = random.randrange(0,len(people_list))
compnum = random.randrange(0,len(comp_list))

print(people_list[peoplenum] +" "+ comp_list[compnum])