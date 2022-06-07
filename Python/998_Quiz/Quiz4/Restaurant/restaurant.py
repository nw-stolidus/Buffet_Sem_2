import random

restaurantlist = [" Giovanni's,"," Burn Bakery,", " or Sushi Bois" ]
print("Do you want to go to", end = " ")
for i in range(0, len(restaurantlist)):
    print(restaurantlist[i],end="")
print("?")
take = str(input())

itemlist = []


if take == "Giovanni's":
    itemlist = ["Margherita Pizza","Spaghettini","Ravioli"]
    x = random.randrange(0,len(itemlist))
    for i in range(0,len(itemlist)):
        print(itemlist[i], end=", ")
    print("I recommend the "+itemlist[x])


if take == "Burn Bakery":
    itemlist = ["Bread Pudding","Cheesecake","Brioche"]
    x = random.randrange(0,len(itemlist))
    for i in range(0,len(itemlist)):
        print(itemlist[i], end=", ")
    print("I recommend the "+itemlist[x])


if take == "Sushi Bois":
    itemlist = ["Sashimi","Salmon Roll","Spicy Tuna"]
    x = random.randrange(0,len(itemlist))
    for i in range(0,len(itemlist)):
        print(itemlist[i], end=", ")
    print("I recommend the "+itemlist[x])



