items = int(input("How many items are you going to buy? "))

list1 = []
list2 = []

for x in range(0,items):
    list1.append(input("What item are you buying? "))
    list2.append(float(input("How much is it? ")))
    print("Thanks for buying", list1[x])

for x in range(0,items):
    print(list1[x]," ... $", list2[x])

print("Your total is: $",sum(list2))

